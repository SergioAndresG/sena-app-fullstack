<!-- InstructorModal.vue -->
<template>
  <Teleport to="body">
    <Transition name="modal" appear>
      <div v-if="modelValue" class="modal-overlay" @click="closeModal">
        <div class="modal-container" @click.stop>
          <!-- Header del modal -->
          <div class="modal-header">
            <h2 class="modal-title">
              <svg class="title-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
              </svg>
              {{ selectedUser ? 'Actualizar Instructor' : 'Agregar Instructor' }}
            </h2>
            <button @click="closeModal" class="close-button" :disabled="isLoading">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <!-- Contenido del modal -->
          <div class="modal-content">
            <form @submit.prevent="guardarInstructor" class="form-content">
              <div class="form-grid">
                <!-- Campo Nombre -->
                <div class="input-group">
                  <label class="input-label" for="nombre">
                    Nombre *
                    <svg class="label-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                    </svg>
                  </label>
                  <input 
                    id="nombre"
                    v-model="instructor.nombre" 
                    type="text" 
                    class="form-input"
                    placeholder="Ingrese el nombre"
                    :disabled="isLoading"
                  >
                </div>

                <!-- Campo Apellidos -->
                <div class="input-group">
                  <label class="input-label" for="apellidos">
                    Apellidos *
                    <svg class="label-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                    </svg>
                  </label>
                  <input 
                    id="apellidos"
                    v-model="instructor.apellidos" 
                    type="text" 
                    class="form-input"
                    placeholder="Ingrese los apellidos"
                    :disabled="isLoading"
                  >
                </div>
              </div>

              <!-- Campo Correo -->
              <div class="input-group">
                <label class="input-label" for="correo">
                  Correo electrónico *
                  <svg class="label-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                  </svg>
                </label>
                <input 
                  id="correo"
                  type="email" 
                  v-model="instructor.correo" 
                  class="form-input"
                  placeholder="ejemplo@correo.com"
                  :disabled="isLoading"
                >
              </div>

              <!-- Campo Rol -->
              <div class="input-group">
                <label class="input-label" for="rol">
                  Rol del usuario *
                  <svg class="label-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
                  </svg>
                </label>
                <div class="select-wrapper">
                  <select 
                    id="rol"
                    v-model="instructor.rol" 
                    class="form-select"
                    :disabled="isLoading"
                  >
                    <option value="INSTRUCTOR">Instructor</option>
                    <option value="ADMINISTRADOR">Administrador</option>
                  </select>
                  <svg class="select-arrow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                  </svg>
                </div>
              </div>

              <!-- Botones -->
              <div class="button-group">
                <button 
                  type="button"
                  @click="closeModal"
                  class="cancel-button"
                  :disabled="isLoading"
                >
                  Cancelar
                </button>
                <button 
                  type="submit" 
                  class="submit-button"
                  :disabled="isLoading"
                  :class="{ 'loading': isLoading }"
                >
                  <div v-if="isLoading" class="loading-spinner"></div>
                  <svg v-else class="button-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                  </svg>
                  {{ isLoading ? 'Guardando...' : (selectedUser ? 'Actualizar Instructor' : 'Agregar Instructor') }}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import axios from 'axios';
import Swal from 'sweetalert2';

interface Instructor {
  id?: number;
  nombre: string;
  apellidos: string;
  correo: string;
  rol: string;
  contraseña?: string;
}

// Props
interface Props {
  modelValue: boolean;
  selectedUser: Instructor | null;
}

const props = defineProps<Props>();

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: boolean];
  'instructor-added': [instructor: Instructor];
  'instructor-updated': [instructor: Instructor];
}>();

// Estado del componente
const instructor = ref<Instructor>({
  nombre: '',
  apellidos: '',
  correo: '',
  rol: 'INSTRUCTOR',
  contraseña: '',
});

const isLoading = ref(false);

