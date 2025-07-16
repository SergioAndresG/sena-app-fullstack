<script setup lang="ts">
import { ref } from 'vue';
import axios from "axios";
import Header from '../components/Header.vue';
import EditAprendizModal from '../components/EditAprendizModal.vue'

// variable que guradara los aprendices
interface Aprendiz {
  tipo_documento: string
  documento: string
  nombre: string
  apellido: string
  celular: string
  correo: string
  estado: string
}

const aprendices = ref<Aprendiz[]>([])
// variable que guarda la ficha digitada por el usuario
let ficha = ref(<string>(''));
let documento = ref(<string>(''));
// varibale que controla el estado de la caja del mensaje
const busquedaRealizada = ref(false);
const mostrarResultados = ref(false);
const cargando = ref(false)

//Variables para el model de edición de aprendices
const mostrarModal = ref(false)
const aprendizSeleccionado = ref<Aprendiz | null>(null)

// Función que cargara los aprendices de la ficha que reciba
const cargarAprendicesFicha = async (codigoFicha: String, numDocumento: String) => {
  cargando.value = true;

  try {
    await new Promise(resolve => setTimeout(resolve, 800));
    const respuesta = await axios.get(`http://127.0.0.1:8000/ficha/${codigoFicha}/aprendiz`, {
      params: {
        documento: numDocumento
      }
    });

    console.log('Respuesta del backend:', respuesta.data);

    aprendices.value = respuesta.data.aprendices;
    busquedaRealizada.value = true;
    mostrarResultados.value = true;

  } catch (error) {
    console.error('Error al cargar los aprendices ', error);
    aprendices.value = []
    busquedaRealizada.value = true;
    mostrarResultados.value = true;

  } finally {
    cargando.value = false;
  }
}

// Función que se llama al hacer clic en el botón
const consultarFicha = async () => {
  if (ficha.value.trim() !== '' && documento.value.trim() !== '') {
    cargarAprendicesFicha(ficha.value, documento.value)
  } else {
    alert('Ingrese una ficha')
  }
}

const volverABusqueda = () => {
  mostrarResultados.value = false;
  busquedaRealizada.value = false;
  aprendices.value = [];
  ficha.value = '';
  documento.value = '';
}

function abrirEdicion(aprendiz: Aprendiz) {
  console.log('Aprendiz seleccionado:', aprendiz)
  aprendizSeleccionado.value = { ...aprendiz }
  mostrarModal.value = true
}

function actualizarDatos(nuevosDatos: Aprendiz) {
  const index = aprendices.value.findIndex(
    (a) => a.documento === nuevosDatos.documento
  )
  if (index !== -1) {
    aprendices.value[index] = nuevosDatos
  }
}
</script>

<template>
  <Header></Header>

  <Transition name="fade-slide" mode="out-in">
    <!--Formualario de busqueda-->
    <section v-if="!mostrarResultados" class="container-if" key="search-form">
      <h1 class="title-if">
        Para consultar el formato por aprendiz, digite el número de la ficha y el número de documento del aprendiz
      </h1>

      <form @submit.prevent="consultarFicha">
        <div class="container-data">
          <label for="" class="label-if"> No. Ficha 🖱️</label>
          <input v-model="ficha" class="input-if" type="text" placeholder="Ingresa el número de la ficha">

          <label for="" class="label-if"> No. de documento</label>
          <input v-model="documento" class="input-if" type="text" placeholder="Ingresa el número de documento">
        </div>

        <div>
          <button class="button-if" type="submit" :disabled="cargando">
            <span v-if="!cargando">Consultar Aprendiz</span>
            <span v-else>Buscando...</span>
          </button>
        </div>
      </form>
    </section>

    <!--Sección de resultados-->
    <section v-else class="results-section" key="results">
      <div class="results-header">
        <h2 class="results-title">
          Resultados para el documento: {{ documento }} <br>
          Ficha: {{ ficha }}
        </h2>
        <button @click="volverABusqueda" class="buttom-back">
          <i class="fa-solid fa-arrow-left"></i>
          Volver a buscar
        </button>
      </div>
      <!--Tabla de resultados-->
      <Transition>
        <div v-if="aprendices.length > 0" class="table-container">
          <table class="styled-table">
            <thead>
              <tr>
                <th># </th>
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
              <tr v-for="(item, index) in aprendices" :key="item.documento" class="table-row"
                :style="{ 'animation-delay': `${index * 0.1}s` }">
                <td>{{ index + 1 }}</td>
                <td>{{ item.tipo_documento }}</td>
                <td>{{ item.documento }}</td>
                <td>{{ item.nombre }}</td>
                <td>{{ item.apellido }}</td>
                <td>{{ item.celular }}</td>
                <td>{{ item.correo }}</td>
                <td>{{ item.estado }}</td>
                <td class="no-border">
                  <button class="button-edit" @click="abrirEdicion(item)">
                    <img class="icon-edit" src="../assets/edit.png" alt="">
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </Transition>

      <!--Mensaje si no hay resultados-->
      <Transition name="fade" appear>
        <!-- Mensaje si se hizo la búsqueda y no hay resultados -->
        <div v-if="aprendices.length === 0 && busquedaRealizada" class="text-center mt-4">
          <p>No se encontró ningún aprendiz para la ficha ingresada.</p>
        </div>
      </Transition>
    </section>
  </Transition>

  <EditAprendizModal :mostrar="mostrarModal" :aprendiz="aprendizSeleccionado" @cerrar="mostrarModal = false"
    @actualizar="actualizarDatos" />
  <div class="spacer"></div>
