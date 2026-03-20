<script setup lang="ts">
import { ChevronRight } from 'lucide-vue-next';

withDefaults(defineProps<{
  type?: 'button' | 'submit' | 'reset';
  disabled?: boolean;
  showArrow?: boolean;
  variant?: 'primary' | 'outline' | 'ghost';
}>(), {
  type: 'button',
  disabled: false,
  showArrow: true,
  variant: 'primary'
});
</script>

<template>
  <button
    :type="type"
    :disabled="disabled"
    :class="[
      'w-full h-12 flex items-center justify-center relative rounded-[200px] transition-all duration-200 select-none outline-none',
      variant === 'primary' ? 'bg-black text-white hover:bg-gray-800 dark:bg-white dark:text-black dark:hover:bg-gray-200' : '',
      variant === 'outline' ? 'bg-transparent border border-gray-300 text-gray-700 hover:bg-gray-50' : '',
      variant === 'ghost' ? 'bg-transparent text-gray-500 hover:text-gray-900' : '',
      disabled ? 'opacity-50 cursor-not-allowed' : 'active:scale-[0.98]'
    ]"
  >
    <span class="text-sm font-medium tracking-wide"><slot /></span>
    
    <div 
      v-if="showArrow && variant === 'primary'" 
      class="w-8 h-8 bg-white dark:bg-black rounded-full flex items-center justify-center absolute right-2 shadow-sm"
    >
      <ChevronRight class="w-4 h-4 text-black dark:text-white" />
    </div>
  </button>
</template>