const resetForm = () => {
  instructor.value = {
    nombre: '',
    apellidos: '',
    correo: '',
    rol: 'INSTRUCTOR',
  };
};

// Inicializar formulario con datos del usuario seleccionado
watch(() => props.selectedUser, (newUser) => {
  if (newUser) {
    instructor.value = {
      id: newUser.id,
      nombre: newUser.nombre,
      apellidos: newUser.apellidos,
      correo: newUser.correo,
      rol: newUser.rol,
    };
  } else {
    resetForm();
  }
}, { immediate: true });

// Métodos
const closeModal = () => {
  if (!isLoading.value) {
    emit('update:modelValue', false);
  }
};



const guardarInstructor = async () => {
  try {
    if (!instructor.value.nombre || !instructor.value.apellidos || !instructor.value.correo || !instructor.value.rol) {
      Swal.fire({
        icon: 'error',
        title: 'Campos requeridos',
        text: 'Por favor, completa todos los campos marcados con *',
        confirmButtonColor: '#3b82f6',
      });
      return;
    }

    isLoading.value = true;
    let respuesta;
    if (props.selectedUser && instructor.value.id) {
      // Actualizar usuario existente
      respuesta = await axios.put(`http://127.0.0.1:8000/usuarios/${instructor.value.id}/`, instructor.value);
      Swal.fire({
        icon: 'success',
        title: '¡Éxito!',
        text: 'Instructor actualizado correctamente',
        confirmButtonText: 'Aceptar',
        confirmButtonColor: '#10b981',
      });
      emit('instructor-updated', { ...instructor.value });
    } else {
      // Crear nuevo usuario
      respuesta = await axios.post('http://127.0.0.1:8000/usuarios/', instructor.value);
      Swal.fire({
        icon: 'success',
        title: '¡Éxito!',
        html: `
          <div class="password-content">
            <p>El usuario ha sido creado con las siguientes credenciales:</p>
            <p><strong>Correo:</strong> ${respuesta.data.correo}</p>
            <p><strong>Contraseña:</strong> ${respuesta.data.contraseña}</p>
            <p class="text-warning">Por favor, guarde esta información de manera segura.</p>
          </div>
        `,
        showCancelButton: true,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Descargar Credenciales',
        confirmButtonColor: '#10b981',
        cancelButtonColor: '#10b981',
        reverseButtons: true,
      }).then((result) => {
        if (result.isDismissed) {
          // Aquí se descarga si presiona "Descargar Credenciales"
          downloadCredentials(respuesta.data.correo, respuesta.data.contraseña || '');
        }
      });
      emit('instructor-added', { ...instructor.value, id: respuesta.data.id });
    }
    // Limpiar formulario y cerrar modal
    resetForm();
    closeModal();

  } catch (error: any) {
    Swal.fire({
      icon: 'error',
      title: 'Error al guardar',
      text: error.response?.data?.message || 'Ocurrió un error al procesar la solicitud',
      confirmButtonColor: '#ef4444',
    });
    console.error(error);
  } finally {
    isLoading.value = false;
  }
};

const downloadCredentials = (email: string, password: string) => {
  const content = `Credenciales de acceso:\nUsuario: ${email}\nContraseña: ${password}`;
  const blob = new Blob([content], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `credenciales-${email}.txt`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
};

// Cerrar modal con Escape
const handleKeydown = (e: KeyboardEvent) => {
  if (e.key === 'Escape' && props.modelValue) {
    closeModal();
  }
};

// Agregar listener para Escape cuando el modal esté abierto
watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    document.addEventListener('keydown', handleKeydown);
  } else {
    document.removeEventListener('keydown', handleKeydown);
  }
});
</script>

<style scoped>
/* Modal Overlay */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.modal-container {
  background: white;
  border-radius: 1.5rem;
  width: 100%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.4);
}

/* Modal Header */
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #e5e7eb;
    background: linear-gradient(145deg, #1b7a6e, #0d9488);

  border-radius: 1.5rem 1.5rem 0 0;
}

