<script setup lang="js">
defineProps({
  label: {
    type: String,
    required: true,
  },
  to: {
    type: String,
    required: true,
  },
});
</script>
<template>
  <RouterLink
    :to="to"
    class="px-4 py-2 text-zinc-300 text-sm hover:text-white hover:bg-white/5 rounded-md"
    >{{ label }}</RouterLink
  >
</template>
