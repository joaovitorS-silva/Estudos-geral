<script setup lang="ts">
import { useAuthStore } from "../../modules/auth/stores/auth.js";
import Header from "../components/Header.vue";
import Loading from "../components/Loading.vue";
import Menu from "../components/menu.vue";
const authStore = useAuthStore();
</script>

<template>
  <Loading v-if="authStore.IsLoading" />
  <div v-else class="flex flex-col min-h-screen">
    <Header />
    <div class="flex flex-1">
      <aside class="w-64 h-screen bg-zinc-900 border-r border-zinc-800">
        <Menu />
      </aside>
      <main><RouterView /></main>
    </div>
  </div>
</template>