.modal-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
  margin: 0;
}

.title-icon {
  width: 1.5rem;
  height: 1.5rem;
}

.close-button {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 0.5rem;
  padding: 0.5rem;
  cursor: pointer;
  color: white;
  transition: all 0.2s ease-in-out;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-button:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.05);
}

.close-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.close-button svg {
  width: 1.25rem;
  height: 1.25rem;
}

/* Modal Content */
.modal-content {
  padding: 2rem;
}

.form-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

@media (max-width: 640px) {
  .form-grid {
    grid-template-columns: 1fr;
  }
  
  .modal-header {
    padding: 1rem 1.5rem;
  }
  
  .modal-content {
    padding: 1.5rem;
  }
  
  .modal-title {
    font-size: 1.25rem;
  }
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.input-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #374151;
  font-size: 0.95rem;
}

.label-icon {
  width: 1.25rem;
  height: 1.25rem;
  color: #6b7280;
}

.form-input, .form-select {
  width: 100%;
  padding: 0.875rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 0.75rem;
  font-size: 1rem;
  transition: all 0.2s ease-in-out;
  background: #ffffff;
  box-sizing: border-box;
}

.form-input:focus, .form-select:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.form-input:hover, .form-select:hover {
  border-color: #9ca3af;
}

.form-input::placeholder {
  color: #9ca3af;
}

.form-input:disabled, .form-select:disabled {
  background-color: #f9fafb;
  color: #6b7280;
  cursor: not-allowed;
}

.select-wrapper {
  position: relative;
}

.form-select {
  appearance: none;
  padding-right: 2.5rem;
  cursor: pointer;
}

.select-arrow {
  position: absolute;
  right: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  width: 1.25rem;
  height: 1.25rem;
  color: #6b7280;
  pointer-events: none;
}

/* Botones */
.button-group {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 1rem;
}

@media (max-width: 480px) {
  .button-group {
    flex-direction: column-reverse;
  }
}

.cancel-button {
  padding: 0.875rem 1.5rem;
  border: 2px solid #e5e7eb;
  border-radius: 0.75rem;
  background: white;
  color: #6b7280;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.cancel-button:hover:not(:disabled) {
  border-color: #9ca3af;
  color: #374151;
  transform: translateY(-1px);
}

.cancel-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.submit-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: linear-gradient(145deg, #116055, #1aa59a);
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  box-shadow: 0 4px 14px 0 rgba(59, 130, 246, 0.3);
  min-width: 160px;
}

.submit-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px 0 rgba(59, 130, 246, 0.4);
}

.submit-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.submit-button.loading {
  background: linear-gradient(135deg, #6b7280 0%, #4b5563 100%);
}

.button-icon {
  width: 1.25rem;
  height: 1.25rem;
}

.loading-spinner {
  width: 1.25rem;
  height: 1.25rem;
  border: 2px solid transparent;
  border-top: 2px solid currentColor;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Transiciones del modal */
.modal-enter-active, .modal-leave-active {
  transition: all 0.3s ease;
}

.modal-enter-from, .modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  transform: scale(0.9) translateY(-2rem);
}

/* Estados de validación */
.form-input:invalid:not(:placeholder-shown) {
  border-color: #ef4444;
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
}

.form-input:valid:not(:placeholder-shown) {
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

/* Estilos personalizados para el modal de contraseña */
:global(.password-modal) {
  width: 90% !important;
  max-width: 600px !important;
  font-family: system-ui, -apple-system, sans-serif !important;
}

:global(.password-content) {
  text-align: left;
  padding: 1rem;
}

:global(.password-content p) {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}

:global(.password-content .text-warning) {
  color: #f59e0b;
  font-style: italic;
  margin-top: 1rem;
}

:global(.password-content strong) {
  color: #374151;
  font-weight: 600;
}
</style>