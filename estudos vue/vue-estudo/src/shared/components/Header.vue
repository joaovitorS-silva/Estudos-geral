<script setup lang="js">
import { useRouter } from "vue-router";
import AuthPage from "../../modules/auth/pages/AuthPage.vue";
import { useAuthStore } from "../../modules/auth/stores/auth.js";

const authStore = useAuthStore();
const router = useRouter();

async function handleLogout() {
  await authStore.logout();
  router.push({ name: "Auth" });
}
</script>
<template>
  <header
    class="flex justify-between items-center px-6 border-b border-zinc-800"
  >
    <h1 class="text-xl font-black">Vue 3</h1>
    <div class="flex gap-3 items-center">
      <div>
        <span class="text-sm font-bold text-zinc-400">{{
          authStore.user.name
        }}</span>
        <span class="text-xs text-zinc-500">{{ authStore.user.email }}</span>
      </div>
      <button @click="handleLogout()">SAIR</button>
    </div>
  </header>
</template>
