<template>
  <Header />
  <div class="floating-buttons">
    <!-- Botón izquierdo -->
    <div class="tooltip tooltip-left btn-left">
      <button class="back-buttons" @click="irAAdmin">
        <i class="fa-solid fa-arrow-left"></i>
      </button>
      <span class="tooltip-text">Regresar</span>
    </div>

    <!-- Contenedor de botones derechos -->
    <div class="right-buttons">

      <div class="tooltip">
        <button class="back-buttons">
          <i class="fa-solid fa-right-from-bracket"></i>
        </button>
        <span class="tooltip-text">Cerrar sesión</span>
      </div>
    </div>

  </div>

  <div class="historial-container">
    <!-- Header con filtros -->
    <div class="header-section">
      <h1 class="page-title">
        <i class="fas fa-history"></i>
        Historial de Archivos
      </h1>
      
      <!-- Filtros y búsqueda -->
      <div class="filters-section">
        <div class="search-box">
          <i class="fas fa-search"></i>
          <input 
            v-model="filtros.busqueda" 
            type="text" 
            placeholder="Buscar por nombre, ficha o modalidad..."
            class="search-input"
          />
        </div>
        
        <select v-model="filtros.ordenar" class="filter-select">
          <option value="fecha_desc">Más recientes</option>
          <option value="fecha_asc">Más antiguos</option>
          <option value="nombre">Por nombre</option>
          <option value="tamaño">Por tamaño</option>
        </select>
      </div>
    </div>

    <!-- Loading state -->
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner"></div>
      <p>Cargando historial...</p>
    </div>

    <!-- Lista de archivos -->
    <div v-else class="archivos-grid">
      <TransitionGroup name="archivo-item" tag="div" class="grid-container">
        <div 
          v-for="archivo in archivosFiltrados" 
          :key="archivo.id" 
          class="archivo-card"
          @click="verDetalles(archivo)"
        >
          <!-- Icono y tipo -->
          <div class="card-header">
            <div class="file-icon">
              <i class="fas fa-file-excel"></i>
            </div>
            <div class="file-info">
              <h3 class="file-name">{{ archivo.nombre_original }}</h3>
              <p class="file-ficha">Ficha: {{ archivo.ficha }}</p>
            </div>
            <div class="file-actions">
              <button @click.stop="descargar(archivo)" class="action-btn download">
                <i class="fas fa-download"></i>
              </button>
              <button @click.stop="verDetalles(archivo)" class="action-btn details">
                <i class="fas fa-eye"></i>
              </button>
            </div>
          </div>

          <!-- Información del archivo -->
          <div class="card-body">
            <div class="info-row">
              <span class="info-label">Modalidad:</span>
              <span class="info-value modalidad" :class="archivo.modalidad.toLowerCase()">
                {{ archivo.modalidad }}
              </span>
            </div>
            
            <div class="info-row">
              <span class="info-label">Aprendices:</span>
              <span class="info-value">{{ archivo.cantidad_aprendices }}</span>
            </div>
            
            <div class="info-row">
              <span class="info-label">Tamaño:</span>
              <span class="info-value">{{ archivo.tamaño_mb }} MB</span>
            </div>
            
            <div class="info-row">
              <span class="info-label">Generado por:</span>
              <span class="info-value">{{ archivo.generado_por }}</span>
            </div>
            
            <div class="info-row">
              <span class="info-label">Rol:</span>
              <span class="info-value rol" :class="archivo.rol_usuario.toLowerCase()">
                {{ archivo.rol_usuario }}
              </span>
            </div>
          </div>

          <!-- Footer con fecha -->
          <div class="card-footer">
            <div class="date-info">
              <i class="fas fa-calendar-alt"></i>
              <span>{{ formatearFecha(archivo.fecha_creacion) }}</span>
            </div>
            <div class="time-ago">
              {{ tiempoTranscurrido(archivo.fecha_creacion) }}
            </div>
          </div>
        </div>
      </TransitionGroup>
    </div>

    <!-- Empty state -->
    <div v-if="!loading && archivosFiltrados.length === 0" class="empty-state">
      <div class="empty-icon">
        <i class="fas fa-folder-open"></i>
      </div>
      <h3>No se encontraron archivos</h3>
      <p>No hay archivos que coincidan con los filtros seleccionados.</p>
    </div>

    <!-- Modal de detalles -->
    <Transition name="modal">
      <div v-if="showModal" class="modal-overlay" @click="cerrarModal">
        <div class="modal-content" @click.stop>
          <div class="modal-header">
            <h2>Detalles del Archivo</h2>
            <button @click="cerrarModal" class="close-btn">
              <i class="fas fa-times"></i>
            </button>
          </div>
          <div class="modal-body" v-if="archivoSeleccionado">
            <!-- Contenido detallado del archivo -->
            <div class="detail-grid">
              <div class="detail-item">
                <strong>Nombre:</strong>
                <span>{{ archivoSeleccionado.nombre_original }}</span>
              </div>
              <div class="detail-item">
                <strong>Ficha:</strong>
                <span>{{ archivoSeleccionado.ficha }}</span>
              </div>
              <div class="detail-item">
                <strong>Modalidad:</strong>
                <span class="modalidad" :class="archivoSeleccionado.modalidad.toLowerCase()">
                  {{ archivoSeleccionado.modalidad }}
                </span>
              </div>
              <div class="detail-item">
                <strong>Cantidad de Aprendices:</strong>
                <span>{{ archivoSeleccionado.cantidad_aprendices }}</span>
              </div>
              <div class="detail-item">
                <strong>Tamaño:</strong>
                <span>{{ archivoSeleccionado.tamaño_mb }} MB</span>
              </div>
              <div class="detail-item">
                <strong>Generado por:</strong>
                <span>{{ archivoSeleccionado.generado_por }}</span>
              </div>
              <div class="detail-item">
                <strong>Rol del Usuario:</strong>
                <span class="rol" :class="archivoSeleccionado.rol_usuario.toLowerCase()">
                  {{ archivoSeleccionado.rol_usuario }}
                </span>
              </div>
              <div class="detail-item">
                <strong>Fecha de Creación:</strong>
                <span>{{ formatearFechaCompleta(archivoSeleccionado.fecha_creacion) }}</span>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button @click="descargar(archivoSeleccionado)" class="btn-primary">
              <i class="fas fa-download"></i>
              Descargar
            </button>
            <button @click="cerrarModal" class="btn-secondary">
              Cerrar
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, type Ref } from 'vue'
import axios, { type AxiosResponse } from 'axios'
import { useRouter } from 'vue-router';
import Header from '../components/Header.vue'

