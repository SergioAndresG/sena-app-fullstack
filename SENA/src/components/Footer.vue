<template>
  <footer class="footer-container">
    
    <!-- Contenido principal del footer -->
    <div class="footer-content">
      <!-- Sección izquierda Logo Sena -->
    <div class="logo-content">
        <img class="logo-icon" src="../assets/logo_Sena.png" alt="Logo SENA" />
    </div>
      <!-- Sección central - Texto principal -->
      <div class="main-text">
        <p class="slogan">CONOCIMIENTO Y EMPRENDIMIENTO PARA TODOS LOS COLOMBIANOS</p>
      </div>      
        <img src="../assets/logo_footer.png" alt="logo_footer" class="logo_footer">      
    </div>
  </footer>
</template>

<style scoped>
.footer-container {
  position: relative;
  padding: 30px 20px;

}
/* Contenido principal */
.footer-content {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.371);
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: center;
  flex-wrap: wrap;
  max-width: 1350px;
  margin: 0 auto;
  gap: 20px;
}
.logo-icon{
    width: 70px;
    height: 70px;
    margin-left: 2rem;
}
/* Texto principal */
.main-text {
  text-align: center;
  flex: 1;
}
.slogan {
  font-size: 1rem;
  letter-spacing: 0.5px;
  text-align: center;
  margin-top: 10px;
  color: #444;  
}
.logo_footer{
    width: 97px;
    height: 100px;
}
/* Responsividad */
@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
    gap: 20px;
  }
  .year-section::before {
    display: none;
  }
  
  .footer-container::before {
    left: 20px;
    right: 20px;
  }
  .slogan {
    font-size: 16px;
  }
}
</style>