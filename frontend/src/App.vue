<script setup lang="ts">
import Footer from './components/Footer.vue';
import { useRoute } from 'vue-router';

const route = useRoute()
</script>

<template>
  <div id="app">
    <router-view /> <!-- Aquí se renderiza cada vista según la ruta -->
    <Footer v-if="route.path !== '/' "/> <!-- Mostramos el Footer en todas las vistas Excepto en la principal '/' -->
  </div>
</template>

<style>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}
</style>


