<template>
  <Header />
  <!-- Botón de logout fijo -->
  <div class="right-button-dashboard">
    <div class="tooltip-dashboard">
      <button class="back-buttons">
        <i class="fa-solid fa-right-from-bracket"></i>
      </button>
      <span class="tooltip-text-dashboard">Cerrar sesión</span>
    </div>
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
  router.push('/groupformat')
}

//Redireccionar al formato individual
function irAIndividual() {
  router.push('/individualformat')
}

</script>

<style scoped>
.forms-container {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 6rem;
  max-width: 1150px;
  margin: 120px auto 0;
  padding: 2rem 0;
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
  height: clamp(8rem, 15vw, 15rem);
  width: clamp(8rem, 15vw, 15rem);
  transition: transform 0.3s ease;
  filter: drop-shadow(0 4px 8px rgba(16, 185, 129, 0.2));
}

.card:hover .icon-docs {
  transform: scale(1.05);
}

.divider {
  width: 1px;
  height: 100%;
  min-height: 300px;
  background-color: #d1d5db;
}

.card {
  background: #ffffff;
  border-radius: 20px;
  padding: 2.5rem 2rem;
  min-height: 420px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 1px solid rgba(16, 185, 129, 0.1);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  width: 100%;
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
  padding: 0.875rem 2rem;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: auto;
  min-width: 160px;
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
  box-shadow: 0 6px 18px rgba(16, 185, 129, 0.3);
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

/* Responsive */
@media (max-width: 1240px) {
  .forms-container {
    gap: 3rem;
    padding: 1.5rem;
  }

  .card {
    min-height: 380px;
    padding: 2rem;
  }
}

@media (max-width: 768px) {

  .forms-container {
    grid-template-columns: 1fr;
    gap: 2rem;
    margin-top: 120px;
  }

  .columna-divisor {
    display: none; /* Ocultamos divisor en móvil */
  }

  .card {
    width: 100%;
    min-height: auto; /* que crezca con contenido */
  }

  .btn-consultar {
    padding: 0.75rem 1.5rem;
    font-size: 0.95rem;
    min-width: 140px;
  }
}

@media (max-width: 600px){
  .right-button-dashboard{
    margin-top: 40px;
  }

  .forms-container {
    margin-top: 100px;
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