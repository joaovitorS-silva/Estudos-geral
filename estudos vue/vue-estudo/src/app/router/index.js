import { createRouter, createWebHistory } from "vue-router";
import { routes } from "./routes";
import { useAuthStore } from "../../modules/auth/stores/auth";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});
router.beforeEach((to, from) => {
  const AuthStore = useAuthStore();
  if (to.name != "Auth" && to.meta.requiresAuth && !AuthStore.isAtuthenticated)
    return { name: "Auth", query: { redirect: to.fullPath } };

  if (AuthStore.isAtuthenticated && to.name === "Auth") {
    const redirect = to.query.redirect ?? { name: "Home" };
    return redirect;
  }
});
export default router;
