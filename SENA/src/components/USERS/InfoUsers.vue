<template>
  <Teleport to="body">
    <!-- Cambiado: usar v-show en lugar de v-if para evitar destroy/recreate -->
    <Transition name="modal" appear>
      <div v-show="modelValue" class="modal-overlay" @click="closeModal">
        <div class="modal-container delete-modal" @click.stop>
          <!-- Header del modal -->
          <div class="modal-header">
            <h2 class="modal-title">
              <svg class="title-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z">
                </path>
              </svg>
              Cambiar contraseña del usuario
            </h2>
            <button @click="closeModal" class="close-button" :disabled="isLoading">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <!-- Contenido del modal -->
          <div class="modal-content">
            <div class="warning-section">
              <div class="warning-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M12 9v3.75m0 0v.008h.008V12.75H12zm0 2.25h.008v.008H12v-.008zM21 12a9 9 0 11-18 0 9 9 0 0118 0z">
                  </path>
                </svg>
              </div>

              <div class="warning-content">
                <h3>Antes de continuar</h3>
                <p v-if="selectedUser">
                  Cambiara la contraseña a <strong>{{ selectedUser.nombre }} {{ selectedUser.apellidos }}</strong>
                  <br>
                </p>
                <p v-else>Se consultara el usuario seleccionado.</p>
              </div>
            </div>

            <!-- Sección de confirmación con contraseña (opcional) -->
            <div v-if="requirePassword" class="password-section">
              <div class="input-group">
                <label class="input-label" for="admin-password">
                  Confirma tu contraseña de administrador *
                  <svg class="label-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-3a1 1 0 011-1l2.879-2.879A6 6 0 0112 5zm5 2a2 2 0 11-4 0 2 2 0 014 0z">
                    </path>
                  </svg>
                </label>
                <input id="admin-password" v-model="contraseña_admin" type="password" class="form-input"
                  placeholder="Ingresa tu contraseña" :disabled="isLoading" autocomplete="current-password">
              </div>
            </div>

            <!-- Botones de acción -->
            <div class="button-group">
              <button type="button" @click="closeModal" class="cancel-button" :disabled="isLoading">
                <svg class="button-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
                Cancelar
              </button>

              <button type="button" @click="cambiarContraseñaInstructor" class="delete-button"
                :disabled="isLoading || (requirePassword && !contraseña_admin)" :class="{ 'loading': isLoading }">
                <div v-if="isLoading" class="loading-spinner"></div>

                    <i class="fa-solid fa-search"></i>

                {{ isLoading ? 'Consultando...' : 'Cambiar contraseña' }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue';
import axios from 'axios';
import Swal from 'sweetalert2';

interface User {
  id: number;
  nombre: string;
  apellidos: string;
  correo: string;
  rol: string;
}

// Props
interface Props {
  modelValue: boolean;
  userId?: number | null;
  selectedUser?: User | null;
  requirePassword?: boolean; // Para requerir contraseña de admin
}

const props = withDefaults(defineProps<Props>(), {
  userId: null,
  selectedUser: null,
  requirePassword: false
});

// Emits
const emit = defineEmits<{
  'update:modelValue': [value: boolean];
  'instructor-request': [userId: number];
  'user-request': [user: User];
}>();

// Estado del componente
const isLoading = ref(false);
const contraseña_admin = ref('');

// Computed
const canDelete = computed(() => {
  if (props.requirePassword) {
    return contraseña_admin.value.length > 0;
  }
  return true;
});

// Métodos
const closeModal = () => {
  emit('update:modelValue', false);
};

const cambiarContraseñaInstructor = async () => {
  if (!props.userId) {
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: 'No se ha seleccionado un usuario para eliminar.',
      confirmButtonColor: '#ef4444'
    });
    return;
  }

  try {
    isLoading.value = true;

    // Si requiere contraseña, validarla primero
    if (props.requirePassword && contraseña_admin.value) {
      // Aquí podrías validar la contraseña del admin
      // await axios.post('/api/validate-admin-password', { password: adminPassword.value });
    }

    const respuesta = await axios.patch(`http://127.0.0.1:8000/usuarios/${props.userId}`, {
      headers: {
        'Authorization': `Bearer ${contraseña_admin.value}`
      }
    });

    // Obtener los datos del usuario de la respuesta
    const userData = respuesta.data;

    // Crear HTML con la información detallada del usuario
    const userInfoHTML = `
      <div style="text-align: left; margin-top: 20px;">
        <h4 style="color: #10b981; margin-bottom: 15px;">Información del Usuario:</h4>
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #10b981;">
          <p style="margin: 8px 0;"><strong>Nombre:</strong> ${userData.nombre || props.selectedUser?.nombre || 'N/A'}</p>
          <p style="margin: 8px 0;"><strong>Apellidos:</strong> ${userData.apellidos || props.selectedUser?.apellidos || 'N/A'}</p>
          <p style="margin: 8px 0;"><strong>Correo:</strong> ${userData.correo || props.selectedUser?.correo || 'N/A'}</p>
          <p style="margin: 8px 0;"><strong>Rol:</strong> <span style="background-color: #e1f5fe; color: #0277bd; padding: 2px 8px; border-radius: 12px; font-size: 18px;">${userData.rol || props.selectedUser?.rol || 'N/A'}</span></p>
          <p style="margin: 8px 0;"><strong>Contraseña:</strong> <span style="background-color: #e1f5fe; color: #00000; padding: 2px 8px; border-radius: 12px; font-size: 20px; font-weight: bold;">${userData.contraseña || 'N/A'}</span></p>
          <p"</p>
        </div>
      </div>
    `;

    // Mostrar SweetAlert con información detallada
    await Swal.fire({
      icon: 'success',
      title: '¡Usuario Actualizado Exitosamente!',
      html: userInfoHTML,
      confirmButtonColor: '#10b981',
      confirmButtonText: 'Cerrar',
      cancelButtonText: 'Descargar Credenciales',
      cancelButtonColor: '#3b82f6',
      width: '500px',
      showCancelButton: true,
      focusConfirm: false
    }).then((result) => {
      if (result.isDismissed) {
        downloadCredentials(userData.correo, userData.contraseña);
      }
    });
      // Emitir eventos
    emit('instructor-request', props.userId);
    if (props.selectedUser) {
      emit('user-request', props.selectedUser);
    }

    // Cerrar modal
    closeModal();

  } catch (error: any) {
    console.error('Error al consultar el instructor:', error);

    let errorMessage = 'Hubo un problema al consultar el usuario.';
    let errorDetails = '';

    if (error.response?.status === 403) {
      errorMessage = 'No tienes permisos para consultar este usuario.';
      errorDetails = 'Verifica que tengas los permisos necesarios o contacta al administrador.';
    } else if (error.response?.status === 404) {
      errorMessage = 'El usuario no fue encontrado.';
      errorDetails = `No se encontró un usuario con ID: ${props.userId}`;
    } else if (error.response?.data?.message) {
      errorMessage = error.response.data.message;
      errorDetails = error.response.data.details || '';
    }

    // SweetAlert de error con más información
    Swal.fire({
      icon: 'error',
      title: 'Error al consultar el usuario',
      html: `
        <div style="text-align: left;">
          <p style="margin-bottom: 10px;"><strong>Error:</strong> ${errorMessage}</p>
          ${errorDetails ? `<p style="color: #6b7280; font-size: 14px;"><strong>Detalles:</strong> ${errorDetails}</p>` : ''}
          ${props.selectedUser ? `
            <div style="margin-top: 15px; padding: 10px; background-color: #fef2f2; border-radius: 6px; border-left: 3px solid #ef4444;">
              <p style="margin: 0; font-size: 14px;"><strong>Usuario seleccionado:</strong> ${props.selectedUser.nombre} ${props.selectedUser.apellidos}</p>
            </div>
          ` : ''}
        </div>
      `,
      confirmButtonColor: '#ef4444',
      confirmButtonText: 'Cerrar',
      width: '450px'
    });
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



// Limpiar formulario cuando se abra el modal
watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    contraseña_admin.value = '';
  }
});

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
/* Modal Overlay - OPTIMIZADO */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* CAMBIADO: backdrop-filter removido por performance */
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  /* AÑADIDO: will-change para optimizar animaciones */
  will-change: opacity;
}

