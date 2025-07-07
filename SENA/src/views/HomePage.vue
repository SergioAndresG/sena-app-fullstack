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
              <img class="logo-icon" src="/src/assets/logo_Sena.png" alt="">
            </div>
            <span class="logo-text">Centro de Biotecnología Agropecuaria</span>
          </div>
        </div>
        <div class="form-container">
          <h2 class="form-title">Inicio Sesión</h2>
          <p class="form-subtitle">Ingrese sus credenciales para acceder</p>
          <div class="form-fields">
            <!-- Campo Email -->
            <div class="field-group">
              <label class="field-label">Nombre de usuario</label>
              <div class="input-container">
                <input type="email" v-model="email" class="form-input" placeholder="Usuario" required />
                <div class="input-icon">
                  <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                  </svg>
                </div>
              </div>
            </div>
            <!-- Campo Contraseña -->
            <div class="field-group">
              <label class="field-label">Contraseña</label>
              <div class="input-container">
                <input :type="showPassword ? 'text' : 'password'" v-model="password" class="form-input" placeholder="••••••••" required />
                <div class="input-icon">
                  <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <button type="button" @click="togglePassword" class="password-toggle">
                  <svg v-if="showPassword" class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029M5.394 5.394L4 4m0 0l1.394 1.394M4 4l15.364 15.364M19.606 19.606L21 21m-1.394-1.394L19.606 19.606m0 0a12.002 12.002 0 01-1.563-3.029 10.05 10.05 0 01-5.043-1.877" />
                  </svg>
                  <svg v-else class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                </button>
              </div>
            </div>
            <!-- Botón de ingreso -->
            <button @click="handleLogin" :disabled="isLoading" class="login-button" :class="{ 'loading': isLoading }">
              <div v-if="isLoading" class="loading-content">
                <div class="spinner"></div>
                Ingresando...
              </div>
              <span v-else>Ingresar</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SenaLogin',
  data() {
    return {
      email: '',
      password: '',
      isLoading: false,
      showPassword: false,
      rememberMe: false
    }
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword
    },
    handleLogin() {
      if (!this.email || !this.password) {
        alert('Por favor completa todos los campos')
        return
      }

      this.isLoading = true

      // Simular proceso de login
      setTimeout(() => {
        this.isLoading = false
        alert(`Bienvenido: ${this.email}`)
        // Aquí puedes agregar la lógica de autenticación real
      }, 2000)
    }
  }
}
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
  padding: 2rem;
  flex-direction: column;
}

.logo-container {
  text-align: center;
  margin-bottom: 2rem;
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
  height: 450px;
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
  .login-container {
    padding: 0.5rem;
  }

  .right-panel {
    padding: 1.5rem;
  }

  .welcome-title {
    font-size: 2rem;
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