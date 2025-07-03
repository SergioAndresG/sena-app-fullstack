<template>
  <header class="main-header">
    <!-- Logo SENA -->
    <div class="logo-container">
      <div class="sena-logo">
        <div class="content-icon">
          <img class="logo-icon" src="../assets/logo_Sena.png" alt="Logo SENA" />
        </div>
        <span class="logo-text">Centro de Biotecnología Agropecuaria</span>
      </div>
    </div>
  </header>
</template>

<style scoped>
.main-header {
  width: 100%;
  height: 100px;
  border-bottom: 1px solid #e5e7eb;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.088);
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  overflow-x: hidden;
}

/* Estilo del contenedor del logo */
.logo-container {
  display: flex;
  align-items: center;
}

/* Logo + texto */
.sena-logo {
  display: flex;
  align-items: center;
  gap: 3rem;
}

/* Imagen del logo */
.logo-icon {
  width: 80px;
  height: 80px;
}

/* Texto al lado del logo */
.logo-text {
  font-size: 1.2rem;
  font-weight: 600;
  color: #16a34a;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ✅ Responsive para pantallas pequeñas */
@media (max-width: 600px) {
  .main-header {
    height: auto;
    padding: 1rem;
  }

  .logo-container {
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  .sena-logo {
    flex-direction: column;
    gap: 1rem;
  }

  .logo-text {
    font-size: 1.2rem;
  }

  .logo-icon {
    width: 80px;
    height: 80px;
  }
}
</style>
