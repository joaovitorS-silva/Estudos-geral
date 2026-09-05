<script setup lang="js">
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
  },
});
</script>

<template>
<div>
  <h1 class="text-lg font-black">{{ props.title }}</h1>
  <h2 v-if="props.subtitle" class="text-zinc-500">{{ props.subtitle }}</h2>
</div>
</template>