.modal-container {
  background: white;
  border-radius: 1.5rem;
  width: 100%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
  /* OPTIMIZADO: box-shadow simplificado */
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  /* AÑADIDO: will-change para animaciones */
  will-change: transform, opacity;
  /* AÑADIDO: transform3d para activar aceleración de hardware */
  transform: translate3d(0, 0, 0);
  margin: 1rem;
}

.delete-modal {
  border: 2px solid #fecaca;
}

/* Modal Header - OPTIMIZADO */
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 2rem;
  border-bottom: 1px solid #fecaca;
  /* OPTIMIZADO: gradiente simplificado */
  background: #7e7e7e;
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
  /* OPTIMIZADO: transición más simple */
  transition: background-color 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-button:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.3);
  /* REMOVIDO: transform scale por performance */
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
  text-align: center;
}

/* Warning Section */
.warning-section {
  display: flex;
  margin-bottom: 3rem;
  padding: 0.8rem;
  background: #fef3c7;
  border: 1px solid #f59e0b;
  border-radius: 0.75rem;
  
}

.warning-icon {
  flex-shrink: 0;
}

.warning-icon svg {
  width: 2rem;
  height: 2rem;
  color: #d97706;
}

.warning-content h3 {
  margin: 0 0 0.75rem 0;
  font-size: 1.125rem;
  font-weight: 600;
  color: #92400e;
}

