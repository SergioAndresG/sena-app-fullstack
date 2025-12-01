// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import InstructorDashboard from '../views/InstructorDashboard.vue'
import IndividualFormat from '../views/IndividualFormat.vue'
import GroupFormat from '../views/GroupFormat.vue'
import ViewHistorialReports from '../views/ViewHistorialReports.vue'
import DashboardUsers from '../views/DashboardUsers.vue'
import AddUsers from '../components/USERS/AddUsers.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/admin',
    name: 'AdminDashboard',
    component: AdminDashboard
  },
  {
    path: '/instructor',
    name: 'InstructorDashboard',
    component: InstructorDashboard
  },
  {
    path: '/individualformat',
    name: 'IndividualFormat',
    component: IndividualFormat
  },
  {
    path: '/groupformat',
    name: 'GroupFormat',
    component: GroupFormat
  },
  {
    path: '/historialReportesGenerados',
    name: 'HistorialReportesGenerados',
    component: ViewHistorialReports
  },
  {
    path: '/user-dashboard',
    name: 'UserDashboard',
    component: DashboardUsers
  },
  {
    path: '/addUser',
    name: 'AddUser',
    component: AddUsers
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
