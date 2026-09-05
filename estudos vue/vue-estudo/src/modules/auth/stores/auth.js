import { defineStore } from "pinia";
import { computed, ref } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const IsLoading = ref(false);
  const user = ref(null);

  const isAtuthenticated = computed(() => user.value !== null);
  //simula uma api
  async function login(email, name) {
    try {
      IsLoading.value = true;
      await new Promise((resolve) => setTimeout(resolve, 2000));
      user.value = {
        email: "resenha@123",
        name: "jaum vitu",
      };
    } finally {
      IsLoading.value = false;
    }
  }

  async function logout() {
    try {
      IsLoading.value = true;
      await new Promise((resolve) => setTimeout(resolve, 2000));
      user.value = null;
    } finally {
      IsLoading.value = false;
    }
  }
  return {
    user,
    IsLoading,
    isAtuthenticated,
    login,
    logout,
  };
});
