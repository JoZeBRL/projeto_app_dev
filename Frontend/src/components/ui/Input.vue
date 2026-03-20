<script setup lang="ts">
import { ref, computed } from 'vue';
import { Eye, EyeOff } from 'lucide-vue-next';

const props = withDefaults(defineProps<{
  modelValue: string | number;
  type?: string;
  placeholder?: string;
  id?: string;
  icon?: any; // Componente de ícone do Lucide
  disabled?: boolean;
}>(), {
  type: 'text',
  placeholder: '',
  disabled: false
});

const emit = defineEmits(['update:modelValue']);

const showPassword = ref(false);

const currentType = computed(() => {
  if (props.type === 'password') {
    return showPassword.value ? 'text' : 'password';
  }
  return props.type;
});
</script>

<template>
  <div class="relative w-full">
    <div v-if="icon" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 flex items-center justify-center pointer-events-none">
      <component :is="icon" class="h-5 w-5" />
    </div>

    <input
      :id="id"
      :type="currentType"
      :value="modelValue"
      @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
      :placeholder="placeholder"
      :disabled="disabled"
      :class="[
        'w-full bg-[#f3f3f5] dark:bg-[#1f1f1f] border border-transparent focus:border-gray-300 dark:focus:border-gray-700 focus:ring-0 rounded-[200px] h-12 text-gray-900 dark:text-white outline-none transition-all placeholder:text-gray-400',
        icon ? 'pl-11' : 'pl-4',
        type === 'password' ? 'pr-12' : 'pr-4',
        disabled ? 'opacity-50 cursor-not-allowed' : ''
      ]"
    />

    <button
      v-if="type === 'password'"
      type="button"
      @click="showPassword = !showPassword"
      class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 transition-colors focus:outline-none flex items-center justify-center"
      tabindex="-1"
    >
      <EyeOff v-if="!showPassword" class="h-5 w-5" />
      <Eye v-else class="h-5 w-5" />
    </button>
  </div>
</template>
