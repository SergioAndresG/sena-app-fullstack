<script setup lang="ts">
import AddUser from '../components/USERS/AddUsers.vue'
import DeleteUsers from '../components/USERS/DeleteUsers.vue';
import InfoUsers from '../components/USERS/InfoUsers.vue';
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import Header from '../components/Header.vue';
import Swal from 'sweetalert2';

const router = useRouter();

interface User {
  id: number;
  nombre: string;
  apellidos: string;
  correo: string;
  rol: string;
}

const users = ref<User[]>([]);
const showModal = ref(false);
const selectedUser = ref<User | null>(null);
const searchQuery = ref('');
const showModalDelete = ref(false);
const showModalRequest = ref(false);
const selectedUserId = ref<number | null>(null);
const isDeleting = ref(false);
const searchTerm = ref("")

// Abrir modal de eliminación
const openDeleteModal = (user: User) => {
  selectedUserId.value = user.id;
  selectedUser.value = user;
  showModalDelete.value = true;
};

const openMoldalInfo = (user: User) => {
  selectedUserId.value = user.id;
  selectedUser.value = user;
  showModalRequest.value = true;
};

// Abrir modal para agregar nuevo usuario
const openAddModal = () => {
  selectedUser.value = null; // Clear selected user for adding new
  showModal.value = true;
};
const cargarUsuarios = async () => {
  try {
    const respuesta = await axios.get('http://127.0.0.1:8000/usuarios/');
    users.value = respuesta.data;
  } catch (error) {
    console.error(error);
  }
}

const handleInstructorAdded = (newInstructor) => {
  console.log('Instructor agregado')
  // Actualizar tu lista, hacer refetch, etc.
  cargarUsuarios();

}

const handleInstructorRequest = (newInstructor) => {
  console.log('Instructor consultado')
  // Actualizar tu lista, hacer refetch, etc.
  cargarUsuarios();
}

const handleInstructorUpdate = (updatedInstructor) => {
  console.log('Instructor actualizado:');
  // Recargar la lista de usuarios
  cargarUsuarios();
};

// Manejar eliminación exitosa
const handleInstructorDeleted = (userId: number) => {
  console.log('Usuario eliminado:');
  // Recargar la lista de usuarios
  cargarUsuarios();


  // Reset selections
  selectedUserId.value = null;
  selectedUser.value = null;
};

const editUser = (user: User) => {
  selectedUser.value = { ...user };
  showModal.value = true;
}

const filtrarInstructores = computed(() => {
  if (!searchTerm.value.trim()) return users.value;

  const term = searchTerm.value.toLowerCase().trim()
  return users.value.filter(pro =>
    pro.nombre.toLowerCase().includes(term)
  )
});

function volver() {
  router.back()
}

onMounted(() => {
  cargarUsuarios();
});

function irAAdmin(){
  router.push('/admin')
}
</script>

