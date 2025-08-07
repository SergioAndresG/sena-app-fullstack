
<script setup lang="ts">
import { ref } from 'vue';
import axios from "axios";
import Swal from 'sweetalert2';
import Header from '../components/Header.vue';
import { useRouter } from 'vue-router';
import EditAprendizModal from '../components/EditAprendizModal.vue'

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
}

interface UsuarioGenerador {
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
  nombre: '',
  apellidos: '',
  correo: '',
  rol: ''
});

const aprendices = ref<Aprendiz[]>([])
let ficha = ref<string>('');
const busquedaRealizada = ref(false);
const mostrarResultados = ref(false);
const cargando = ref(false)

// Variables para el modal de edición
const mostrarModal = ref(false)
const aprendizSeleccionado = ref<Aprendiz | null>(null)

const aprendicesExportar = ref<AprendizParaExportar[]>([]);
const modalidad = 'grupal'
const router = useRouter()

// Función para cargar aprendices
const cargarAprendicesFicha = async (codigoFicha: String) => {
  cargando.value = true;

  try {
    await new Promise(resolve => setTimeout(resolve, 800));
    const respuesta = await axios.get(`http://127.0.0.1:8000/ficha/${codigoFicha}/aprendices`);

    if(respuesta.data.archivo_existente) {
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
        // Solución para evitar el padding en el body
        willOpen: () => {
          document.body.style.paddingRight = '0px';
        },
        didClose: () => {
          document.body.style.paddingRight = '';
        }
      }).then((result) => {
        if (result.isConfirmed) {
          window.open(`http://127.0.0.1:8000/descargar-archivo?ruta=${encodeURIComponent(respuesta.data.ruta_archivo)}`, '_blank');
        } else if (result.isDenied) {
          aprendices.value = respuesta.data.aprendices;
          busquedaRealizada.value = true;
          mostrarResultados.value = true;
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

const consultarFicha = async () => {
  if (ficha.value.trim() !== '') {
    cargarAprendicesFicha(ficha.value)
  } else {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Por favor ingrese un número de ficha",
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

function abrirModal(aprendiz: Aprendiz) {
  console.log('Aprendiz seleccionado:', aprendiz)
  aprendizSeleccionado.value = { ...aprendiz }
  mostrarModal.value = true
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
    if (existente == -1 ) {
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
      discapacidad: ap.discapacidad || 'No', 
      tipo_discapacidad: ap.tipo_discapacidad || 'N/A', 
      firma: ap.firma || '', 
    })),
    usuario_generator: {
      nombre: usuarioGenerador.value.nombre,
      apellidos: usuarioGenerador.value.apellidos,
      correo: usuarioGenerador.value.correo,
      rol: usuarioGenerador.value.rol.toUpperCase() 
    }
  };

  axios.post("http://127.0.0.1:8000/exportar-f165", datosParaEnviar, {
    responseType: 'blob'
  }).then(res => {
    const url = window.URL.createObjectURL(new Blob([res.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'formato_F165.xlsx');
    document.body.appendChild(link);
    link.click();
    
    Swal.fire({
      icon: "success",
      title: "Éxito",
      text: "El archivo se ha generado correctamente.",
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
      willOpen: () => {
        document.body.style.paddingRight = '0px';
      },
      didClose: () => {
        document.body.style.paddingRight = '';
      }
    });
  });
}

function cerrarModal() {
  mostrarModal.value = false
}

function irAInstructor(){
  router.push('/instructor')
}
</script>

<template>
  <Header></Header>
  
  <!-- Botón de regreso -->
  <div v-if="!mostrarResultados" class="navigation-container">
    <button class="back-button" @click="irAInstructor">
      <i class="fa-solid fa-arrow-left"></i>
      Regresar
    </button>
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
            <input 
              id="ficha"
              v-model="ficha" 
              class="search-input" 
              type="text" 
              placeholder="Ingresa el número de la ficha"
            >
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
      
      <!-- Tabla optimizada -->
      <Transition name="table-fade">
        <div v-if="aprendices.length > 0" class="table-wrapper">
          <div class="table-container">
            <table class="modern-table">
              <thead>
                <tr class="table-header">
                  <th class="th-number">#</th>
                  <th class="th-documento">Tipo Doc.</th>
                  <th class="th-numero">Número</th>
                  <th class="th-nombre">Nombre</th>
                  <th class="th-apellidos">Apellidos</th>
                  <th class="th-celular">Celular</th>
                  <th class="th-correo">Correo</th>
                  <th class="th-estado">Estado</th>
                  <th class="th-accion">Acción</th>
                </tr>
              </thead>
              <tbody>
                <tr 
                  v-for="(item, index) in aprendices" 
                  :key="item.documento" 
                  class="table-row"
                  :style="{ 'animation-delay': `${index * 0.05}s` }"
                >
                  <td class="td-number">{{ index + 1 }}</td>
                  <td class="td-documento">
                    <span class="document-badge">{{ item.tipo_documento }}</span>
                  </td>
                  <td class="td-numero">{{ item.documento }}</td>
                  <td class="td-nombre">{{ item.nombre }}</td>
                  <td class="td-apellidos">{{ item.apellido }}</td>
                  <td class="td-celular">{{ item.celular }}</td>
                  <td class="td-correo">{{ item.correo }}</td>
                  <td class="td-estado">
                    <span 
                      class="status-badge" 
                      :class="[item.estado.toLowerCase()]"
                    >
                      {{ item.estado }}
                    </span>
                  </td>
                  <td class="td-accion">
                    <button 
                      class="edit-button" 
                      @click="abrirModal(item)"
                      :title="`Editar ${item.nombre}`"
                    >
                      <i class="fa-solid fa-edit"></i>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Formulario del generador -->
          <div class="user-generator-form">
            <h3 class="form-title">
              <i class="fa-solid fa-user-gear"></i>
              Información del generador del reporte
            </h3>
            
            <div class="form-grid">
              <div class="form-group">
                <label class="form-label">Nombre</label>
                <input 
                  v-model="usuarioGenerador.nombre" 
                  placeholder="Ingrese su nombre" 
                  class="form-input"
                >
              </div>
              
              <div class="form-group">
                <label class="form-label">Apellidos</label>
                <input 
                  v-model="usuarioGenerador.apellidos" 
                  placeholder="Ingrese sus apellidos" 
                  class="form-input"
                >
              </div>
              
              <div class="form-group">
                <label class="form-label">Correo electrónico</label>
                <input 
                  v-model="usuarioGenerador.correo" 
                  placeholder="correo@ejemplo.com" 
                  class="form-input"
                  type="email"
                >
              </div>
              
              <div class="form-group">
                <label class="form-label">Rol</label>
                <select v-model="usuarioGenerador.rol" class="form-select">
                  <option value="">Seleccionar rol</option>
                  <option value="INSTRUCTOR">Instructor</option>
                  <option value="coordinador">Coordinador</option>
                </select>
              </div>
            </div>
            
            <button @click="exportarAprendices" class="export-button">
              <i class="fa-solid fa-download"></i>
              Generar y Descargar Reporte
            </button>
          </div>
        </div>
      </Transition>

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
    </section>
  </Transition>

  <!-- Modal de edición -->
  <EditAprendizModal 
    :aprendiz="aprendizSeleccionado" 
    :mostrar="mostrarModal" 
    @cerrar="cerrarModal"
    @actualizar="actualizarAprendiz" 
  />
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
  background: linear-gradient(135deg, var(--secondary-color) 0%, #4f46e5 100%);
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
  background: #51d283;
  color: #166534;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: ease-in-out 0.2s;
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

.export-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  color: white;
  border: none;
  padding: 16px 32px;
  border-radius: var(--border-radius);
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: var(--shadow-md);
  width: 100%;
  max-width: 300px;
  margin: 0 auto;
}

.export-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

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
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  max-width: 400px;
}

.no-results-subtitle {
  color: #64748b;
  font-size: 0.9rem;
  margin-top: 8px;
}

/* Transiciones */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.fade-slide-enter-form {
  opacity: 0;
  transform: translateX(-30px);
}

.table-fade-enter-active {
  transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.table-fade-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.table-row {
  animation: slideInUp 0.6s ease-out both;
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* ✅ Estilos responsive para pantallas menores a 768px */
@media (max-width: 1400px) {
  .container-gf {
    width: 60%;
    height: 300px;
    margin-top: 50px;
    padding: 1rem;
  }

  .icon-gf {
    height: 8rem;
    width: 8rem;
  }

  .title-gf {
    font-size: 1.5rem;
    text-align: center;
  }

  .button-gf {
    width: 40%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }
}

@media (max-width: 600px) {
  .container-gf {
    width: 60%;
    height: 320px;
    margin: 0 auto;
    margin-top: 80px;
    padding: 1rem;
  }

  .icon-gf {
    height: 5rem;
    width: 5rem;
  }

  .title-gf {
    font-size: 1.3rem;
    text-align: center;
  }

  .button-gf {
    width: 50%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }

  .results-header {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }

  .results-title {
    font-size: 1.2rem;
  }

  .button-back {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 600px) {
  .button-gf {
    font-size: 0.9rem;

  }
}
</style>  