</template>

<style scoped>
.container-if {
  width: 50%;
  height: 500px;
  background-color: rgb(255, 255, 255);
  display: flex;
  justify-content: center;
  text-align: center;
  margin: 0 auto;
  margin-top: 50px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.189);
  flex-direction: column;
}

.title-if {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 1.3rem;
  margin-top: 25px;
  margin-bottom: 55px;
}

.label-if {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 1.1rem;
}

.input-if {
  width: 40%;
  padding: 0.8rem 0.8rem 0.8rem 0.8rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: all 0.3s ease;
  box-sizing: border-box;
  margin: 1rem;
  text-align: center;
}

.container-data {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  text-align: left;
}

.button-if {
  width: 25%;
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

.button-if:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(8, 106, 73, 0.382);
}

.button-if:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* Estilos de la tabla */
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
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.422);
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

/* Estilos de experiencia mejorada */
.results-section {
  padding: 20px;
  max-width: 1500px;
  margin: 0 auto;
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding: 20px;
  background-color: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.results-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.buttom-back {
  display: flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, #10b981 0%, #208b69 100%);
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(79, 70, 229, 0.25);
}

.buttom-back:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 15px rgba(79, 70, 229, 0.35);
}

.icon-back {
  height: 16px;
  width: 16px;
}

.no-results {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
  padding: 40px;
}

.no-results-content {
  text-align: center;
  background: white;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  max-width: 400px;
}

.no-results-subtitle {
  color: #64748b;
  font-size: 0.9rem;
  margin-top: 8px;
}

/* Transiciones */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.fade-slide-enter-form {
  opacity: 0;
  transform: translateX(-30px);
}

.table-fade-enter-active {
  transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.table-fade-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.table-row {
  animation: slideInUp 0.6s ease-out both;
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* ✅ Estilos responsive para pantallas menores a 768px */
@media (max-width: 1400px) {
  .container-if {
    width: 60%;
    height: 300px;
    margin-top: 50px;
    padding: 1rem;
  }

  .icon-if {
    height: 8rem;
    width: 8rem;
  }

  .title-if {
    font-size: 1.5rem;
    text-align: center;
  }

  .button-if {
    width: 40%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }
}

@media (max-width: 600px) {
  .container-if {
    width: 60%;
    height: 320px;
    margin: 0 auto;
    margin-top: 80px;
    padding: 1rem;
  }

  .icon-if {
    height: 5rem;
    width: 5rem;
  }

  .title-if {
    font-size: 1.3rem;
    text-align: center;
  }

  .button-if {
    width: 50%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }

  .results-header {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }

  .results-title {
    font-size: 1.2rem;
  }

  .button-back {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 600px) {
  .button-if {
    font-size: 0.9rem;

  }
}
</style>