<template>
  <div v-if="visible" class="modal-overlay" @click="cerrarClickOverlay">
    <div class="modal-content" @click.stop>
      <!-- Encabezado -->
      <div class="modal-header">
        <h2 class="modal-title">
          <i class="fa-solid fa-file-lines"></i> 
          <span>Información del Reporte</span>
        </h2>
        <button @click="cerrar" class="btn-cerrar" aria-label="Cerrar modal">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Cuerpo -->
      <div class="modal-body">
        <div class="section">
          <h3 class="form-title">
            <i class="fa-solid fa-user-gear"></i> 
            <span>Generador del reporte</span>
          </h3>

          <div class="form-grid">
            <div class="form-group">
              <label class="form-label">Nombre</label>
              <input 
                v-model="localUsuario.nombre" 
                class="form-input" 
                placeholder="Ingrese el nombre"
                required
              />
            </div>

            <div class="form-group">
              <label class="form-label">Apellidos</label>
              <input 
                v-model="localUsuario.apellidos" 
                class="form-input"
                placeholder="Ingrese los apellidos"
                required
              />
            </div>

            <div class="form-group">
              <label class="form-label">Correo</label>
              <input 
                v-model="localUsuario.correo" 
                type="email" 
                class="form-input"
                placeholder="ejemplo@correo.com"
                required
              />
            </div>

            <div class="form-group">
              <label class="form-label">Rol</label>
              <select v-model="localUsuario.rol" class="form-select" required>
                <option value="" disabled>Seleccionar rol</option>
                <option value="INSTRUCTOR">Instructor</option>
                <option value="ADMINISTRADOR">Administrador</option>
                <option value="COORDINADOR">Coordinador</option>
              </select>
            </div>
          </div>
        </div>

        <div class="section">
          <h3 class="form-title">
            <i class="fa-solid fa-layer-group"></i> 
            <span>Información adicional</span>
          </h3>

          <div class="form-grid">
            <div class="form-group">
              <label class="form-label">Nivel de formación</label>
              <select v-model="localInfo.nivel_formacion" class="form-select">
                <option value="" disabled>Seleccionar nivel</option>
                <option value="AUXILIAR">Auxiliar</option>
                <option value="OPERARIO">Operario</option>
                <option value="TECNICO">Técnico</option>
                <option value="TECNOLOGO">Tecnólogo</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label">Modalidad</label>
              <select v-model="localInfo.modalidad_formacion" class="form-select">
                <option value="" disabled>Seleccionar modalidad</option>
                <option value="PRESENCIAL">Presencial</option>
                <option value="VIRTUAL">Virtual</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label">Trimestre</label>
              <input 
                v-model="localInfo.trimestre" 
                class="form-input" 
                type="text"
                placeholder="Ej: 2024-1"
              />
            </div>

            <div class="form-group">
              <label class="form-label">Fecha inicio etapa productiva</label>
              <input 
                v-model="localInfo.fecha_inicio_etapa_productiva" 
                type="date" 
                class="form-input" 
              />
            </div>

            <div class="form-group form-group-full">
              <label class="form-label">Jornada</label>
              <select v-model="localInfo.jornada" class="form-select">
                <option value="" disabled>Seleccionar jornada</option>
                <option value="DIURNA">Diurna</option>
                <option value="NOCTURNA">Nocturna</option>
                <option value="MIXTA">Mixta</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <div class="modal-footer">
        <button class="btn btn-cancelar" @click="cerrar">
          <i class="fa-solid fa-xmark"></i>
          <span>Cancelar</span>
        </button>
        <button class="btn btn-guardar" @click="guardar">
          <i class="fa-solid fa-check"></i>
          <span>Guardar</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'

// Props
const props = defineProps<{
  visible: boolean
  usuarioGenerador: {
    id?: number
    nombre: string
    apellidos: string
    correo: string
    rol: string
  }
  informacionAdicional: {
    nivel_formacion: string
    modalidad_formacion: string
    trimestre: string
    fecha_inicio_etapa_productiva: string
    jornada: string
  }
}>()

// Emits
const emit = defineEmits(['cerrar', 'guardar'])

// Variables locales para editar sin afectar directamente props
const localUsuario = ref({ ...props.usuarioGenerador })
const localInfo = ref({ ...props.informacionAdicional })

// Si cambian props desde fuera, actualizar locales
watch(
  () => props.usuarioGenerador,
  (val) => {
    localUsuario.value = { ...val }
  },
  { deep: true }
)

watch(
  () => props.informacionAdicional,
  (val) => {
    localInfo.value = { ...val }
  },
  { deep: true }
)

// Cerrar modal
const cerrar = () => {
  emit('cerrar')
}

