<template>
  <Header></Header>
  <section class="container-gf">
    <!-- <div>
      <img class="icon-docs" src="../assets/submit.png" alt="">
    </div> -->

    <h1 class="title-gf">
      Para consultar el formato por ficha, digite el número de la ficha
    </h1>

    <form @submit.prevent="buscarPorFicha">
      <label class="label-gf" for="">Número de ficha</label>
      <input class="input-gf" type="text" v-model="buscarFicha">

      <div>
        <button class="button-gf" type="submit">
          Consultar Ficha
        </button>
      </div>
    </form>

  </section>

  <div class="list-students" v-for="item in aprendices" :key="item.numero_documento">
    <div class="card mb-3">
      <div class="card-body">
        <p class="card-text"><strong>Tipo documento:</strong> {{ item.tipo_documento }}</p>
        <p class="card-text"><strong>Número documento:</strong> {{ item.numero_documento }}</p>
        <p class="card-text"><strong>Nombre:</strong> {{ item.nombre }}</p>
        <p class="card-text"><strong>Apellidos:</strong> {{ item.apellidos }}</p>
        <p class="card-text"><strong>Celular:</strong> {{ item.celular }}</p>
        <p class="card-text"><strong>Correo electrónico:</strong> {{ item.correo_electronico }}</p>
        <p class="card-text"><strong>Estado:</strong> {{ item.estado }}</p>
      </div>
    </div>
  </div>

  <div v-if="buscarFicha && aprendices.length === 0" class="text-center mt-4">
    <p>No se encontró ningún aprendiz para la ficha ingresada.</p>
  </div>

</template>

<script>
import Header from '../components/Header.vue';

export default {
  components: {
    Header
  },
  data() {
    return {
      buscarFicha: '',
      aprendices: [],
      fichas: [
        {
          grupo_id: 123456,
          personas: [
            {
              tipo_documento: "CC",
              numero_documento: "1020304050",
              nombre: "Laura",
              apellidos: "Martínez Gómez",
              celular: "3104567890",
              correo_electronico: "laura.martinez@example.com",
              estado: "EN FORMACION"
            },
            {
              tipo_documento: "TI",
              numero_documento: "1122334455",
              nombre: "Juan",
              apellidos: "Pérez Rodríguez",
              celular: "3001234567",
              correo_electronico: "juan.perez@example.com",
              estado: "CANCELADO"
            }
          ]
        },
        {
          grupo_id: 654321,
          personas: [
            {
              tipo_documento: "CE",
              numero_documento: "987654321",
              nombre: "Ana",
              apellidos: "Gómez Ruiz",
              celular: "3119876543",
              correo_electronico: "ana.gomez@example.com",
              estado: "EN FORMACION"
            },
            {
              tipo_documento: "NUIP",
              numero_documento: "1234567890",
              nombre: "Carlos",
              apellidos: "Díaz Torres",
              celular: "3132223344",
              correo_electronico: "carlos.diaz@example.com",
              estado: "RETIRO VOLUNTARIO"
            }
          ]
        },
        {
          grupo_id: 789012,
          personas: [
            {
              tipo_documento: "PPT",
              numero_documento: "5678901234",
              nombre: "María",
              apellidos: "Fernández Salazar",
              celular: "3124567891",
              correo_electronico: "maria.fernandez@example.com",
              estado: "EN FORMACION"
            },
            {
              tipo_documento: "CC",
              numero_documento: "9988776655",
              nombre: "Diego",
              apellidos: "Ramírez López",
              celular: "3145678902",
              correo_electronico: "diego.ramirez@example.com",
              estado: "CANCELADO"
            }
          ]
        }
      ]
    }
  },
  methods: {
    buscarPorFicha() {
      console.log("Buscando ficha:", this.buscarFicha);
      const grupo = this.fichas.find(f => f.grupo_id === Number(this.buscarFicha));
      console.log("Grupo encontrado:", grupo);
      this.aprendices = grupo ? grupo.personas : [];
    }
  }
}
</script>

<style scoped>
.container-gf {
  width: 50%;
  height: 400px;
  background-color: rgb(255, 255, 255);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin: 0 auto;
  margin-top: 50px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  flex-direction: column;
}

.title-gf {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 1.3rem;
  margin-top: 25px;
  margin-bottom: 55px;
}

.label-gf {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 1.1rem;
}

.input-gf {
  width: 80%;
  padding: 0.8rem 0.8rem 0.8rem 2.5rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.3s ease;
  box-sizing: border-box;
}

.button-gf {
  width: 45%;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  font-size: 1.1rem;
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

.button-gf:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(8, 106, 73, 0.382);
}

.list-students{
  width: 90%;
  height: auto;
  margin: 0 auto;
}

/* ✅ Estilos responsive para pantallas menores a 768px */
@media (max-width: 1400px) {
  .container-gf {
    width: 60%;
    height: 300px;
    margin-top: 50px;
    padding: 1rem;
  }

  .icon-gf {
    height: 8rem;
    width: 8rem;
  }

  .title-gf {
    font-size: 1.5rem;
    text-align: center;
  }

  .button-gf {
    width: 40%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }
}

@media (max-width: 600px) {
  .container-gf {
    width: 60%;
    height: 320px;
    margin: 0 auto;
    margin-top: 80px;
    padding: 1rem;
  }

  .icon-gf {
    height: 5rem;
    width: 5rem;
  }

  .title-gf {
    font-size: 1.3rem;
    text-align: center;
  }

  .button-gf {
    width: 50%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }
}

@media (max-width: 600px) {
  .button-gf {
    font-size: 0.9rem;

  }
}
</style>