<template>
  <div class="dashboard-container">
    <Header />

    <div class="floating-buttons">
      <!-- Botón izquierdo -->
      <div class="tooltip tooltip-left btn-left">
        <button class="back-buttons" @click="irAAdmin">
          <i class="fa-solid fa-arrow-left"></i>
        </button>
        <span class="tooltip-text">Regresar</span>
      </div>

      <!-- Contenedor de botones derechos -->
      <div class="right-buttons">
        <div class="tooltip">
          <button class="back-buttons">
            <i class="fa-solid fa-right-from-bracket"></i>
          </button>
          <span class="tooltip-text">Cerrar sesión</span>
        </div>
      </div>
    </div>

    <main class="main-content">
      <div class="dashboard-header">
        <h1>Gestión de Usuarios</h1>
      </div>
      <hr style="margin-bottom: 2rem;">
      <div class="actions">
        <div class="search-box">
          <input type="text" v-model="searchTerm" placeholder="Buscar usuarios..." class="search-input">
          <i class="fas fa-search"></i>

        </div>
        <button @click="openAddModal" class="btn btn-primary">
          <i class="fas fa-plus"></i> Nuevo Usuario
        </button>
        <AddUser v-model="showModal" :selected-user="selectedUser" @instructor-added="handleInstructorAdded"
          @instructor-updated="handleInstructorUpdate" />
      </div>
      <hr style="margin-bottom: 2rem;">

      <div class="users-grid">
        <div v-for="user in filtrarInstructores" :key="user.id" class="user-card">
          <div class="user-info">
            <h3>{{ user.nombre }} {{ user.apellidos }}</h3>
            <p>{{ user.correo }}</p>
            <span class="role-badge">{{ user.rol }}</span>
          </div>
          <div class="card-actions">
            <button @click="editUser(user)" class="btn btn-edit">
              <i class="fas fa-edit"></i>
            </button>
            <button @click="openDeleteModal(user)" class="btn btn-delete" :disabled="isDeleting"
              v-if="user.rol !== 'ADMINISTRADOR'">
              <i class="fas fa-trash"></i>
            </button>
            <DeleteUsers v-model="showModalDelete" :user-id="selectedUserId" :selected-user="selectedUser"
              :require-password="true" @instructor-deleted="handleInstructorDeleted" />
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
:root {
  --primary-color: #10b981;
  --primary-dark: #059669;
  --secondary-color: #6366f1;
  --background-light: #f8fafc;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --border-color: #e2e8f0;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --border-radius: 8px;
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.dashboard-container {
  min-height: 100vh;
  background-color: #ffffff;
}
.fa-circle-info{
  background: linear-gradient(135deg, #555 0%, var(--primary-dark) 100%);
  color: white;
  margin-left: 14rem;
  border: none;
  padding: 6px 6px;
  border-radius: 50%;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: var(--shadow-md);
  font-size: 0.9rem;
}
.fa-circle-info:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
.tooltip-info {
  position: relative; /* el padre controla dónde se ubica el tooltip */
  display: inline-block;
}

.tooltip-text-info {
  visibility: hidden;
  width: max-content; /* se ajusta al texto */
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 0.85rem;

  /* posicionamiento debajo */
  position: absolute;
  top: 120%; /* un poco más abajo del ícono */
  left: 91%;
  transform: translateX(-50%);

  /* transición */
  opacity: 0;
  transition: opacity 0.3s;
}

.tooltip-info:hover .tooltip-text-info {
  visibility: visible;
  opacity: 1;
}

.right-buttons{
  margin-right: 20px;
}
.main-content {
  padding: 2rem;
  max-width: 1000px;
  margin: 0 auto;
  margin-top: 80px;
}
.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}
.dashboard-header h1 {
  margin: auto;
  font-size: 2.5rem;
}
.actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}
.search-box {
  position: relative;
  display: flex;
  align-items: center;
}
.search-input {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  width: 400px;
  font-size: 0.9rem;
  margin: 10px;
}
.search-icon {
  position: absolute;
  left: 8px;
  color: #555;
  font-size: 1rem;
  pointer-events: none; /* que no bloquee clics */
}

.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-primary {
  background: linear-gradient(145deg, #1fb19e, #0b746b);
  color: white;
  transition: all 0.3s ease-in-out;
}

.btn-primary:hover {
  background-color: #45a049;
  transform: scale(1.01) translateY(-2px);

}

.users-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.user-card {
  background: white;
  border-radius: 12px;
  border: solid 2px #e0e0e0;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.user-card:hover {
  transform: translateY(-2px);
}

.user-info {
  margin-bottom: 1rem;
}

.role-badge {
  background: #e9ecef;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  color: #495057;
}

.card-actions {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-end;
}

.btn-edit {
  background-color: #2196F3;
  color: white;
}

.btn-delete {
  background-color: #f44336;
  color: white;
}

.btn-edit:hover,
.btn-delete:hover {
  opacity: 0.9;
}

/* Responsive Design */
@media (max-width: 768px) {
  .dashboard-header {
    gap: 1rem;
    text-align: center;
  }

 .actions {
    flex-direction: row;
    justify-content: center;
  }

  .right-buttons{
    margin-right: 20px;
  }

  

  .btn {
    flex-shrink: 0; /* El botón mantiene su tamaño */
  }

  .search-input {
    width: 100%;
  }

  .users-grid {
    grid-template-columns: 1fr;
  }
}
</style>