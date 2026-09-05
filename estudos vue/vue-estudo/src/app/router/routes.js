import AppLayout from "../../shared/layouts/AppLayout.vue";
import HomePage from "../../modules/samples/pages/HomePage.vue";
import AuthPage from "../../modules/auth/pages/AuthPage.vue";
import CounterPage from "../../modules/auth/pages/CounterPage.vue";
import CounterPiniaPage from "../../modules/auth/pages/CounterPiniaPage.vue";

export const routes = [
  {
    name: "Auth",
    path: "/auth",
    component: AuthPage,
  },

  {
    path: "/",
    component: AppLayout,
    meta: { requiresAuth: true },
    children: [
      {
        name: "Home",
        path: "",

        component: HomePage,
      },

      { name: "Counter", path: "counter", component: CounterPage },
      {
        name: "CounterPinia",
        path: "counter/pinia",
        component: CounterPiniaPage,
      },
    ],
  },
];
