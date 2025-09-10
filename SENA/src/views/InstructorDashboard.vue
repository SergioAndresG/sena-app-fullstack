<template>
  <Header />
  <div class="tooltip">
    <button class="btn-logout">
      <i class="fa-solid fa-right-from-bracket"></i>
    </button>
    <span class="tooltip-text">Cerrar sesión</span>
  </div>

  <div class="forms-container">
    <!-- Primera columna - Formato Grupal -->
    <div class="column">
      <div class="card">
        <div class="card-content">
          <div>
            <img class="icon-docs" src="../assets/group.png" alt="">
          </div>
          <h2 class="card-titulo">
            Aquí puede generar y editar el formato F-165 grupal
          </h2>
          <button class="btn-consultar tooltip-container" @click="irAGrupal">
            Consultar
          </button>
        </div>
      </div>
    </div>

    <!-- Columna del divisor -->
    <div class="columna-divisor">
      <div class="divider"></div>
    </div>

    <!-- Segunda columna - Formato Individual -->
    <div class="column">
      <div class="card">
        <div class="card-content">
          <div>
            <img class="icon-docs" src="../assets/individual.png" alt="">
          </div>
          <h2 class="card-titulo">
            Aquí puede generar y editar el formato F-165 individual
          </h2>
          <button class="btn-consultar tooltip-container" @click="irAIndividual">
            Consultar
          </button>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import Header from '../components/Header.vue'

const router = useRouter()

//Redireccionar al formato grupal
function irAGrupal() {
  router.back()
}

//Redireccionar al formato individual
function irAIndividual() {
  router.back()
}

</script>

<style scoped>
.forms-container {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 7.5rem;
  max-width: 1150px;
  margin: 0 auto;
  margin-top: 80px;
  padding: 2rem 0;
}

.btn-logout {
  background: linear-gradient(145deg, #2dd4bf, #0d9488);
  color: white;
  font-size: 20px;
  border: none;
  padding: 14px;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  transition: transform 0.2s ease;
}

.btn-logout:hover {
  transform: scale(1.1);
}

/* Tooltips mejorados */
.tooltip {
  position: absolute;
  top: 120px;
  right: 30px; 
}

.tooltip-text {
    visibility: hidden;
    background: rgba(26, 32, 44, 0.95);
    backdrop-filter: blur(10px);
    color: #fff;
    text-align: center;
    border-radius: 8px;
    padding: 8px 12px;
    position: absolute;
    top: 65px;
    right: 50%;
    transform: translateX(50%);
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-size: 12px;
    font-weight: 500;
    white-space: nowrap;
    border: 1px solid rgba(255, 255, 255, 0.1);
    z-index: 1000;
}

.tooltip-text::before {
    content: '';
    position: absolute;
    bottom: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: transparent transparent rgba(26, 32, 44, 0.95) transparent;
}

.tooltip:hover .tooltip-text {
    visibility: visible;
    opacity: 1;
    transform: translateX(50%) translateY(-5px);
}

.tooltip-left .tooltip-text {
    top: 65px;
    right: auto;
    transform: translateX(0);
}

.tooltip-left .tooltip-text::before {
    left: 25px;
}

.tooltip-left:hover .tooltip-text {
    transform: translateY(-5px);
}

.title-id {
  text-align: center;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.column {
  display: flex;
  align-items: center;
  justify-content: center;
}

.columna-divisor {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1px;
}

.icon-container {
  position: relative;
  margin-bottom: 2rem;
}

.icon-docs {
  height: 15rem;
  width: 15rem;
  transition: transform 0.3s ease;
  filter: drop-shadow(0 4px 8px rgba(16, 185, 129, 0.2));
}

.card:hover .icon-docs {
  transform: scale(1.05);
}

.divider {
  width: 1px;
  height: clamp(400px, 35vw, 600px);
  background-color: #d1d5db;
}

.card {
  background: #ffffff;
  border-radius: 20px;
  padding: 3rem 2rem;
  height: 430px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 1px solid rgba(16, 185, 129, 0.1);
  box-shadow:
    0 4px 20px rgba(0, 0, 0, 0.08),
    0 1px 3px rgba(0, 0, 0, 0.05);
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow:
    0 20px 40px rgba(0, 0, 0, 0.12),
    0 8px 16px rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.3);
}

.card:hover::before {
  transform: scaleX(1);
}

.card-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 25px;
}

.card-titulo {
  font-size: 1.5rem;
  font-weight: 500;
  padding: 10px;
  color: #374151;
  margin: 0;
  line-height: 1.5;
}

.btn-consultar {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  font-size: 1rem;
  font-weight: 500;
  padding: 0.875rem 2.5rem;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  min-width: 180px;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
  margin-top: auto;
}

.btn-consultar::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.btn-consultar:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.4);
  background: linear-gradient(135deg, #059669 0%, #047857 100%);
}

.btn-consultar:hover::before {
  left: 100%;
}

.separator {
  font-weight: bold;
  color: #555;
  text-align: center;
}

/* Responsive design */
@media (max-width: 800px) {
  .forms-container {
    grid-template-columns: 1fr;
    grid-template-rows: auto auto auto;
    gap: 20px;
  }

  .icon-docs {
    height: 10rem;
    width: 10rem;
  }

  .columna-divisor {
    width: 100%;
    height: 1px;
    order: 2;
  }

  .divider {
    width: 200px;
    height: 1px;
  }

  .columna:first-child {
    order: 1;
  }

  .columna:last-child {
    order: 3;
  }

  .card {
    padding: 30px 20px;
  }

  .card-titulo {
    font-size: 16px;
  }

  .card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.137);
    text-align: center;
    width: clamp(350px, 30vw, 500px);
    height: clamp(350px, 30vw, 500px);
    border: 1px solid #e5e7eb;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50%;
    height: 450px;
  }

  .btn-consultar {
    background-color: #10b981;
    color: white;
    border: none;
    padding: 12px 20px;
    font-size: 15px;
    font-weight: 500;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    min-width: 120px;
  }

  .btn-consultar:hover {
    background-color: #059669;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
  }
}

@media (max-width: 768px) {
  .container-section-docs {
      grid-template-columns: 1fr;
      gap: 1.5rem;
      padding: 1rem;
  }
  
  .container-docs {
      padding: 2rem 1.5rem;
  }

  .title-docs {
      font-size: 1.4rem;
  }

  .button-docs {
      min-width: 160px;
      padding: 0.75rem 2rem;
  }
}

/* Animación de entrada */
.container-docs {
  animation: fadeInUp 0.8s ease-out;
}

.container-docs:nth-child(2) {
  animation-delay: 0.2s;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>