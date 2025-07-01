<script setup>
import HelloWorld from './views/HomePage.vue'
</script>

<template>
  <div id="app">
    <router-view /> <!-- Aquí se renderiza cada vista según la ruta -->
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