// Interfaces
interface ArchivoExcel {
  id: number
  nombre_original: string
  ficha: string
  modalidad: 'Presencial' | 'Virtual' | 'Mixta'
  cantidad_aprendices: number
  fecha_creacion: string
  tamaño_mb: number
  generado_por: string
  rol_usuario: string
}

interface Filtros {
  busqueda: string
  modalidad: string
  ordenar: 'fecha_desc' | 'fecha_asc' | 'nombre' | 'tamaño'
}

// Reactive variables
const archivos: Ref<ArchivoExcel[]> = ref([])
const loading: Ref<boolean> = ref(true)
const showModal: Ref<boolean> = ref(false)
const archivoSeleccionado: Ref<ArchivoExcel | null> = ref(null)

const router = useRouter()

const filtros: Ref<Filtros> = ref({
  busqueda: '',
  modalidad: '',
  ordenar: 'fecha_desc'
})

// Computed para filtros
const archivosFiltrados = computed((): ArchivoExcel[] => {
  let resultado = [...archivos.value]

  // Filtro de búsqueda
  if (filtros.value.busqueda) {
    const busqueda = filtros.value.busqueda.toLowerCase()
    resultado = resultado.filter(archivo =>
      archivo.nombre_original.toLowerCase().includes(busqueda) ||
      archivo.ficha.toLowerCase().includes(busqueda) ||
      archivo.modalidad.toLowerCase().includes(busqueda) ||
      archivo.generado_por.toLowerCase().includes(busqueda)
    )
  }

  // Filtro por modalidad
  if (filtros.value.modalidad) {
    resultado = resultado.filter(archivo => 
      archivo.modalidad === filtros.value.modalidad
    )
  }

  // Ordenamiento
  switch (filtros.value.ordenar) {
    case 'fecha_desc':
      resultado.sort((a, b) => new Date(b.fecha_creacion).getTime() - new Date(a.fecha_creacion).getTime())
      break
    case 'fecha_asc':
      resultado.sort((a, b) => new Date(a.fecha_creacion).getTime() - new Date(b.fecha_creacion).getTime())
      break
    case 'nombre':
      resultado.sort((a, b) => a.nombre_original.localeCompare(b.nombre_original))
      break
    case 'tamaño':
      resultado.sort((a, b) => b.tamaño_mb - a.tamaño_mb)
      break
  }

  return resultado
})

