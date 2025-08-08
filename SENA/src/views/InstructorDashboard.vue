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
  gap: 0;
  min-height: 500px;
  width: 100%;
  margin: 30px auto;
  margin-top: 120px;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.tooltip {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  position: absolute; /* o 'fixed' si deseas que no se mueva al hacer scroll */
  top: 120px;
  right: 30px;
  z-index: 100;
}

.btn-logout {
  background-color: #208b69;
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

.tooltip-text {
  visibility: hidden;
  width: 110px;
  background-color: #333;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 6px 8px;
  position: absolute;
  top: 55px;
  right: 0;
  opacity: 0;
  transition: opacity 0.3s;
}

.tooltip:hover .tooltip-text {
  visibility: visible;
  opacity: 1;
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

.icon-docs {
  height: 15rem;
  width: 15rem;
}

.divider {
  width: 1px;
  height: clamp(400px, 35vw, 600px);
  background-color: #d1d5db;
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
  width: 60%;
  height: 600px;
}

.card:hover {
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
  transform: translateY(-5px);
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
  background-color: #10b981;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
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

.btn-consultar:active {
  transform: translateY(0);
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
</style>