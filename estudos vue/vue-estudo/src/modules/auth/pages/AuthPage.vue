<script setup lang="js">
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import Loading from "../../../shared/components/Loading.vue";
const authStore = useAuthStore();
const router = useRouter();
const route = useRoute();
async function handleLogin() {
  await authStore.login("email", "name");
  redirect();
  console.log("123");
}
async function redirect() {
  const q = route.query.redirect;
  const r = (typeof q === "string" && q.startsWith("/")) ? q : "/";
  await router.replace(r);
}
</script>

<template>
  <Loading v-if="authStore.IsLoading" />
  <div v-else class="flex justify-center items-center min-h-screen">
    <h1 class="text-4xl font-black">auth Page</h1>
    <button @click="handleLogin" class="w-28 bg-red-700 text-black h-28">
      butao
    </button>
  </div>
</template>
1