// Métodos
const obtenerHistorial = async (): Promise<void> => {
  try {
    loading.value = true
    const response: AxiosResponse<ArchivoExcel[]> = await axios.get('http://127.0.0.1:8000/archivo/historial')
    archivos.value = response.data
  } catch (error) {
    console.error('Error al obtener historial:', error)
    // Aquí puedes agregar manejo de errores (toast, notification, etc.)
  } finally {
    loading.value = false
  }
}

const verDetalles = (archivo: ArchivoExcel): void => {
  archivoSeleccionado.value = archivo
  showModal.value = true
}

const cerrarModal = (): void => {
  showModal.value = false
  archivoSeleccionado.value = null
}

const descargar = async (): Promise<void> => {
  try {
    loading.value = true
    const response: AxiosResponse<any> = await axios.post('http://127.0.0.1:8000/exportar-f165')
    archivos.value = response.data
  } catch (error) {
    console.error('Error al obtener historial:', error)
    // Aquí puedes agregar manejo de errores (toast, notification, etc.)
  } finally {
    loading.value = false
  }
}

const formatearFecha = (fecha: string): string => {
  return new Date(fecha).toLocaleDateString('es-ES', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  })
}

const formatearFechaCompleta = (fecha: string): string => {
  return new Date(fecha).toLocaleString('es-ES', {
    day: '2-digit',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const tiempoTranscurrido = (fecha: string): string => {
  const ahora = new Date()
  const fechaArchivo = new Date(fecha)
  const diferencia = ahora.getTime() - fechaArchivo.getTime()
  
  const minutos = Math.floor(diferencia / (1000 * 60))
  const horas = Math.floor(diferencia / (1000 * 60 * 60))
  const dias = Math.floor(diferencia / (1000 * 60 * 60 * 24))
  
  if (dias > 0) return `hace ${dias} día${dias > 1 ? 's' : ''}`
  if (horas > 0) return `hace ${horas} hora${horas > 1 ? 's' : ''}`
  if (minutos > 0) return `hace ${minutos} minuto${minutos > 1 ? 's' : ''}`
  return 'hace un momento'
}

// Lifecycle
onMounted(() => {
  obtenerHistorial()
})

function irAAdmin(){
  router.push('/admin')
}
</script>

<style scoped>
/* Variables CSS */
:root {
  --primary-color: #667eea;
  --primary-hover: #5a6fd8;
  --success-color: #48bb78;
  --warning-color: #ed8936;
  --danger-color: #f56565;
  --text-primary: #2d3748;
  --text-secondary: #718096;
  --bg-primary: #ffffff;
  --bg-secondary: #f7fafc;
  --bg-card: #ffffff;
  --border-color: #e2e8f0;
  --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --radius: 25%;
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Contenedor principal */
.historial-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 1rem;
  min-height: 100vh;
  margin-top: 70px;
}

/* Header */
.header-section {
  margin-bottom: 2rem;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.page-title i {
  color: var(--primary-color);
  font-size: 2rem;
}

/* Filtros */
.filters-section {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  align-items: center;
}

.search-box {
  position: relative;
  flex: 1;
  min-width: 200px;
}

.search-box i {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-secondary);
}

.search-input {
  width: 80%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 2px solid var(--border-color);
  border-radius: var(--radius);
  font-size: 1rem;
  transition: var(--transition);
  background: var(--bg-primary);
  border-radius: 10px;
}

.search-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.filter-select {
  padding: 0.75rem 1rem;
  border: 2px solid var(--border-color);
  border-radius: var(--radius);
  background: var(--bg-primary);
  font-size: 1rem;
  cursor: pointer;
  transition: var(--transition);
  border-radius: 10px;
}

.filter-select:focus {
  outline: none;
  border-color: var(--primary-color);
}

/* Loading */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem;
}

.loading-spinner {
  width: 3rem;
  height: 3rem;
  border: 3px solid var(--border-color);
  border-top: 3px solid var(--primary-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Grid de archivos */
.archivos-grid {
  margin-top: 2rem;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 1.5rem;
}

/* Tarjetas de archivo */
.archivo-card {
  background: var(--bg-card);
  border-radius: 5%;
  box-shadow: var(--shadow);
  transition: var(--transition);
  cursor: pointer;
  overflow: hidden;
  border: 3px solid var(--border-color);
}

.archivo-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary-color);
}

.card-header {
  padding: 1.5rem;
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  border-bottom: 1px solid var(--border-color);
}

.file-icon {
  width: 3rem;
  height: 3rem;
  background: linear-gradient(135deg, #48bb78, #38a169);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.file-icon i {
  color: white;
  font-size: 1.5rem;
}

.file-info {
  flex: 1;
}

.file-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
  line-height: 1.4;
}

.file-ficha {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin: 0;
}

.file-actions {
  display: flex;
  gap: 0.5rem;
}

.action-btn {
  width: 2.5rem;
  height: 2.5rem;
  border: none;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
  opacity: 0.7;
}

.action-btn:hover {
  opacity: 1;
  transform: scale(1.1);
}

.action-btn.download {
  background: var(--success-color);
  color: white;
}

.action-btn.details {
  background: var(--primary-color);
  color: white;
}

/* Cuerpo de la tarjeta */
.card-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.info-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.info-label {
  font-weight: 500;
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.info-value {
  font-weight: 600;
  color: var(--text-primary);
}

/* Badges */
.modalidad, .rol {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.modalidad.presencial {
  background: rgba(72, 187, 120, 0.1);
  color: var(--success-color);
}

.modalidad.virtual {
  background: rgba(102, 126, 234, 0.1);
  color: var(--primary-color);
}

.modalidad.mixta {
  background: rgba(237, 137, 54, 0.1);
  color: var(--warning-color);
}

.rol.admin {
  background: rgba(245, 101, 101, 0.1);
  color: var(--danger-color);
}

.rol.usuario {
  background: rgba(102, 126, 234, 0.1);
  color: var(--primary-color);
}

/* Footer de la tarjeta */
.card-footer {
  padding: 1rem 1.5rem;
  background: var(--bg-secondary);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
}

.date-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-secondary);
}

.time-ago {
  color: var(--text-secondary);
  font-style: italic;
}

/* Empty state */
.empty-state {
  text-align: center;
  padding: 4rem;
  color: var(--text-secondary);
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
  opacity: 0.5;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.modal-content {
  background: #ffffff;
  border-radius: 2%;
  max-width: 600px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: var(--shadow-lg);
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h2 {
  margin: 0;
  color: var(--text-primary);
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: red;
  transition: var(--transition);
}

.close-btn:hover {
  color: var(--text-primary);
  transform: scale(1.1);
  transform: translateY(-2px);
}

.modal-body {
  padding: 1.5rem;
}

.detail-grid {
  display: grid;
  gap: 1rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  background: var(--bg-secondary);
  border-radius: 8px;
}

.modal-footer {
  padding: 1.5rem;
  border-top: 1px solid var(--border-color);
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

.btn-primary, .btn-secondary {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-primary {
  background: var(--primary-color);
  color: white;
}

.btn-primary:hover {
  background: #45aa6f;
  transform: translateY(-2px) scale(1.01);
}

.btn-secondary {
  background: red;
  color: white;
}
.btn-secondary:hover {
  background: rgb(211, 65, 65);
  transform: translateY(-2px) scale(1.01);
}

/* Transiciones */
.archivo-item-enter-active,
.archivo-item-leave-active {
  transition: var(--transition);
}

.archivo-item-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.archivo-item-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.modal-enter-active,
.modal-leave-active {
  transition: var(--transition);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

/* Responsive */
@media (max-width: 768px) {
  .historial-container {
    padding: 1rem;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .filters-section {
    flex-direction: column;
  }
  
  .search-box {
    min-width: 100%;
  }
  
  .grid-container {
    grid-template-columns: 1fr;
  }
  
  .card-header {
    flex-direction: column;
    gap: 1rem;
  }
  
  .file-actions {
    align-self: flex-end;
  }
}
</style>