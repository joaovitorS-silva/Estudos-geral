<script setup lang="js">
import Title from "../../../shared/components/title.vue";
import { useCounterStore } from "/src/modules/samples/stores/counter.js";
const counterStore = useCounterStore();
</script>

<template>
  <div class="flex flex-col gap-6">
    <Title
      title="Contador com Pinia"
      subtitle="Exmeplos de contador com pinia e estado"
    ></Title>
    <div class="flex flex-col">
      <span class="text-5xl">{{ counterStore.counter }}</span>
      <span>{{ counterStore.doublecount }}</span>
    </div>
    <button
      @click="counterStore.aumentar1()"
      class="bg-zinc-500 text-white px-4 py-2"
    >
      +
    </button>
    <button
      @click="counterStore.diminuir1()"
      class="bg-zinc-500 text-white px-4 py-2"
    >
      -
    </button>
    <button
      @click="counterStore.resetar0()"
      class="bg-zinc-500 text-white px-4 py-2"
    >
      Resetar
    </button>
  </div>
</template>
