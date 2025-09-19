<template>
  <!-- Contenedor principal -->
  <div class="login-card">
    <div class="card-content">
      <!-- Panel izquierdo con ilustración -->
      <div class="left-panel">
        <!-- Formas decorativas de fondo -->
        <div class="background-shapes">
          <div class="shape shape-1"></div>
          <div class="shape shape-2"></div>
          <div class="shape shape-3"></div>
        </div>
        <!-- Contenido principal -->
        <div class="left-content">
          <h1 class="welcome-title">Bienvenidos</h1>
          <p class="welcome-subtitle">Sistema de Gestión de Formatos F-165</p>
          <div>
            <img class="avatar-container" src="/src/assets/team-illustration.png" alt="">
          </div>
          <!-- Ilustración de personas -->
          <div class="people-illustration">
            <div class="person person-1"><div class="person-avatar"></div></div>
            <div class="person person-2"><div class="person-avatar"></div></div>
            <div class="person person-3"><div class="person-avatar"></div></div>
          </div>
          <div class="welcome-description">
            Genere y descargue los formatos de forma fácil y segura
          </div>
        </div>
      </div>
      
      <!-- Panel derecho con formulario -->
      <div class="right-panel">
        <div class="logo-container">
          <div class="sena-logo">
            <div class="content-icon">
              <img class="logo-icon" src="/src/assets/logo_Sena.png" alt="Logo SENA">
            </div>
            <span class="logo-text">Centro de Biotecnología Agropecuaria</span>
          </div>
        </div>
        
        <div class="form-container">
          <h2 class="form-title">Inicio Sesión</h2>
          <p class="form-subtitle">Ingrese sus credenciales para acceder</p>
          
          <!-- Mostrar errores -->
          <div v-if="errorMessage" class="error-message">
            {{ errorMessage }}
          </div>
          
          
          <form @submit.prevent="handleLogin" class="form-fields">
            <!-- Campo Email -->
            <div class="field-group">
              <label class="field-label">Correo electrónico</label>
              <div class="input-container">
                <input 
                  type="email" 
                  v-model="loginForm.correo" 
                  class="form-input" 
                  :class="{ 'error': emailError }"
                  placeholder="usuario@ejemplo.com" 
                  required 
                  autocomplete="email"
                  :disabled="isLoading || isBlocked"
                  @blur="validateEmail"
                  @input="clearErrors"
                />
                <div class="input-icon">
                  <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                  </svg>
                </div>
              </div>
              <span v-if="emailError" class="field-error">{{ emailError }}</span>
            </div>
            
            <!-- Campo Contraseña -->
            <div class="field-group">
              <label class="field-label">Contraseña</label>
              <div class="input-container">
                <input 
                  :type="showPassword ? 'text' : 'password'" 
                  v-model="loginForm.contraseña" 
                  class="form-input" 
                  :class="{ 'error': passwordError }"
                  placeholder="••••••••" 
                  required 
                  autocomplete="current-password"
                  :disabled="isLoading || isBlocked"
                  @blur="validatePassword"
                  @input="clearErrors"
                  minlength="8"
                />
                <div class="input-icon">
                  <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <button 
                  type="button" 
                  @click="togglePassword" 
                  class="password-toggle"
                  :disabled="isLoading || isBlocked"
                >
                  <svg v-if="showPassword" class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029M5.394 5.394L4 4m0 0l1.394 1.394M4 4l15.364 15.364M19.606 19.606L21 21m-1.394-1.394L19.606 19.606m0 0a12.002 12.002 0 01-1.563-3.029 10.05 10.05 0 01-5.043-1.877" />
                  </svg>
                  <svg v-else class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                </button>
              </div>
              <span v-if="passwordError" class="field-error">{{ passwordError }}</span>
            </div>
            
            <!-- Indicador de fortaleza de contraseña -->
            <div v-if="loginForm.contraseña" class="password-strength">
              <div class="strength-bar">
                <div class="strength-fill" :class="passwordStrength.class" :style="{ width: passwordStrength.width }"></div>
              </div>
              <span class="strength-text">{{ passwordStrength.text }}</span>
            </div>
            
            <!-- Botón de ingreso -->
            <button 
              type="submit"
              :disabled="isLoading || isBlocked || !isFormValid" 
              class="login-button" 
              :class="{ 'loading': isLoading, 'blocked': isBlocked }"
            >
              <div v-if="isLoading" class="loading-content">
                <div class="spinner"></div>
                Ingresando...
              </div>
              <span v-else-if="isBlocked">
                Bloqueado por {{ Math.ceil(blockTimeRemaining / 60) }} min
              </span>
              <span v-else>Ingresar</span>
            </button>
            
            <!-- Información de bloqueo -->
            <div v-if="isBlocked" class="block-info">
              Demasiados intentos fallidos. Intente de nuevo en {{ Math.ceil(blockTimeRemaining / 60) }} minutos.
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2';