.warning-content p {
  margin: 0;
  color: #92400e;
  line-height: 1.5;
}

.user-email {
  font-style: italic;
  color: #a16207;
  font-size: 0.95rem;
}

/* Password Section */
.password-section {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: #f8fafc;
  border: 2px dashed #cbd5e1;
  border-radius: 0.75rem;
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

.form-input {
  width: 100%;
  padding: 0.875rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 0.75rem;
  font-size: 1rem;
  /* OPTIMIZADO: transición más simple */
  transition: border-color 0.2s ease;
  background: #ffffff;
  box-sizing: border-box;
}

.form-input:focus {
  outline: none;
  border-color: #3b82f6;
  /* SIMPLIFICADO: box-shadow removido por performance */
}

.form-input:disabled {
  background-color: #f9fafb;
  color: #6b7280;
  cursor: not-allowed;
}

/* Botones - OPTIMIZADOS */
.button-group {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.cancel-button {
  display: flex;
  align-items: center;
  text-align: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  border: 2px solid #e5e7eb;
  border-radius: 0.75rem;
  background: white;
  color: #6b7280;
  font-weight: 600;
  cursor: pointer;
  /* OPTIMIZADO: transición simple */
  transition: all 0.15s ease;
}

.cancel-button:hover:not(:disabled) {
  border-color: #9ca3af;
  color: #374151;
  /* REMOVIDO: transform por performance */
}

.delete-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  /* OPTIMIZADO: background sólido en lugar de gradiente */
  background: #9ca3af;
  color: white;
  border: none;
  padding: 0.875rem 1.5rem;
  border-radius: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.15s ease;
  min-width: 160px;
}

.delete-button:hover:not(:disabled) {
  background: #7e7e7e;
}

.delete-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.delete-button.loading {
  background: #6b7280;
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
  /* AÑADIDO: will-change para optimizar animación */
  will-change: transform;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Transiciones del modal - OPTIMIZADAS */
.modal-enter-active {
  transition: opacity 0.25s ease-out;
}

.modal-leave-active {
  transition: opacity 0.2s ease-in;
}

.modal-enter-active .modal-container {
  transition: transform 0.25s ease-out;
}

.modal-leave-active .modal-container {
  transition: transform 0.2s ease-in;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container {
  transform: translate3d(0, -1rem, 0) scale(0.95);
}

.modal-leave-to .modal-container {
  transform: translate3d(0, -0.5rem, 0) scale(0.98);
}

/* AÑADIDO: Optimización para scroll suave */
.modal-container {
  scroll-behavior: smooth;
}

/* AÑADIDO: Mejora para dispositivos táctiles */
@media (hover: none) {

  .cancel-button:hover,
  .delete-button:hover,
  .close-button:hover {
    transform: none;
  }
}

@media (max-width: 480px) {

  .modal-container {
    width: 95%;   /* casi toda la pantalla */
    height: auto;
    max-height: 85vh;
  }
  .modal-title{
    font-size: 16px;
  }
  
  .label-icon {
    width: 3rem;
    height: 3rem;
    color: #6b7280;
  }

  .button-group {
    gap: 0.5rem;
    text-align: center;
    flex-direction: column;
  }

  .button-group button {
    flex: 1;
    font-size: 12px;
  }

  .form-input::placeholder {
    font-size: 0.75rem; /* más pequeño en móviles */
  }

  .cancel-button{
    text-align: center;
  }

  .warning-section h3{
    font-size: 15px;
  }

  .warning-section {
    flex-direction: column;
    text-align: center;
    font-size: 14px;
    width: 90%;
  }
}
</style>