<script setup lang="ts">
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

import Swal from "sweetalert2";
import { ref } from 'vue';
import axios from 'axios';


const inputFichas = ref<HTMLInputElement | null>(null)
const inputMaestro = ref<HTMLInputElement | null>(null)

function abrirExploradorFichas() {
   console.log("Abriendo input de fichas")
  inputFichas.value?.click()
}

function abrirExploradorMaestro() {
   console.log("Abriendo input de")
  inputMaestro.value?.click()
}

async function subirFichas(event: Event) {
  const files = (event.target as HTMLInputElement).files
  if (!files || files.length === 0) return
  const formData = new FormData()
  for (let i = 0; i < files.length; i++) {
    formData.append('archivos', files[i]) // El nombre 'archivos' debe coincidir con el parámetro del backend
  }
  Swal.fire({
    title: 'Subiendo fichas...',
    html: 'Progreso: <b>0%</b>',
    allowOutsideClick: false,
    didOpen: () => {
      Swal.showLoading()
    }
  })
  try {
    const response = await axios.post('http://localhost:8000/upload-fichas/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress: (progressEvent) => {
        const percent = Math.round((progressEvent.loaded * 100) / (progressEvent.total || 1))
        Swal.getHtmlContainer()!.querySelector('b')!.textContent = `${percent}%`
      },
    })
    Swal.fire({
      icon: 'success',
      title: '✅ Archivos subidos',
      text: response.data.message,
      timer: 2000,
      showConfirmButton: false,
    })
  } catch (error) {
    console.error('Error al subir fichas:', error)
    Swal.fire({
      icon: 'error',
      title: '❌ Error',
      text: 'No se pudieron subir los archivos. Verifica el formato o el servidor.',
    })
  }
}

// declaramos la funcion async para poder usar el await dentro de la misma
async function subirArchivoMaestro(event: Event) { // Recibe un evento como parametro (changue del input file) con tipado TypeScript
  // obtenemos el elemento que disparo el evento le indicamos que es un input especifico de HTML
  const fileList = (event.target as HTMLInputElement).files
  // validamos que se vayan a subir archivos si no, termina la funcion con un return
  if (!fileList || fileList.length === 0) return


  const archivo = fileList[0] // Tomamos el primer archivo de la lista 
  const formData = new FormData() // Creamos un objeto Forma Data para enviar archivos por HTTp
  formData.append('archivo', archivo) // Agregamos el archivo al formData con la clave 'archivo'

  let timerInterval: any = null
  let progress = 0

  Swal.fire({
    title: 'Subiendo archivo...',
    html: 'Progreso: <b>0%</b>',
    allowOutsideClick: false,
    didOpen: () => {
      Swal.showLoading()
    },
  })

  // Definimos un bloque try catch, para capturar errores
  try {
    // hacemos la peticion al backend enviando el archivo en el cuerpo de la respuesta
    const response = await axios.post('http://localhost:8000/upload-archivo-maestro/', formData, {
      // especificamos el tipo de contenido
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    // mostramos este mensaje si es exitosa
    Swal.fire({
      icon: 'success',
      title: '✅ Archivo subido',
      text: response.data.message,
      timer: 2000,
      showConfirmButton: false,
    })
  } catch (error) {
    // mostramos este mensaje si algo ha fallado
        console.error('Error al subir archivo:', error)

    Swal.fire({
      icon: 'error',
      title: '❌ Error',
      text: 'No se pudo subir el archivo. Verifica el formato o el servidor.',
    });
  }
}
</script>


<template>
  <Header />

  <div class="container-section-docs">
    <section class="container-docs">

      <div>
        <img class="icon-docs" src="../assets/logo_admin.png" alt="">
      </div>

      <article class="title-docs">
          Seleccione el reporte PE-04
      </article>

      <button class="button-docs" @click="abrirExploradorMaestro">
          Cargar Archivos
      </button>
      <input
        type="file"
        ref="inputMaestro"
        style="display: none"
        @change="subirArchivoMaestro"
        accept=".xlsx, .xls"
      />
    </section>

    <section class="container-docs">
      <div>
        <img class="icon-docs" src="../assets/submit.png" alt="">
      </div>

      <article class="title-docs">
        Seleccione los reportes de Fichas
      </article>

      <button class="button-docs"  @click="abrirExploradorFichas">
          Cargar Archivos
      </button>

        <input 
        type="file"
        ref="inputFichas"
        style="display: none;"
        @change="subirFichas"
        accept=".xlsx, .xls"
        multiple

      />


    </section>
  </div>
</template>


<style scoped>
.container-section-docs{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  padding: 2rem;
  justify-items: center;
}

.container-docs {
  width: 80%;
  height: 450px;
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
  height: 13rem;
  width: 13rem;
}

.title-docs {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 1.5rem;
  margin-top: 35px;
}

.button-docs {
  width: 35%;
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
    width: 90%;
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
    width: 45%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }
}

@media (max-width: 800px) {
  .container-section-docs {
    grid-template-columns: 1fr;
  }

  .container-docs{
    width: 70%;
  }

  .button-docs {
    width: 40%;
    font-size: 1.1rem;
    padding: 0.8rem;
  }
}

@media (max-width: 600px) {
  .container-docs {
    width: 70%;
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
    width: 70%;
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