// Cerrar modal al hacer click en el overlay
const cerrarClickOverlay = (event: Event) => {
  if (event.target === event.currentTarget) {
    cerrar()
  }
}

// Guardar cambios
const guardar = () => {
  emit('guardar', {
    usuario: localUsuario.value,
    info: localInfo.value
  })
}
</script>

<style scoped>
/* ========== ANIMACIONES ========== */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/* ========== OVERLAY Y CONTENEDOR PRINCIPAL ========== */
.modal-overlay {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(0, 0, 0, 0.6) !important;
  backdrop-filter: blur(4px) !important;
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
  z-index: 1000 !important;
  padding: 1rem !important;
  animation: fadeIn 0.3s ease-out !important;
}

.modal-content {
  background: #ffffff !important;
  border-radius: 16px !important;
  width: 100% !important;
  max-width: 800px !important;
  max-height: 90vh !important;
  overflow: hidden !important;
  box-shadow: 
    0 20px 25px -5px rgba(0, 0, 0, 0.1),
    0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
  animation: slideIn 0.3s ease-out !important;
  display: flex !important;
  flex-direction: column !important;
}

/* ========== HEADER ========== */
.modal-header {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  padding: 1.5rem 2rem !important;
  border-bottom: 1px solid #e5e7eb !important;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%) !important;
}

.modal-title {
  display: flex !important;
  align-items: center !important;
  gap: 0.75rem !important;
  margin: 0 !important;
  font-size: 1.25rem !important;
  font-weight: 600 !important;
  color: #1f2937 !important;
}

.modal-title i {
  color: #059669 !important;
  font-size: 1.1rem !important;
}

.btn-cerrar {
  background: transparent !important;
  border: none !important;
  padding: 0.5rem !important;
  border-radius: 8px !important;
  cursor: pointer !important;
  color: #6b7280 !important;
  font-size: 1.2rem !important;
  transition: all 0.2s ease !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.btn-cerrar:hover {
  background: #f3f4f6 !important;
  color: #374151 !important;
  transform: scale(1.05) !important;
}

/* ========== BODY ========== */
.modal-body {
  flex: 1 !important;
  overflow-y: auto !important;
  padding: 0 !important;
  scrollbar-width: thin !important;
  scrollbar-color: #d1d5db #f9fafb !important;
}

.modal-body::-webkit-scrollbar {
  width: 6px !important;
}

.modal-body::-webkit-scrollbar-track {
  background: #f9fafb !important;
}

.modal-body::-webkit-scrollbar-thumb {
  background: #d1d5db !important;
  border-radius: 3px !important;
}

.modal-body::-webkit-scrollbar-thumb:hover {
  background: #9ca3af !important;
}

.section {
  padding: 1.5rem 2rem !important;
  border-bottom: 1px solid #f3f4f6 !important;
}

.section:last-child {
  border-bottom: none !important;
}

.form-title {
  display: flex !important;
  align-items: center !important;
  gap: 0.75rem !important;
  margin: 0 0 1.5rem 0 !important;
  font-size: 1.1rem !important;
  font-weight: 600 !important;
  color: #374151 !important;
}

.form-title i {
  color: #059669 !important;
  font-size: 1rem !important;
}

/* ========== GRID Y FORMULARIOS ========== */
.form-grid {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 1.5rem !important;
}

.form-group {
  display: flex !important;
  flex-direction: column !important;
  gap: 0.5rem !important;
}

.form-group-full {
  grid-column: 1 / -1 !important;
}

.form-label {
  font-weight: 500 !important;
  color: #374151 !important;
  font-size: 0.875rem !important;
  margin-bottom: 0.25rem !important;
}

.form-input,
.form-select {
  padding: 0.75rem 1rem !important;
  border: 2px solid #e5e7eb !important;
  border-radius: 8px !important;
  font-size: 0.875rem !important;
  transition: all 0.2s ease !important;
  background: #ffffff !important;
  color: #374151 !important;
}

.form-input:focus,
.form-select:focus {
  outline: none !important;
  border-color: #059669 !important;
  box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.1) !important;
  transform: translateY(-1px) !important;
}

.form-input::placeholder {
  color: #9ca3af !important;
}

.form-select {
  cursor: pointer !important;
}

.form-select option {
  padding: 0.5rem !important;
  background: white !important;
  color: #374151 !important;
}

/* ========== FOOTER ========== */
.modal-footer {
  display: flex !important;
  justify-content: flex-end !important;
  gap: 1rem !important;
  padding: 1.5rem 2rem !important;
  border-top: 1px solid #e5e7eb !important;
  background: #f9fafb !important;
}

.btn {
  display: flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  padding: 0.75rem 1.5rem !important;
  border: none !important;
  border-radius: 8px !important;
  font-weight: 500 !important;
  font-size: 0.875rem !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  text-decoration: none !important;
  min-width: 100px !important;
  justify-content: center !important;
}

