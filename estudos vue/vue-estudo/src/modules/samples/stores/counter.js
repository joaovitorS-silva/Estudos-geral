import { defineStore } from "pinia";
import { computed,ref } from "vue";

export const useCounterStore = defineStore("counter", () => {
  const counter = ref(0);
  const doublecount = computed(() => counter.value * 2);
  function aumentar1() {
    counter.value++;
  }
  function diminuir1() {
    counter.value--;
  }
  function resetar0() {
    counter.value = 0;
  }

  return { counter, aumentar1, diminuir1, resetar0, doublecount };
});
