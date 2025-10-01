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
              <label class="form-label">Fecha inicio ficha</label>
              <input 
              v-model="localInfo.fecha_inicio" 
              type="date" 
              class="form-input" 
            />
            </div>

            <div class="form-group">
              <label class="form-label">Fecha fin ficha</label>
              <input 
              v-model="localInfo.fecha_fin" 
              type="date" 
              class="form-input" 
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

            <div class="form-group">
              <label class="form-label">Trimestre</label>
              <input 
                v-model="localInfo.trimestre" 
                class="form-input" 
                type="text"
                placeholder="Ej: 1"
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
    fecha_inicio: string
    fecha_fin: string
    fecha_inicio_etapa_productiva: string
    trimestre: string
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
/* ========== OVERLAY Y CONTENEDOR PRINCIPAL ========== */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  animation: fadeIn 0.3s ease-out;
}

.modal-content {
  background: #ffffff;
  border-radius: 16px;
  width: 100%;
  max-width: 800px;
  max-height: 90vh;
  overflow: hidden;
  box-shadow: 
    0 20px 25px -5px rgba(0, 0, 0, 0.1),
    0 10px 10px -5px rgba(0, 0, 0, 0.04);
  animation: slideIn 0.3s ease-out;
  display: flex;
  flex-direction: column;
}

/* ========== HEADER ========== */
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #e5e7eb;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
}

.modal-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
}

.modal-title i {
  color: #059669;
  font-size: 1.1rem;
}

.btn-cerrar {
  background: transparent;
  border: none;
  padding: 0.5rem;
  border-radius: 8px;
  cursor: pointer;
  color: #6b7280;
  font-size: 1.2rem;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-cerrar:hover {
  background: #f3f4f6;
  color: #374151;
  transform: scale(1.05);
}

/* ========== BODY ========== */
.modal-body {
  flex: 1;
  overflow-y: auto;
  padding: 0;
  scrollbar-width: thin;
  scrollbar-color: #d1d5db #f9fafb;
}

.modal-body::-webkit-scrollbar {
  width: 6px;
}

.modal-body::-webkit-scrollbar-track {
  background: #f9fafb;
}

.modal-body::-webkit-scrollbar-thumb {
  background: #d1d5db;
  border-radius: 3px;
}

.modal-body::-webkit-scrollbar-thumb:hover {
  background: #9ca3af;
}

.section {
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #f3f4f6;
}

.section:last-child {
  border-bottom: none;
}

.form-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin: 0 0 1.5rem 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #374151;
}

.form-title i {
  color: #059669;
  font-size: 1rem;
}

/* ========== GRID Y FORMULARIOS ========== */
.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group-full {
  grid-column: 1 / -1;
}

.form-label {
  font-weight: 500;
  color: #374151;
  font-size: 0.875rem;
  margin-bottom: 0.25rem;
}

.form-input,
.form-select {
  padding: 0.75rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 0.875rem;
  transition: all 0.2s ease;
  background: #ffffff;
  color: #374151;
}

.form-input:focus,
.form-select:focus {
  outline: none;
  border-color: #059669;
  box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.1);
  transform: translateY(-1px);
}

.form-input::placeholder {
  color: #9ca3af;
}

.form-select {
  cursor: pointer;
}

.form-select option {
  padding: 0.5rem;
}

/* ========== FOOTER ========== */
.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  padding: 1.5rem 2rem;
  border-top: 1px solid #e5e7eb;
  background: #f9fafb;
}

.btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  min-width: 100px;
  justify-content: center;
}

.btn-cancelar {
  background: #ffffff;
  color: #6b7280;
  border: 2px solid #e5e7eb;
}

.btn-cancelar:hover {
  background: #f3f4f6;
  color: #374151;
  border-color: #d1d5db;
  transform: translateY(-1px);
}

.btn-guardar {
  background: linear-gradient(135deg, #059669 0%, #047857 100%);
  color: #ffffff;
  box-shadow: 0 4px 6px -1px rgba(5, 150, 105, 0.3);
}

.btn-guardar:hover {
  background: linear-gradient(135deg, #047857 0%, #065f46 100%);
  transform: translateY(-2px);
  box-shadow: 0 8px 12px -2px rgba(5, 150, 105, 0.4);
}

.btn:active {
  transform: translateY(0);
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