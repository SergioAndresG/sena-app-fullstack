<template>
  <Header></Header>
  <section class="container-docs">

    <div>
      <img class="icon-docs" src="../assets/submit.png" alt="">
    </div>

    <article class="title-docs">
        Seleccione los archivos que desea cargar
    </article>

    <button class="button-docs">
        Cargar Archivos
    </button>
  </section>
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
.container-docs {
  width: 50%;
  height: 400px;
  background-color: rgb(255, 255, 255);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin: 0 auto;
  margin-top: 80px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  flex-direction: column;
}

.icon-docs{
  height: 10rem;
  width: 10rem;
}

.title-docs {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 1.5rem;
  margin-top: 35px;
}

.button-docs {
  width: 25%;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  font-size: 1rem;
  padding: 1rem;
  border-radius: 0.5rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  animation: slideUp 0.6s ease-out;
  margin: 0 auto;
  margin-top: 30px;
}

.button-docs:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(8, 106, 73, 0.382);
}

/* ✅ Estilos responsive para pantallas menores a 768px */
@media (max-width: 1400px) {
  .container-docs {
    width: 60%;
    height: 300px;
    margin-top: 50px;
    padding: 1rem;
  }

  .icon-docs{
    height: 8rem;
    width: 8rem;
  }

  .title-docs {
    font-size: 1.5rem;
    text-align: center;
  }

  .button-docs {
    width: 30%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }
}

@media (max-width: 600px) {
  .container-docs {
    width: 50%;
    height: 280px;
    margin: 0 auto;
    margin-top: 80px;
    padding: 1rem;
  }

  .icon-docs{
    height: 5rem;
    width: 5rem;
  }

  .title-docs {
    font-size: 1.3rem;
    text-align: center;
  }

  .button-docs {
    width: 50%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }
}

@media (max-width: 600px) {
  .button-docs {
    font-size: 0.9rem;

  }
}

</style>

