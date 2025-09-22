<script setup lang="ts">
import { ref, watch, onMounted, computed } from 'vue';
import axios from "axios";
import Swal from 'sweetalert2';
import Header from '../components/Header.vue';
import { useRouter } from 'vue-router';
import EditAprendizModal from '../components/EditAprendizModal.vue'
import TablesAprendiz from '../components/GROUPFORMAT/TablesAprendiz.vue';
import EditFicha from '../components/EditFicha.vue';
import GroupInstructions from '../components/GroupInstructions.vue'
import { authService } from '../services/auth_service';

// Interfaces
interface Aprendiz {
  tipo_documento: string
  documento: string
  nombre: string
  apellido: string
  celular: string
  correo: string
  direccion: string
  estado: string
  editado?: boolean
  discapacidad?: string
  tipo_discapacidad?: string
  firma?: string
}

interface Usuario {
  nombre: string;
  apellidos: string;
  correo: string;
  rol: string;
}

interface UsuarioGenerador {
  id?: number;
  nombre: string;
  apellidos: string;
  correo: string;
  rol: string;
}

interface AprendizParaExportar {
  tipo_documento: string;
  documento: string;
  nombre: string;
  apellido: string;
  celular: string;
  correo: string;
  direccion: string;
  discapacidad: string;
  tipo_discapacidad: string;
  modalidad: string;
  firma?: string;
}

const usuarioGenerador = ref<UsuarioGenerador>({
  id: 0,
  nombre: '',
  apellidos: '',
  correo: '',
  rol: ''
});

const informacionAdicional = ref({
  nivel_formacion: '',
  modalidad_formacion: '',
  trimestre: '',
  fecha_inicio_etapa_productiva: '',
  jornada: ''
})

const aprendices = ref<Aprendiz[]>([])
const aprendices_editados = ref<Aprendiz[]>([])
let ficha = ref<string>('');
const busquedaRealizada = ref(false);
const mostrarResultados = ref(false);
const cargando = ref(false)
const fichaEditada = ref(false)

// Variables para el modal de edición
const mostrarModal = ref(false)
const mostrarModalFicha = ref(false)
const aprendizSeleccionado = ref<Aprendiz | null>(null)

const aprendicesExportar = ref<AprendizParaExportar[]>([]);
const modalidad = 'grupal'
const router = useRouter()

const currentUser = ref<Usuario | null>(null)

const isFormReadonly = ref(true) // Para hacer los campos de solo lectura inicialmente

// Computed para separar aprendices editados y no editados
const aprendicesNoEditados = computed(() =>
  aprendices.value.filter(a => !a.editado)
)

const aprendicesEditados = computed(() =>
  aprendices.value.filter(a => a.editado)
)

// Función para obtener los datos del usuario logueado
const getCurrentUser = (): Usuario | null => {
  try {
    const userStr = localStorage.getItem('user')
    if (userStr) {
      return JSON.parse(userStr)
    }
    return null
  } catch (error) {
    console.error('Error al obtener datos del usuario:', error)
    return null
  }
}

// Función para verificar si el token es válido
const isTokenValid = (): boolean => {
  const token = localStorage.getItem('access_token')
  if (!token) return false

  try {
    // Decodificar el JWT para verificar si no ha expirado
    const payload = JSON.parse(atob(token.split('.')[1]))
    const currentTime = Date.now() / 1000

    return payload.exp > currentTime
  } catch (error) {
    console.error('Error al verificar token:', error)
    return false
  }
}

// Función para cargar los datos del usuario automáticamente
const loadUserData = () => {
  // Verificar si hay un token válido
  if (!isTokenValid()) {
    // Redirigir al login si no hay token válido
    router.push('/')
    return
  }

  // Obtener datos del usuario
  const user = getCurrentUser()

  if (user) {
    currentUser.value = user

    // Autocompletar el formulario con los datos del usuario
    usuarioGenerador.value = {
      id: user.id || 0,
      nombre: user.nombre,
      apellidos: user.apellidos,
      correo: user.correo,
      rol: user.rol
    }

    console.log('Datos del usuario cargados automáticamente:', user)
  } else {
    // Si no hay datos de usuario, redirigir al login
    router.push('/')
  }
}

