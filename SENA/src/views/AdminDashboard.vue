<script setup lang="ts">
import Header from '../components/Header.vue';

import Swal from "sweetalert2";
import { ref } from 'vue';
import axios from 'axios';
import router from '../router';
import { authService } from '../services/auth_service';

const inputFichas = ref<HTMLInputElement | null>(null)
const inputMaestro = ref<HTMLInputElement | null>(null)

function abrirExploradorFichas() {
  console.log("Abriendo input de fichas")
  inputFichas.value?.click()
}

function abrirExploradorMaestro() {
  inputMaestro.value?.click()
}

//Redireccionar al formato grupal
function irAGrupal() {
  router.push('/groupformat')
}

//Redireccionar al formato individual
function irAIndividual() {
  router.push('/individualformat')
}

function irAUsuarios() {
  router.push('/user-dashboard')
}

async function cerrarSession() {
  authService.logout();
  localStorage.removeItem('access_token')
  router.push('/');
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
function irAHistorial() {
  router.push('/historialReportesGenerados')
}
</script>

<template>
  <Header />

  <!-- Botón de logout fijo -->
  <div class="right-button-dashboard">
    <div class="tooltip-dashboard">
      <button class="back-buttons" @click="cerrarSession">
        <i class="fa-solid fa-right-from-bracket"></i>
      </button>
      <span class="tooltip-text-dashboard" >
        Cerrar sesión</span>
    </div>
  </div>

  <h1 class="title-admin">¡BIENVENIDO ADMINISTRADOR!</h1>
  <hr style="width: 50%;">

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
      <input type="file" ref="inputMaestro" style="display: none" @change="subirArchivoMaestro" accept=".xlsx, .xls" />
    </section>

    <section class="container-docs">
      <div>
        <img class="icon-docs" src="../assets/reporte_aprendices.png" alt="">
      </div>

      <article class="title-docs">
        Seleccione los reportes de Fichas
      </article>

      <button class="button-docs" @click="abrirExploradorFichas">
        Cargar Archivos
      </button>

      <input type="file" ref="inputFichas" style="display: none;" @change="subirFichas" accept=".xlsx, .xls" multiple />
    </section>

    <section class="container-docs">
      <div>
        <img class="icon-docs" src="../assets/reportes_descargas_img.png" alt="" style="width: 19rem;">
      </div>

      <article class="title-docs">
        Ver historial de formatos descargados
      </article>

      <button class="button-docs" @click="irAHistorial()">
        Ver Historial
      </button>

      <input type="file" ref="inputFichas" style="display: none;" @change="subirFichas" accept=".xlsx, .xls" multiple />
    </section>

    <section class="container-docs">
      <div>
        <img class="icon-docs" src="../assets/user_admin.png" alt="">
      </div>

      <article class="title-docs">
        Administración de usuarios
      </article>

      <button class="button-docs" @click="irAUsuarios()">
        Ver Usuarios
      </button>

      <input type="file" ref="inputFichas" style="display: none;" @change="subirFichas" accept=".xlsx, .xls" multiple />
    </section>


    <section class="container-docs">
      <div>
        <img class="icon-docs" src="../assets/group.png" alt="">
      </div>

      <article class="title-docs">
        Generar Reporte Grupal
      </article>

      <button class="button-docs" @click="irAGrupal">
        Generar Reporte
      </button>

      <input type="file" ref="inputFichas" style="display: none;" @change="subirFichas" accept=".xlsx, .xls" multiple />
    </section>


    <section class="container-docs">
      <div>
        <img class="icon-docs" src="../assets/individual.png" alt="">
      </div>

      <article class="title-docs">
        Generar Reporte Individual
      </article>

      <button class="button-docs" @click="irAIndividual">
        Generar Reporte
      </button>

      <input type="file" ref="inputFichas" style="display: none;" @change="subirFichas" accept=".xlsx, .xls" multiple />
    </section>

  </div>

</template>

<style scoped>
.title-admin {
  text-align: center;
  padding: 2rem;
  font-family: 'Inter', sans-serif;
  letter-spacing: 3px;
  font-size: 2rem;
}

.container-section-docs {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  max-width: 1150px;
  margin: 0 auto;
  margin-top: 30px;
  padding: 2rem 0;
  overflow: hidden;
}

.container-docs {
  background: #ffffff;
  border-radius: 20px;
  padding: 3rem 2rem;
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

.container-docs::before {
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

.container-docs:hover {
  transform: translateY(-10px);
  box-shadow:
    0 20px 40px rgba(0, 0, 0, 0.12),
    0 8px 16px rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.3);
}

.container-docs:hover::before {
  transform: scaleX(1);
}

.icon-container {
  position: relative;
  margin-bottom: 2rem;
}

.icon-docs {
  height: 15rem;
  width: 16rem;
  transition: transform 0.3s ease;
  filter: drop-shadow(0 4px 8px rgba(16, 185, 129, 0.2));
}

.container-docs:hover .icon-docs {
  transform: scale(1.05);
}

.title-docs {
  font-family: 'Inter', sans-serif;
  font-size: 1.6rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 1.5rem;
  line-height: 1.3;
}

.description-docs {
  font-size: 0.95rem;
  color: #6b7280;
  margin-bottom: 2rem;
  line-height: 1.6;
  max-width: 280px;
}

.button-docs {
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

.button-docs::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.button-docs:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.4);
  background: linear-gradient(135deg, #059669 0%, #047857 100%);
}

.button-docs:hover::before {
  left: 100%;
}



/* RESPONSIVE STYLES - Cada breakpoint mantiene TODOS los efectos */

@media (max-width: 1400px) {
  .container-section-docs {
    margin-right: 15px;
    padding: 10px;
  }

  .container-docs {
    width: 90%;
    height: 350px;
    margin-top: 50px;
    padding: 1rem;
    margin-left: 10px;
    margin-right: 15px;
  }

  .container-docs:hover {
    transform: translateY(-8px) !important;
    box-shadow:
      0 18px 35px rgba(0, 0, 0, 0.12),
      0 6px 14px rgba(16, 185, 129, 0.2) !important;
    border-color: rgba(16, 185, 129, 0.3) !important;
  }

  .container-docs:hover::before {
    transform: scaleX(1) !important;
  }

  .icon-docs {
    height: 12rem;
    width: 12rem;
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
    justify-content: center;
    padding: 0 1rem;
    margin: 0 auto;
    overflow-x: hidden;
    margin-top: 70px;
  }

  .container-docs {
    width: 90%;
    max-width: 400px;
    margin: 20px auto;
    height: auto;
  }

  .container-docs:hover {
    transform: translateY(-6px) !important;
    box-shadow:
      0 16px 30px rgba(0, 0, 0, 0.12),
      0 5px 12px rgba(16, 185, 129, 0.2) !important;
    border-color: rgba(16, 185, 129, 0.3) !important;
  }

  .container-docs:hover::before {
    transform: scaleX(1) !important;
  }

  .button-docs {
    width: 60%;
    font-size: 1rem;
    padding: 0.7rem;
  }
}

@media (max-width: 772px) {
  .container-section-docs {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 1rem;
    margin-top: 100px;
  }

  .container-docs {
    padding: 2rem 1.5rem;
  }

  .container-docs:hover {
    transform: translateY(-5px) !important;
    box-shadow:
      0 15px 28px rgba(0, 0, 0, 0.12),
      0 4px 10px rgba(16, 185, 129, 0.2) !important;
    border-color: rgba(16, 185, 129, 0.3) !important;
  }

  .container-docs:hover::before {
    transform: scaleX(1) !important;
  }

  .title-docs {
    font-size: 1.4rem;
  }

  .button-docs {
    min-width: 160px;
    padding: 0.75rem 2rem;
  }
}

@media (max-width: 600px) {
  .container-section-docs {
    grid-template-columns: 1fr;
    justify-content: center;
    padding-left: 15px;
    overflow-x: hidden;
    margin-top: 85px;
  }

  .right-button-dashboard{
    margin-top: 40px;
  }

  .container-docs {
    width: 75%;
    height: 360px;
    margin-top: 20 0px;
  }

  .container-docs:hover {
    transform: translateY(-4px) !important;
    box-shadow:
      0 12px 25px rgba(0, 0, 0, 0.12),
      0 3px 8px rgba(16, 185, 129, 0.2) !important;
    border-color: rgba(16, 185, 129, 0.3) !important;
  }

  .container-docs:hover::before {
    transform: scaleX(1) !important;
  }

  .icon-docs {
    height: 12rem;
    width: 12rem;
  }

  .title-docs {
    font-size: 1.3rem;
    text-align: center;
    margin-top: 15px;
  }

  .button-docs {
    width: 70%;
    font-size: 1.1rem;
    padding: 0.8rem;
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