// Types
interface LoginForm {
  correo: string
  contraseña: string
}

interface User {
  id: number
  nombre: string
  apellidos: string
  correo: string
  rol: string
}

interface LoginResponse {
  access_token: string
  token_type: string
  user: User
}

// Router
const router = useRouter()

// Reactive state
const loginForm = ref<LoginForm>({
  correo: '',
  contraseña: ''
})

const isLoading = ref(false)
const showPassword = ref(false)
const errorMessage = ref('')
const emailError = ref('')
const passwordError = ref('')
const attemptsRemaining = ref(5)
const isBlocked = ref(false)
const blockTimeRemaining = ref(0)

let blockTimer: number | null = null

// API Configuration
const API_BASE_URL = 'http://localhost:8000'  

// Configure axios with interceptors for security
axios.defaults.timeout = 10000 // 10 second timeout
axios.interceptors.request.use((config) => {
  // Add CSRF token if available
  const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content')
  if (csrfToken) {
    config.headers['X-CSRF-Token'] = csrfToken
  }
  return config
})

// Computed properties
const isFormValid = computed(() => {
  return loginForm.value.correo && 
         loginForm.value.contraseña && 
         !emailError.value && 
         !passwordError.value &&
         loginForm.value.contraseña.length >= 8
})

const passwordStrength = computed(() => {
  const password = loginForm.value.contraseña
  let score = 0
  
  if (password.length >= 8) score += 1
  if (/[A-Z]/.test(password)) score += 1
  if (/[a-z]/.test(password)) score += 1
  if (/[0-9]/.test(password)) score += 1
  if (/[^A-Za-z0-9]/.test(password)) score += 1
  
  const levels = [
    { class: 'very-weak', width: '20%', text: 'Muy débil' },
    { class: 'weak', width: '40%', text: 'Débil' },
    { class: 'fair', width: '60%', text: 'Regular' },
    { class: 'good', width: '80%', text: 'Buena' },
    { class: 'strong', width: '100%', text: 'Muy fuerte' }
  ]
  
  return levels[Math.min(score, 4)]
})