// Función para permitir editar los campos (opcional)
const toggleEditMode = () => {
  isFormReadonly.value = !isFormReadonly.value
}

// Función para resetear a los datos originales del usuario
const resetToUserData = () => {
  if (currentUser.value) {
    usuarioGenerador.value = {
      nombre: currentUser.value.nombre,
      apellidos: currentUser.value.apellidos,
      correo: currentUser.value.correo,
      rol: currentUser.value.rol
    }
  }
}

// Función para cargar aprendices
const cargarAprendicesFicha = async (codigoFicha: String) => {
  cargando.value = true;

  try {
    await new Promise(resolve => setTimeout(resolve, 800));
    const respuesta = await axios.get(`http://127.0.0.1:8000/ficha/${codigoFicha}/aprendices`);

    if (respuesta.data.archivo_existente) {
      console.log(respuesta.data.archivo_existente)
      Swal.fire({
        icon: "info",
        title: "Archivo ya generado",
        text: "Ya existe un archivo generado para esta ficha",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Descargar",
        confirmButtonColor: "#059669",
        denyButtonText: "Editar Archivo",
        denyButtonColor: "#3085d6",
        cancelButtonText: "Cancelar",
        cancelButtonColor: "#d33",
        customClass: {
          popup: 'mi-alerta'
        },
        // Solución para evitar el padding en el body
        willOpen: () => {
          document.body.style.paddingRight = '0px';
        },
        didClose: () => {
          document.body.style.paddingRight = '';
        }
      }).then(async (result) => {
        if (result.isConfirmed) {
          try {
            // Mostrar loading
            Swal.fire({
              title: 'Descargando...',
              allowOutsideClick: false,
              customClass: {
                popup: 'mi-alerta'
              },
              didOpen: () => {
                Swal.showLoading();
              }
            });

            const response = await axios.get(
              `http://127.0.0.1:8000/descargar-archivo?ruta=${encodeURIComponent(respuesta.data.ruta_archivo)}`,
              {
                responseType: 'blob', // Importante para archivos
              }
            );

            // Crear un blob y descargarlo
            const blob = new Blob([response.data], {
              type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            });

            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `formato_F165_ficha_${codigoFicha}.xlsx`; // Nombre del archivo
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            window.URL.revokeObjectURL(url);

            Swal.close();
            Swal.fire('¡Éxito!', 'Archivo descargado correctamente', 'success');

    } catch (error) {
      Swal.close();
      Swal.fire('Error', 'No se pudo descargar el archivo', 'error');
      console.error('Error descargando:', error);
    }
  } else if (result.isDenied) {
    aprendices.value = respuesta.data.aprendices;
    busquedaRealizada.value = true;
    mostrarResultados.value = true;
        aprendicesExportar.value = respuesta.data.aprendices
    .filter(a => a.editado)
    .map(ap => ({
      tipo_documento: ap.tipo_documento,
      documento: ap.documento,
      nombre: ap.nombre,
      apellido: ap.apellido,
      direccion: ap.direccion || '', 
      correo: ap.correo,
      celular: ap.celular,
      discapacidad: ap.discapacidad.toUpperCase() || 'NO', 
      tipo_discapacidad: ap.tipo_discapacidad || 'N/A', 
      modalidad: modalidad,
      firma: ap.firma || '' 
    }));
    console.log("Aprendices para editados:", aprendices.value)

  }
});
      return;
    }
    aprendices.value = respuesta.data.aprendices;


    busquedaRealizada.value = true;
    mostrarResultados.value = true;

  } catch (error) {
    console.error('Error al cargar los aprendices ', error);
    aprendices.value = []
    busquedaRealizada.value = true;
    mostrarResultados.value = true;
  } finally {
    cargando.value = false;
  }
}

watch(aprendices, (newVal) => {
  aprendices_editados.value = newVal.filter(a => a.editado);
}, { immediate: true });

const consultarFicha = async () => {
  if (ficha.value.trim() !== '') {
    cargarAprendicesFicha(ficha.value)
  } else {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Por favor ingrese un número de ficha",
      customClass: {
        popup: 'mi-alerta'
      },
      willOpen: () => {
        document.body.style.paddingRight = '0px';
      },
      didClose: () => {
        document.body.style.paddingRight = '';
      }
    });
  }
}