.btn-cancelar {
  background: #ffffff !important;
  color: #6b7280 !important;
  border: 2px solid #e5e7eb !important;
}

.btn-cancelar:hover {
  background: #f3f4f6 !important;
  color: #374151 !important;
  border-color: #d1d5db !important;
  transform: translateY(-1px) !important;
}

.btn-guardar {
  background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
  color: #ffffff !important;
  box-shadow: 0 4px 6px -1px rgba(5, 150, 105, 0.3) !important;
}

.btn-guardar:hover {
  background: linear-gradient(135deg, #047857 0%, #065f46 100%) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 12px -2px rgba(5, 150, 105, 0.4) !important;
}

.btn:active {
  transform: translateY(0) !important;
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
  .modal-overlay {
    padding: 0.5rem !important;
  }
  
  .modal-content {
    max-height: 95vh !important;
  }
  
  .modal-header {
    padding: 1rem 1.5rem !important;
  }
  
  .modal-title {
    font-size: 1.1rem !important;
  }
  
  .section {
    padding: 1rem 1.5rem !important;
  }
  
  .form-grid {
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
  }
  
  .modal-footer {
    padding: 1rem 1.5rem !important;
    flex-direction: column-reverse !important;
  }
  
  .btn {
    width: 100% !important;
  }
}

/* ========== ANIMACIONES ========== */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/* ========== RESPONSIVE DESIGN ========== */

/* Tablets (768px y menos) */
@media (max-width: 768px) {
  .modal-overlay {
    padding: 0.5rem;
  }
  
  .modal-content {
    max-height: 95vh;
  }
  
  .modal-header {
    padding: 1rem 1.5rem;
  }
  
  .modal-title {
    font-size: 1.125rem;
  }
  
  .section {
    padding: 1rem 1.5rem;
  }
  
  .form-grid {
    gap: 1rem;
  }
  
  .modal-footer {
    padding: 1rem 1.5rem;
    gap: 0.75rem;
  }
}

/* Móviles (480px y menos) */
@media (max-width: 480px) {
  .modal-overlay {
    padding: 0.25rem;
    align-items: flex-start;
    padding-top: 2rem;
  }
  
  .modal-content {
    max-height: calc(100vh - 4rem);
    border-radius: 12px;
  }
  
  .modal-header {
    padding: 1rem;
  }
  
  .modal-title {
    font-size: 1rem;
    gap: 0.5rem;
  }
  
  .modal-title span {
    display: none;
  }
  
  .modal-title::after {
    content: "Info. Reporte";
  }
  
  .section {
    padding: 1rem;
  }
  
  .form-title {
    font-size: 1rem;
    margin-bottom: 1rem;
  }
  
  .form-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .form-group-full {
    grid-column: 1;
  }
  
  .form-input,
  .form-select {
    padding: 0.75rem;
    font-size: 16px; /* Evita zoom en iOS */
  }
  
  .modal-footer {
    padding: 1rem;
    flex-direction: column-reverse;
    gap: 0.5rem;
  }
  
  .btn {
    width: 100%;
    padding: 0.875rem;
    font-size: 0.875rem;
  }
  
  .btn span {
    display: block;
  }
}

/* Pantallas muy pequeñas (360px y menos) */
@media (max-width: 360px) {
  .modal-overlay {
    padding: 0;
  }
  
  .modal-content {
    border-radius: 0;
    max-height: 100vh;
  }
  
  .section {
    padding: 0.75rem;
  }
  
  .modal-header {
    padding: 0.75rem;
  }
  
  .modal-footer {
    padding: 0.75rem;
  }
}

/* Dark mode support (opcional) */
@media (prefers-color-scheme: dark) {
  .modal-content {
    background: #1f2937;
    color: #f9fafb;
  }
  
  .modal-header {
    background: linear-gradient(135deg, #374151 0%, #1f2937 100%);
    border-bottom-color: #374151;
  }
  
  .modal-title,
  .form-title,
  .form-label {
    color: #f9fafb;
  }
  
  .section {
    border-bottom-color: #374151;
  }
  
  .form-input,
  .form-select {
    background: #374151;
    border-color: #4b5563;
    color: #f9fafb;
  }
  
  .form-input:focus,
  .form-select:focus {
    border-color: #059669;
    background: #374151;
  }
  
  .modal-footer {
    background: #374151;
    border-top-color: #4b5563;
  }
  
  .btn-cancelar {
    background: #4b5563;
    color: #d1d5db;
    border-color: #6b7280;
  }
  
  .btn-cancelar:hover {
    background: #6b7280;
    color: #f9fafb;
  }
}
</style>