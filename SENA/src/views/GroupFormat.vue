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

  <div v-if="aprendices.length > 0" class="table-container">
    <table class="styled-table">
      <thead>
        <tr>
          <th>Tipo documento</th>
          <th>Número documento</th>
          <th>Nombre</th>
          <th>Apellidos</th>
          <th>Celular</th>
          <th>Correo electrónico</th>
          <th>Estado</th>
          <th>Editar</th> <!-- Nueva columna -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in aprendices" :key="item.numero_documento">
          <td>{{ item.tipo_documento }}</td>
          <td>{{ item.numero_documento }}</td>
          <td>{{ item.nombre }}</td>
          <td>{{ item.apellidos }}</td>
          <td>{{ item.celular }}</td>
          <td>{{ item.correo_electronico }}</td>
          <td>{{ item.estado }}</td>
          <td class="no-border">
            <button class="button-edit">
              <img class="icon-edit" src="../assets/edit.png" alt="">
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Mensaje si se hizo la búsqueda y no hay resultados -->
  <div v-if="busquedaRealizada && aprendices.length === 0" class="text-center mt-4">
    <p>No se encontró ningún aprendiz para la ficha ingresada.</p>
  </div>

  <div class="spacer"></div>

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
      busquedaRealizada: false,
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
      this.busquedaRealizada = true;
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

.text-center {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 1.1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  margin-top: 50px;
  background-color: #f9f9f9;
  width: 70%;
  height: 200px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.table-container {
  width: 95%;
  margin: 20px auto;
  overflow-x: auto;
}

.styled-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 10px 10px;
  font-family: 'Inter', sans-serif;
  font-size: 0.95rem;
}

.styled-table thead tr {
  background-color: #ffffff;
  color: rgb(0, 0, 0);
  text-align: left;
}

.styled-table th,
.styled-table td {
  padding: 12px 15px;
  background-color: #ffffff;
  border-radius: 5px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.199);
}

.styled-table tbody tr:hover {
  background-color: #e6f4f1;
  transition: background-color 0.3s ease;
}

.container-btn-edit {
  display: flex;
  justify-content: center;
  align-items: center;
}

.no-border {
  border: none;
  background-color: transparent;
}

.button-edit {
  width: 100%;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  font-size: 1rem;
  padding: 0.4rem;
  border-radius: 0.2rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  animation: slideUp 0.6s ease-out;
  margin: 0 auto;
  margin-top: 5px;
}

.button-edit:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(8, 106, 73, 0.382);
}

.icon-edit {
  height: 15px;
}

.spacer {
  height: 50px;
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