const volverABusqueda = () => {
  mostrarResultados.value = false;
  busquedaRealizada.value = false;
  aprendices.value = [];
  ficha.value = '';
}

// Función para manejar la edición desde el componente tabla
const manejarEdicionAprendiz = (aprendiz: Aprendiz) => {
  console.log('Editando aprendiz desde', aprendiz.nombre)
  aprendizSeleccionado.value = aprendiz
  mostrarModal.value = true
  bloquearScroll()
}

// Función para manejar errores de carga desde el componente tabla
const manejarErrorCarga = (error: any) => {
  console.error('Error desde tabla:', error)
  Swal.fire({
    icon: "error",
    title: "Error",
    text: error,
    scrollbarPadding: false,
    heightAuto: false,
    didOpen: () => {
      document.body.style.paddingRight = '';
      document.body.style.overflow = '';
    }
  });
}

// Función para manejar cuando se cierra el modal desde el componente tabla
const manejarModalCerrado = () => {
  console.log('Modal cerrado desde tabla')
  cerrarModal()
}

const bloquearScroll = () => {
  document.body.style.overflow = 'hidden'
}

const desbloquearScroll = () => {
  document.body.style.overflow = ''
}

function actualizarAprendiz(datosEditados) {
  const index = aprendices.value.findIndex(a =>
    a.documento === aprendizSeleccionado.value?.documento
  )

  if (index !== -1) {
    aprendices.value[index] = {
      ...aprendices.value[index],
      ...datosEditados
    }

    const datosParaExportar = {
      tipo_documento: datosEditados.tipo_documento,
      documento: datosEditados.documento,
      nombre: datosEditados.nombre,
      apellido: datosEditados.apellido,
      celular: datosEditados.celular,
      correo: datosEditados.correo,
      direccion: datosEditados.direccion || '',
      discapacidad: datosEditados.discapacidad || 'No',
      tipo_discapacidad: datosEditados.tipo_discapacidad || 'N/A',
      modalidad: modalidad,
      firma: datosEditados.firma || ''
    };

    const existente = aprendicesExportar.value.findIndex(a => a.documento === datosEditados.documento)
    if (existente == -1) {
      aprendicesExportar.value.push(datosParaExportar)
    } else {
      aprendicesExportar.value[existente] = datosParaExportar
    }
  }
}

