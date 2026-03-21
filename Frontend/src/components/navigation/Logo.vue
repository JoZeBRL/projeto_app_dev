<script setup lang="ts">
withDefaults(defineProps<{ 
  compact?: boolean;
  variant?: 'light' | 'dark';
}>(), {
  compact: false,
  variant: 'dark'
});
</script>

<template>
  <div class="flex items-center gap-3 group select-none">
    <div 
      class="rounded-[12px] flex items-center justify-center transition-all duration-500 shadow-sm transition-all"
      :class="[
        compact ? 'w-10 h-10' : 'w-12 h-12',
        variant === 'dark' ? 'bg-black shadow-black/10' : 'bg-white shadow-white/10 border border-gray-100'
      ]"
    >
      <span 
        class="font-black italic tracking-tighter" 
        :class="[
          compact ? 'text-2xl' : 'text-3xl',
          variant === 'dark' ? 'text-white' : 'text-black'
        ]"
      >C.</span>
    </div>
    <div v-if="!compact" class="flex flex-col -space-y-1">
      <span 
        class="font-black text-xl italic uppercase tracking-tighter transition-colors"
        :class="variant === 'dark' ? 'text-white group-hover:text-emerald-500' : 'text-black group-hover:text-emerald-500'"
      >
        Corretiza
      </span>
      <span class="text-[8px] font-bold text-gray-400 uppercase tracking-[0.4em] ml-1">
        Elite Real Estate
      </span>
    </div>
  </div>
</template>