// Methods
const sanitizeInput = (input: string): string => {
  return input.trim().replace(/[<>\"'%;()&+]/g, '')
}

const validateEmail = () => {
  const email = loginForm.value.correo.trim()
  emailError.value = ''
  
  if (!email) {
    emailError.value = 'El correo es requerido'
    return false
  }
  
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(email)) {
    emailError.value = 'Formato de correo inválido'
    return false
  }
  
  // Check for suspicious patterns
  const suspiciousPatterns = ['script', 'select', 'union', 'drop', 'insert', 'update', 'delete']
  const lowerEmail = email.toLowerCase()
  for (const pattern of suspiciousPatterns) {
    if (lowerEmail.includes(pattern)) {
      emailError.value = 'El correo contiene caracteres no válidos'
      return false
    }
  }
  
  return true
}

const validatePassword = () => {
  const password = loginForm.value.contraseña
  passwordError.value = ''
  
  if (!password) {
    passwordError.value = 'La contraseña es requerida'
    return false
  }
  
  if (password.length < 8) {
    passwordError.value = 'La contraseña debe tener al menos 8 caracteres'
    return false
  }
  
  if (!/[A-Za-z]/.test(password)) {
    passwordError.value = 'La contraseña debe contener al menos una letra'
    return false
  }
  
  if (!/\d/.test(password)) {
    passwordError.value = 'La contraseña debe contener al menos un número'
    return false
  }
  
  return true
}

const clearErrors = () => {
  errorMessage.value = ''
  emailError.value = ''
  passwordError.value = ''
}

const togglePassword = () => {
  showPassword.value = !showPassword.value
}

const startBlockTimer = (seconds: number) => {
  isBlocked.value = true
  blockTimeRemaining.value = seconds
  
  blockTimer = setInterval(() => {
    blockTimeRemaining.value--
    if (blockTimeRemaining.value <= 0) {
      isBlocked.value = false
      attemptsRemaining.value = 5
      if (blockTimer) {
        clearInterval(blockTimer)
        blockTimer = null
      }
    }
  }, 1000)
}

watch(attemptsRemaining, (newValue) => {  // 👈 Vue te da el valor aquí
  if (newValue < 5 && newValue > 0) {
    Swal.fire({
      icon: 'warning',
      title: 'Atención',
      text: `Intentos restantes: ${newValue}`
    })
  } else if (newValue === 0) {
    Swal.fire({
      icon: 'error',
      title: 'Cuenta bloqueada',
      text: 'Has agotado tus intentos.'
    })
  }
})
const handleLogin = async () => {
  // Clear previous errors
  clearErrors()
  
  // Validate form
  if (!validateEmail() || !validatePassword()) {
    return
  }
  
  if (isBlocked.value) {
    errorMessage.value = 'Cuenta temporalmente bloqueada'
    return
  }
  
  isLoading.value = true
  
  try {
    // Sanitize inputs
    const sanitizedForm = {
      correo: sanitizeInput(loginForm.value.correo).toLowerCase(),
      contraseña: loginForm.value.contraseña // Don't sanitize password as it might contain special chars
    }
    
    const response = await axios.post<LoginResponse>(
      `${API_BASE_URL}/login/`,
      sanitizedForm,
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    )
    
    const { access_token, user } = response.data
    
    // Store token securely (consider using httpOnly cookies in production)
    localStorage.setItem('access_token', access_token)
    localStorage.setItem('user', JSON.stringify(user))
    
    // Configure axios for future requests
    axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`
    
    // Reset attempts
    attemptsRemaining.value = 5
      const rol = user.rol.trim().toUpperCase()
      if (user.rol === 'ADMINISTRADOR') {
        router.push('/admin')
      } else if (user.rol === 'INSTRUCTOR') {
        router.push('/instructor')
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Acceso denegado',
          text: 'No tienes permisos para acceder a esta aplicación.',
          confirmButtonText: 'Aceptar'
        })
      }
    
  } catch (error: any) {
    console.error('Login error:', error)
    
    if (error.response?.status === 401) {
      attemptsRemaining.value--
      if (attemptsRemaining.value <= 0) {
        startBlockTimer(300) // 5 minutes
        errorMessage.value = 'Cuenta bloqueada por demasiados intentos'
      } else {
        errorMessage.value = 'Credenciales inválidas'
      }
    } else if (error.response?.status === 429) {
      startBlockTimer(300)
      errorMessage.value = 'Demasiados intentos. Cuenta temporalmente bloqueada'
    } else if (error.response?.status === 422) {
      errorMessage.value = 'Datos de entrada inválidos'
    } else if (error.code === 'ECONNABORTED') {
      errorMessage.value = 'Tiempo de conexión agotado. Intente nuevamente'
    } else {
      errorMessage.value = 'Error del servidor. Intente más tarde'
    }
  } finally {
    isLoading.value = false
  }
}

// Lifecycle
onMounted(() => {
  // Check if user is already logged in
  const token = localStorage.getItem('access_token')
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
  }
})

onUnmounted(() => {
  if (blockTimer) {
    clearInterval(blockTimer)
  }
})
</script>

<style scoped>
/* Contenedor principal */
.login-card {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  animation: fadeIn 0.8s ease-out;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
.card-content {
  display: flex;
  flex: 1;
  height: 100%;
}
.left-panel,
.right-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
/* Panel izquierdo */
.left-panel {
  background: linear-gradient(135deg, #4ade80 0%, #16a34a 100%);
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  position: relative;
  overflow: hidden;
}
.background-shapes {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.1;
}
.shape {
  position: absolute;
  background: white;
  border-radius: 50%;
}
.shape-1 {
  width: 8rem;
  height: 8rem;
  top: 5rem;
  left: 2.5rem;
  animation: float 6s ease-in-out infinite;
}
.shape-2 {
  width: 6rem;
  height: 6rem;
  bottom: 5rem;
  right: 2.5rem;
  animation: float 6s ease-in-out infinite 2s;
}
.shape-3 {
  width: 4rem;
  height: 4rem;
  top: 50%;
  left: 25%;
  animation: pulse 2s ease-in-out infinite;
}
.left-content {
  position: relative;
  z-index: 10;
  text-align: center;
}
.avatar-container {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  margin-bottom: 1.5rem;
  animation: bounceGentle 3s ease-in-out infinite;
}
.welcome-title {
  font-size: 3.5rem;
  font-weight: bold;
  animation: slideUp 0.6s ease-out;
}
.welcome-subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
  margin-bottom: 1.5rem;
  animation: slideUp 0.8s ease-out;
}
.people-illustration {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}
.person {
  width: 3rem;
  height: 3rem;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.person-1 {
  animation: slideUp 0.6s ease-out;
}
.person-2 {
  animation: slideUp 0.8s ease-out;
}
.person-3 {
  animation: slideUp 0.6s ease-out;
}
.person-avatar {
  width: 1.5rem;
  height: 1.5rem;
  background: white;
  border-radius: 50%;
}
.welcome-description {
  font-size: 1.2rem;
  opacity: 0.8;
  margin-bottom: 20px;
}
/* Panel derecho */
.right-panel {
  padding: 1.8rem;
  flex-direction: column;
}

.logo-container {
  text-align: center;
  margin-bottom: 0.5rem;
}

.sena-logo {
  display: inline-flex;
  align-items: center;
  gap: 5rem;
  color: #16a34a;
  font-weight: bold;
  font-size: 1.125rem;
}

.logo-icon {
  width: 4rem;
  height: 4rem;
  border-radius: 0.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-icon span {
  color: white;
  font-size: 0.75rem;
  font-weight: bold;
}

.logo-text {
  font-size: 1.8rem;
}

.form-container {
  max-width: 35rem;
  height: 550px;
  margin: 0 auto;
  border: 1px solid rgba(222, 220, 220, 0.345);
  border-radius: 10px;
  text-align: center;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.088);
}

.form-title {
  font-size: 2rem;
  font-weight: bold;
  color: #1f2937;
  animation: slideRight 0.6s ease-out;
}

.form-subtitle {
  color: #6b7280;
  margin-bottom: 2rem;
  font-size: 1rem;
  animation: slideRight 0.8s ease-out;
}

.form-fields {
  display: flex;
  flex-direction: column;
}

.field-group {
  position: relative;
  animation: slideRight 0.6s ease-out;
  margin: 1rem 0;
}

.field-group:nth-child(2) {
  animation: slideRight 0.8s ease-out;
}

.field-label {
  display: block;
  font-size: 1rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.5rem;
}

.input-container {
  position: relative;
}

.form-input {
  width: 100%;
  padding: 0.8rem 1rem 0.8rem 2.5rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.3s ease;
  box-sizing: border-box;
  text-indent: 1.5rem;
}

.form-input::placeholder {
  color: #aaa;
  /* No puedes posicionar con top/left, solo padding o text-indent */
  padding-left: 1rem;
  /* o */
  text-indent: 0.5rem;
}

.form-input:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.form-input:hover {
  border-color: #6ee7b7;
}

.input-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
}

.icon {
  width: 1.25rem;
  height: 1.25rem;
  color: #9ca3af;
}

.password-toggle {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  transition: color 0.3s ease;
}

.password-toggle:hover {
  color: #6b7280;
}

.form-options {
  display: flex;
  align-items: center;
  justify-content: space-between;
  animation: slideRight 0.6s ease-out;
}

.login-button {
  width: 60%;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  font-size: 0.8rem;
  padding: 1rem;
  border-radius: 0.5rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  animation: slideUp 0.6s ease-out;
  margin: 0 auto;
}

.login-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3);
}

.login-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.loading-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.spinner {
  width: 1.25rem;
  height: 1.25rem;
  border: 2px solid transparent;
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.additional-links {
  text-align: center;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
  animation: fadeIn 1s ease-out;
}

.register-text {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}

.register-link {
  color: #10b981;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.register-link:hover {
  color: #059669;
}

.error-message {
  background-color: #fee2e2;
  border: 1px solid #fecaca;
  color: #dc2626;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 16px;
  font-size: 14px;
}

.warning-message {
  background-color: #fef3c7;
  border: 1px solid #fcd34d;
  color: #d97706;
  padding: 8px 12px;
  border-radius: 6px;
  margin-bottom: 16px;
  font-size: 12px;
}

.field-error {
  color: #dc2626;
  font-size: 12px;
  margin-top: 4px;
  display: block;
}

.form-input.error {
  border-color: #dc2626;
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}

.password-strength {
  margin-top: 8px;
  margin-bottom: 16px;
}

.strength-bar {
  width: 100%;
  height: 4px;
  background-color: #e5e7eb;
  border-radius: 2px;
  overflow: hidden;
}

.strength-fill {
  height: 100%;
  transition: width 0.3s ease;
}

.strength-fill.very-weak { background-color: #ef4444; }
.strength-fill.weak { background-color: #f97316; }
.strength-fill.fair { background-color: #eab308; }
.strength-fill.good { background-color: #84cc16; }
.strength-fill.strong { background-color: #22c55e; }

.strength-text {
  font-size: 12px;
  color: #6b7280;
  margin-top: 4px;
  display: block;
}

.login-button.blocked {
  background-color: #dc2626;
  cursor: not-allowed;
}

.block-info {
  text-align: center;
  color: #dc2626;
  font-size: 12px;
  margin-top: 12px;
  padding: 8px;
  background-color: #fee2e2;
  border-radius: 6px;
}

.loading-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.spinner {
  width: 16px;
  height: 16px;
  border: 2px solid transparent;
  border-top: 2px solid currentColor;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@media (max-width: 1400px) {
  .sena-logo {
    gap: 3.5rem;
  }

  .logo-icon{
    width: 3rem;
    height: 3rem;
  }

  .logo-text{
    font-size: 1.3rem;
  }

  .form-title {
    font-size: 1.5rem;
  }

  .field-label{
    font-size: 0.9rem;
  }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* RESPONSIVE: columna en móviles */
@media (max-width: 768px) {
  .card-content {
    flex-direction: column;
    height: auto;
  }

  .left-panel,
  .right-panel {
    height: auto;
  }

  .left-panel > *,
  .right-panel > * {
    overflow: visible;
  }

  .welcome-subtitle{
    font-size: 1.1;
  }

  .welcome-description {
  font-size: 1rem;
  opacity: 0.8;
}
.logo-text {
  font-size: 1.5rem;
}
}

/* Animaciones */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideRight {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes float {

  0%,
  100% {
    transform: translateY(0px);
  }

  50% {
    transform: translateY(-20px);
  }
}

@keyframes bounceGentle {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

@keyframes pulse {

  0%,
  100% {
    opacity: 1;
  }

  50% {
    opacity: 0.5;
  }
}

/* Responsive Design */
@media (max-width: 640px) {

  .right-panel {
    padding: 1.5rem;
  }

  .welcome-title {
    font-size: 2rem;
  }

  .avatar-container{
    height: 230px;
    width: 230px;
  }

  .logo-text {
    font-size: 1rem;
  }
  .form-title {
    font-size: 1.5rem;
  }

  .form-options {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
}

</style>