function exportarAprendices() {
  if (aprendicesExportar.value.length === 0) {
    Swal.fire({
      icon: "info",
      title: "Sin aprendices seleccionados",
      text: "Debes editar al menos un aprendiz antes de generar el formato.",
      customClass: {
        popup: 'mi-alerta'
      },
      willOpen: () => {
        document.body.style.paddingRight = '0px';
      },
      didClose: () => {
        document.body.style.paddingRight = '';
      }
    });
    return;
  }

  if (!usuarioGenerador.value.nombre || !usuarioGenerador.value.apellidos || !usuarioGenerador.value.rol) {
    Swal.fire({
      icon: "warning",
      title: "Información incompleta",
      text: "Por favor, completa la información del generador del reporte.",
      customClass: {
        popup: 'mi-alerta'
      },
      willOpen: () => {
        document.body.style.paddingRight = '0px';
      },
      didClose: () => {
        document.body.style.paddingRight = '';
      }
    });
    return;
  }

  const datosParaEnviar = {
    modalidad: 'grupal',
    ficha: ficha.value,
    aprendices: aprendicesExportar.value.map(ap => ({
      tipo_documento: ap.tipo_documento,
      documento: ap.documento,
      nombre: ap.nombre,
      apellido: ap.apellido,
      direccion: ap.direccion || '',
      correo: ap.correo,
      celular: ap.celular,
      discapacidad: ap.discapacidad.toUpperCase() || 'NO', 
      tipo_discapacidad: ap.tipo_discapacidad || 'N/A', 
      firma: ap.firma || '', 
    })),
    usuario_generator: {
      id: usuarioGenerador.value.id || 0,
      nombre: usuarioGenerador.value.nombre,
      apellidos: usuarioGenerador.value.apellidos,
      correo: usuarioGenerador.value.correo,
      rol: usuarioGenerador.value.rol.toUpperCase()
    },
    informacion_adicional: {
      nivel_formacion: informacionAdicional.value?.nivel_formacion || '',
      modalidad_formacion: informacionAdicional.value?.modalidad_formacion || '',
      trimestre: informacionAdicional.value?.trimestre || '',
      fecha_inicio_etapa_productiva: informacionAdicional.value?.fecha_inicio_etapa_productiva || '',
      jornada: informacionAdicional.value?.jornada || ''
    }
  };

  axios.post("http://127.0.0.1:8000/exportar-f165", datosParaEnviar, {
    responseType: 'blob'
  }).then(res => {
    const url = window.URL.createObjectURL(new Blob([res.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `formato_F165_ficha_${ficha.value}.xlsx`);
    document.body.appendChild(link);
    link.click();

    Swal.fire({
      icon: "success",
      title: "Éxito",
      text: "El archivo se ha generado correctamente.",
      customClass: {
        popup: 'mi-alerta'
      },
      willOpen: () => {
        document.body.style.paddingRight = '0px';
      },
      didClose: () => {
        document.body.style.paddingRight = '';
      }
    });
  }).catch(async (err) => {
    console.error("Error al exportar:", err);

    let errorMessage = "Ocurrió un error inesperado.";

    if (err.response && err.response.data instanceof Blob) {
      try {
        const errorText = await err.response.data.text();
        const errorData = JSON.parse(errorText);
        errorMessage = errorData.detail || errorMessage;
        console.error("Error parseado:", errorData);
      } catch (parseError) {
        console.error("No se pudo parsear el error del blob:", parseError);
      }
    } else if (err.response?.data?.detail) {
      errorMessage = err.response.data.detail;
    }

    Swal.fire({
      icon: "error",
      title: "Error al exportar",
      text: errorMessage,
      customClass: {
        popup: 'mi-alerta'
      },
      willOpen: () => {
        document.body.style.paddingRight = '0px';
      },
      didClose: () => {
        document.body.style.paddingRight = '';
      }
    });
  });
}

//Función para guardar la información adicional de la ficha
const manejarGuardar = async (datos: any) => {
  usuarioGenerador.value = datos.usuario
  informacionAdicional.value = datos.info
  mostrarModalFicha.value = false
  fichaEditada.value = true

  console.log('Datos listos para enviar:', datos)

  try {
    await axios.post(
      `http://127.0.0.1:8000/ficha/${ficha.value}/informacion-adicional`,
      informacionAdicional.value
    )
    console.log("Información adicional guardada en BD")
  } catch (err) {
    console.error("Error guardando información adicional:", err)
  }
}
//Función para cargar los datos adicionales de la ficha
async function cargarInformacionAdicional(numeroFicha: string) {
  try {
    const res = await axios.get(
      `http://127.0.0.1:8000/ficha/${numeroFicha}/informacion-adicional`
    )
    informacionAdicional.value = res.data
    console.log("Información adicional cargada:", res.data)
  } catch (err) {
    console.error("Error cargando información adicional:", err)
  }
}

async function abrirModalFicha(numeroFicha: string) {
  await cargarInformacionAdicional(numeroFicha)
  fichaEditada.value = false
  mostrarModalFicha.value = true
}

function cerrarModal() {
  mostrarModal.value = false
  mostrarModalFicha.value = false
  desbloquearScroll()
}


function irAInstructor() {
  router.back()
}

onMounted(() => {
  loadUserData();
});
</script>

<template>
  <Header></Header>

  <div class="floating-buttons" v-if="!mostrarResultados">
    <!-- Botón izquierdo -->
    <div class="tooltip tooltip-left btn-left">
      <button class="back-buttons" @click="irAInstructor">
        <i class="fa-solid fa-arrow-left"></i>
      </button>
      <span class="tooltip-text">Regresar</span>
    </div>

    <!-- Contenedor de botones derechos -->
    <div class="right-buttons">
      <div class="tooltip">
        <button class="back-buttons" @click="mostrarModal = true">
          <i class="fa-solid fa-circle-info"></i>
        </button>
        <span class="tooltip-text">Instrucciones</span>
      </div>

      <div class="tooltip">
        <button class="back-buttons">
          <i class="fa-solid fa-right-from-bracket"></i>
        </button>
        <span class="tooltip-text">Cerrar sesión</span>
      </div>
    </div>

    <GroupInstructions v-if="mostrarModal" @cerrar="mostrarModal = false" />
  </div>

  <Transition name="fade-slide" mode="out-in">
    <!-- Formulario de búsqueda -->
    <section v-if="!mostrarResultados" class="search-container" key="search-form">
      <div class="search-card">
        <h1 class="search-title">
          Para consultar el formato por ficha, digite el número de la ficha
        </h1>

        <form @submit.prevent="consultarFicha" class="search-form">
          <div class="input-group">
            <label for="ficha" class="input-label">No. Ficha 🖱️</label>
            <input id="ficha" v-model="ficha" class="search-input" type="text"
              placeholder="Ingresa el número de la ficha">
          </div>

          <button class="search-button" type="submit" :disabled="cargando">
            <span v-if="!cargando">Consultar Ficha</span>
            <span v-else class="loading-text">
              <i class="fa-solid fa-spinner fa-spin"></i>
              Buscando...
            </span>
          </button>
        </form>
      </div>
    </section>

    <!-- Sección de resultados -->
    <section v-else class="results-section" key="results">
      <div class="results-header">
        <h2 class="results-title">
          Resultados para la ficha: <span class="ficha-number">{{ ficha }}</span>
        </h2>
        <button @click="volverABusqueda" class="back-to-search-button">
          <i class="fa-solid fa-arrow-left"></i>
          Volver a buscar
        </button>
      </div>

      <!-- TABLA DE APRENDICES NO EDITADOS - Usando componente reutilizable -->
      <TablesAprendiz v-if="aprendicesNoEditados.length > 0" :aprendices="aprendicesNoEditados" :esIndividual="false"
        titulo="Aprendices disponibles" @editar-aprendiz="manejarEdicionAprendiz" @modal-cerrado="manejarModalCerrado"
        @error-carga="manejarErrorCarga">

      </TablesAprendiz>

      <!-- TABLA DE APRENDICES EDITADOS - Usando el mismo componente -->
      <div v-if="aprendicesEditados.length > 0" class="edited-section">
        <h3 class="section-title">
          <i class="fa-solid fa-edit"></i>
          Aprendices Editados ({{ aprendicesEditados.length }})
        </h3>

        <TablesAprendiz :aprendices="aprendicesEditados" titulo="Aprendices editados" :mostrar-solo-no-editados="false"
          :esIndividual="false" @editar-aprendiz="manejarEdicionAprendiz" @modal-cerrado="manejarModalCerrado"
          @error-carga="manejarErrorCarga" />
      </div>

      <!-- Mensaje sin resultados -->
      <Transition name="fade" appear>
        <div v-if="aprendices.length === 0 && busquedaRealizada" class="no-results">
          <div class="no-results-content">
            <i class="fa-solid fa-search no-results-icon"></i>
            <h3 class="no-results-title">No se encontraron resultados</h3>
            <p class="no-results-text">
              No se encontró ningún aprendiz para la ficha <strong>{{ ficha }}</strong>
            </p>
          </div>
        </div>
      </Transition>

      <div v-if="mostrarResultados && (aprendicesNoEditados?.length || aprendicesEditados?.length)" class="btns-ficha">
        <!-- Botón para abrir modal -->
        <button class="export-button" @click="abrirModalFicha(ficha)">
          Editar datos de ficha
        </button>

        <!-- El modal -->
        <EditFicha :visible="mostrarModalFicha" :usuarioGenerador="usuarioGenerador"
          :informacionAdicional="informacionAdicional" @cerrar="cerrarModal" @guardar="manejarGuardar" />

        <!-- Botón exportar (deshabilitado hasta editar) -->
        <button :disabled="!fichaEditada || aprendices.length === 0" @click="exportarAprendices" class="export-button">
          <i class="fa-solid fa-download"></i>
          Generar y Descargar Reporte
        </button>
      </div>

    </section>
  </Transition>

  <!-- Modal de edición independiente (mantener tu modal actual) -->
  <EditAprendizModal :aprendiz="aprendizSeleccionado" :mostrar="mostrarModal" @cerrar="cerrarModal"
    @actualizar="actualizarAprendiz" />
</template>

<style scoped>
/* Variables CSS */
:root {
  --primary-color: #10b981;
  --primary-dark: #059669;
  --secondary-color: #6366f1;
  --background-light: #f8fafc;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --border-color: #e2e8f0;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --border-radius: 8px;
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

body {
  overflow-x: hidden;
  /* Previene scroll horizontal */
}

.form-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.form-controls {
  display: flex;
  gap: 0.5rem;
}

.btn-edit,
.btn-reset {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 0.875rem;
  transition: all 0.2s ease;
}

.btn-edit {
  background-color: #3b82f6;
  color: white;
}

.btn-edit:hover {
  background-color: #2563eb;
}

.btn-reset {
  background-color: #6b7280;
  color: white;
}

.btn-reset:hover {
  background-color: #4b5563;
}

.user-info-banner {
  background-color: #dbeafe;
  border: 1px solid #3b82f6;
  border-radius: 0.5rem;
  padding: 0.75rem 1rem;
  margin-bottom: 1rem;
  color: #1e40af;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.form-input.readonly,
.form-select.readonly {
  background-color: #f9fafb;
  border-color: #d1d5db;
  color: #6b7280;
  cursor: not-allowed;
}

.form-input:read-only {
  background-color: #f9fafb;
  border-color: #d1d5db;
  color: #6b7280;
}

/* Layout principal */
.navigation-container {
  padding: 20px 50px 0;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: var(--border-radius);
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: var(--shadow-md);
}

.back-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

/* Sección de búsqueda */
.search-container {
  display: flex;
  justify-content: center;
  margin-top: 110px;
  align-items: center;
  min-height: 60vh;
  padding: 20px;
}

.search-card {
  background: white;
  padding: 60px 40px;
  border-radius: 16px;
  box-shadow: var(--shadow-lg);
  text-align: center;
  max-width: 600px;
  width: 100%;
}

.search-title {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 40px;
  line-height: 1.4;
}

.search-form {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.input-group {
  text-align: left;
}

.input-label {
  display: block;
  font-family: 'Inter', sans-serif;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.search-input {
  width: 100%;
  padding: 16px 20px;
  border: 2px solid var(--border-color);
  border-radius: var(--border-radius);
  font-size: 1rem;
  transition: var(--transition);
  box-sizing: border-box;
  font-family: inherit;
}

.search-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.search-button {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  font-size: 1.1rem;
  font-weight: 600;
  padding: 16px 32px;
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
  box-shadow: var(--shadow-md);
}

.search-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.search-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.loading-text {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

/* Sección de resultados */
.results-section {
  padding: 20px;
  max-width: 1400px;
  margin: 0 auto;
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding: 24px;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius: 12px;
  box-shadow: var(--shadow-md);
}

.results-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
  font-family: 'Inter', sans-serif;
}

.ficha-number {
  color: var(--primary-color);
  font-weight: 700;
}

.back-to-search-button {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--secondary-color);
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: var(--border-radius);
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: var(--shadow-md);
}

.back-to-search-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

/* Tabla optimizada */
.table-wrapper {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.table-container {
  overflow-x: auto;
  /* Prevenir el scroll horizontal innecesario */
  scrollbar-width: thin;
  scrollbar-color: var(--border-color) transparent;
}

.table-container::-webkit-scrollbar {
  height: 6px;
}

.table-container::-webkit-scrollbar-track {
  background: transparent;
}

.table-container::-webkit-scrollbar-thumb {
  background-color: var(--border-color);
  border-radius: 3px;
}

.modern-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  background: white;
}

/* Cabecera de la tabla */
.table-header {
  background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
}

.modern-table th {
  padding: 16px 12px;
  text-align: left;
  font-weight: 600;
  color: var(--text-primary);
  border-bottom: 2px solid var(--border-color);
  white-space: nowrap;
  position: sticky;
  top: 0;
  background: inherit;
  z-index: 10;
}

/* Celdas de la tabla */
.modern-table td {
  padding: 14px 12px;
  border-bottom: 1px solid var(--border-color);
  transition: background-color 0.2s ease;
}

/* Filas de la tabla */
.table-row {
  animation: slideInRow 0.4s ease-out both;
  transition: background-color 0.2s ease;
}

.table-row:hover {
  background-color: #f8fafc;
}

/* Columnas específicas */
.td-number {
  font-weight: 600;
  color: var(--text-secondary);
  width: 60px;
  text-align: center;
}

.document-badge {
  display: inline-block;
  padding: 4px 8px;
  background: var(--primary-color);
  color: white;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status-badge {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status-badge.activo {
  background: #dcfce7;
  color: #166534;
}

.status-badge.inactivo {
  background: #fee2e2;
  color: #991b1b;
}

.edit-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: var(--transition);
  font-size: 0.9rem;
}

.edit-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

/* Formulario del generador */
.user-generator-form {
  margin-top: 32px;
  padding: 32px;
  background: #f8fafc;
  border-radius: 12px;
  border-top: 4px solid var(--primary-color);
}

.form-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 24px;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 6px;
  font-size: 0.9rem;
}

.form-input,
.form-select {
  padding: 12px 16px;
  border: 2px solid var(--border-color);
  border-radius: var(--border-radius);
  font-size: 0.95rem;
  transition: var(--transition);
  background: white;
  font-family: inherit;
}

.form-input:focus,
.form-select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.btns-ficha {
  display: flex;
  /* botones en fila */
  gap: 16px;
  /* espacio entre botones */
  justify-content: center;
  /* centrados */
  flex-wrap: wrap;
  /* se ajustan si no caben */
}

.export-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  border: none;
  padding: 16px 2px;
  border-radius: var(--border-radius);
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: var(--shadow-md);
  flex: 1;
  /* ocupan mismo espacio */
  max-width: 250px;
  margin-top: 40px;
}

.export-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.export-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Sin resultados */
.no-results {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
  padding: 40px;
}

.no-results-content {
  text-align: center;
  background: white;
  padding: 48px;
  border-radius: 16px;
  box-shadow: var(--shadow-lg);
  max-width: 400px;
}

.no-results-icon {
  font-size: 3rem;
  color: var(--text-secondary);
  margin-bottom: 20px;
}

.no-results-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.no-results-text {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.5;
}

/* Animaciones */
@keyframes slideInRow {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Transiciones */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateX(-30px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.table-fade-enter-active {
  transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.table-fade-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Responsive Design */
@media (max-width: 1200px) {
  .right-buttons {
    margin-right: 30px;
  }

  .results-section {
    padding: 15px;
  }

  .modern-table {
    font-size: 0.85rem;
  }

  .modern-table th,
  .modern-table td {
    padding: 10px 8px;
  }
}

@media (max-width: 768px) {
  .navigation-container {
    padding: 20px 20px 0;
  }

  .search-card {
    padding: 40px 24px;
    margin: 20px;
  }

  .search-title {
    font-size: 1.25rem;
  }

  .results-header {
    flex-direction: column;
    gap: 16px;
    text-align: center;
    padding: 20px;
  }

  .search-input::placeholder {
    font-size: 0.85rem;
  }

  .results-title {
    font-size: 1.25rem;
  }

  .back-to-search-button {
    width: 100%;
    justify-content: center;
  }

  .table-container {
    border-radius: 8px;
    margin: 0 -10px;
  }

  .modern-table {
    font-size: 0.8rem;
  }

  .modern-table th,
  .modern-table td {
    padding: 8px 6px;
  }

  .user-generator-form {
    margin: 20px -10px 0;
    padding: 24px 16px;
  }

  .form-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .export-button {
    width: 100%;
    max-width: none;
  }
}

@media (max-width: 480px) {
  .search-card {
    margin: 10px;
    padding: 32px 20px;
  }

  .modern-table th,
  .modern-table td {
    padding: 6px 4px;
    font-size: 0.75rem;
  }

  /* Ocultar columnas menos importantes en móvil */
  .th-direccion,
  .td-direccion,
  .th-celular,
  .td-celular {
    display: none;
  }
}


/* Mejoras de accesibilidad */
@media (prefers-reduced-motion: reduce) {

  .table-row,
  .search-button,
  .edit-button,
  .export-button,
  .back-button {
    animation: none;
    transition: none;
  }
}

/* Focus visible para accesibilidad */
.search-input:focus-visible,
.form-input:focus-visible,
.form-select:focus-visible,
.search-button:focus-visible,
.edit-button:focus-visible,
.export-button:focus-visible,
.back-button:focus-visible {
  outline: 2px solid var(--primary-color);
  outline-offset: 2px;
}

/* Indicador de carga mejorado */
.fa-spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}
</style>
