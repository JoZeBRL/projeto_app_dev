<script setup lang="ts">
import type { Component } from 'vue';

interface Props {
  title: string;
  description: string;
  icon: Component;
  colorClass: string;
}

defineProps<Props>();
defineEmits(['click']);
</script>

<template>
  <button 
    @click="$emit('click')"
    :class="[
      'group p-8 rounded-3xl border border-gray-100 dark:border-white/5 transition-all duration-300 text-left w-full',
      'hover:shadow-xl hover:shadow-black/5 hover:-translate-y-1',
      colorClass
    ]"
  >
    <div class="flex flex-col h-full justify-between gap-6">
      <div class="p-3 w-fit rounded-2xl bg-white dark:bg-white/10 shadow-sm group-hover:scale-110 transition-transform">
        <component :is="icon" class="w-6 h-6 text-gray-900 dark:text-white" />
      </div>
      
      <div>
        <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2 italic tracking-tight">
          {{ title }}
        </h3>
        <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed font-medium">
          {{ description }}
        </p>
      </div>
    </div>
  </button>
</template>