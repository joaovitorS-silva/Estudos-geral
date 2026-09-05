<script setup lang="js">
import { ref } from "vue";
import Title from "../../../shared/components/title.vue";
const count = ref(0);
function aumentar() {
  count.value++;
}
function diminuir() {
  count.value--;
}

function resetar() {
  count.value = 0;
}
</script>

<template>
  <div>
    <Title title="Contador" subtitle="exemplo de contador com vue 3"></Title>
    <div>conteudo do contador</div>
    <div class="flex flex-col gap-10">
      {{ count }}
      <button @click="aumentar" class="bg-zinc-500 text-white px-4 py-2">
        +
      </button>
      <button @click="diminuir" class="bg-zinc-500 text-white px-4 py-2">
        -
      </button>
      <button @click="resetar" class="bg-zinc-500 text-white px-4 py-2">
        Resetar
      </button>
    </div>
  </div>
</template>
