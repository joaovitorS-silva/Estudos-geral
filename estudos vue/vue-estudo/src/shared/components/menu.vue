<script setup lang="js">
import MenuItem from "./menuItem.vue";
</script>
<template>
  <nav class="flex flex-col">
    <MenuItem label="Inicio" to="/" />
    <MenuItem label="Contador # 1" to="/Counter" />
    <MenuItem label="Contador #2 " to="/counter/pinia" />
  </nav>
</template>
<style scoped></style>
