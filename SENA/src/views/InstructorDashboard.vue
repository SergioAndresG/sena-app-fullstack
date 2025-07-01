<template>
  <Header></Header>

  <div class="forms-container">
    <!-- Primera columna - Formato Grupal -->
    <div class="column">
      <div class="card">
        <div class="card-content">
          <div>
            <img class="icon-docs" src="../assets/people.png" alt="">
          </div>
          <h3 class="card-titulo">
            Aquí puede encontrar el formato F-165 grupal
          </h3>
          <button class="btn-consultar">
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
            <img class="icon-docs" src="../assets/user.png" alt="">
          </div>
          <h3 class="card-titulo">
            Aquí puede encontrar el formato F-165 individual
          </h3>
          <button class="btn-consultar">
            Consultar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '../components/Header.vue';

export default {
  components: {
    Header
  }
}
</script>


<style scoped>
.forms-container {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 0;
  min-height: 500px;
  width: 100%;
  margin: 80px auto;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.column {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.columna-divisor {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1px;
}
.icon-docs{
  height: 12rem;
  width: 12rem;
}
.divider {
  width: 1px;
  height: clamp(400px, 35vw, 600px);
  background-color: #d1d5db;
}

.card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  padding: 60px 40px;
  text-align: center;
  width: clamp(400px, 35vw, 600px);
  height: clamp(400px, 35vw, 600px);
  border: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: center;
  
}

.card-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 25px;
}

.card-titulo {
  font-size: 40px;
  font-weight: 500;
  color: #374151;
  margin: 0;
  line-height: 1.5;
}

.btn-consultar {
  background-color: #10b981;
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 25px;
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

/* Responsive design */
@media (max-width: 1038px) {
  .forms-container {
    grid-template-columns: 1fr;
    grid-template-rows: auto auto auto;
    gap: 20px;
  }

  .icon-docs{
    height: 8rem;
    width: 8rem;
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