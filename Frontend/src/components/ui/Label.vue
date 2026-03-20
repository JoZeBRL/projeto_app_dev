<script setup lang="ts">
defineProps<{ for?: string }>();
</script>

<template>
  <label :for="for" class="text-sm font-medium text-gray-700 dark:text-gray-300 flex items-center gap-2 select-none mb-2">
    <slot />
  </label>
</template>
