<script setup lang="ts">
defineProps<{ compact?: boolean }>();
</script>

<template>
  <div class="flex items-center gap-3 group select-none">
    <div 
      class="bg-white rounded-[12px] flex items-center justify-center transition-all duration-500 shadow-[0_0_20px_rgba(255,255,255,0.1)] group-hover:shadow-[0_0_30px_rgba(255,255,255,0.2)]"
      :class="compact ? 'w-10 h-10' : 'w-12 h-12'"
    >
      <span class="text-black font-black italic tracking-tighter" :class="compact ? 'text-2xl' : 'text-3xl'">C.</span>
    </div>
    <div v-if="!compact" class="flex flex-col -space-y-1 animate-fade-in">
      <span class="text-white font-black text-xl italic uppercase tracking-tighter transition-colors group-hover:text-gray-200">
        Corretiza
      </span>
      <span class="text-[8px] font-bold text-gray-500 uppercase tracking-[0.4em] ml-1">
        Elite Real Estate
      </span>
    </div>
  </div>
</template>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateX(-10px); }
  to { opacity: 1; transform: translateX(0); }
}
</style>
