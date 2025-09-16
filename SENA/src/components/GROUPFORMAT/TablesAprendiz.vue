<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';
import Swal from 'sweetalert2';

interface Aprendiz {
  tipo_documento: string;
  documento: string;
  nombre: string;
  apellido: string;
  celular: string;
  correo: string;
  direccion: string;
  estado: string;
  editado?: boolean;
  firma?: string;
}

interface Props {
  aprendices: Aprendiz[];
  titulo?: string;
  rowClass?: string;
  mostrarSoloNoEditados?: boolean;
}

interface Emits {
  (e: 'editarAprendiz', aprendiz: Aprendiz): void;
  (e: 'modalCerrado'): void;
  (e: 'errorCarga', mensaje: string): void;
}

const aprendizSeleccionado = ref<Aprendiz | null>(null)
const mostrarModal = ref(false)

const props = defineProps<Props>();
const emit = defineEmits<Emits>();

const cargandoDatos = ref(false)


async function abrirModal(aprendiz: Aprendiz) {
  if (aprendiz.editado) {
    try {
    cargandoDatos.value = true
    const respuesta = await axios.get(`http://127.0.0.1:8000/aprendices/${aprendiz.documento}`)
    const datosFrescos = respuesta.data.aprendiz || respuesta.data

    emit('editarAprendiz', {...datosFrescos})
    } catch (error) {
      console.error('Error al obtener datos frescos del aprendiz:', error)
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "No se pudieron cargar los datos del aprendiz. Inténtalo de nuevo.",
        willOpen: () => {
          document.body.style.paddingRight = '0px';
        },
        didClose: () => {
          document.body.style.paddingRight = '';
        }
      });
      return;
    }
  } else {
    //Emitir al componente padre
    emit('editarAprendiz', {...aprendiz})
  }
}
</script>
<template>
<!-- Tabla optimizada -->
<Transition name="table-fade">
<div v-if="aprendices.length" class="table-wrapper">
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
</div>
</Transition>
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
</style>