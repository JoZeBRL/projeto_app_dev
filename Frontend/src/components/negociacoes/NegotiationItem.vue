<script setup lang="ts">
// Removidos Lucide imports.

interface Props {
    title: string;
    date: string;
    status: string;
    isActive?: boolean;
}

defineProps<Props>();
defineEmits(['click']);
</script>

<template>
    <div @click="$emit('click')"
        class="group relative w-full h-[64px] bg-zinc-900/40 backdrop-blur-xl border border-white/5 border-solid rounded-[20px] cursor-pointer hover:border-emerald-500/50 transition-all duration-300 overflow-hidden mb-3">
        <div class="flex items-center justify-between px-6 h-full w-full">
            <div class="flex items-center gap-4 flex-1">
                <div class="h-2 w-2 rounded-full bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.5)]"></div>
                <h4 class="font-black text-[15px] text-white uppercase tracking-tight truncate">
                    {{ title }}
                </h4>
            </div>

            <div class="flex items-center gap-8">
                <span class="font-black text-[12px] text-zinc-500 uppercase tracking-widest">
                    {{ date }}
                </span>

                <div class="px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-tighter"
                    :class="status === 'aceita' || status === 'finalizada' ? 'bg-emerald-500/10 text-emerald-500 border border-emerald-500/20' : 'bg-orange-500/10 text-orange-500 border border-orange-500/20'">
                    {{ status === 'aceita' || status === 'finalizada' ? 'Concluída' : 'Em Análise' }}
                </div>

                <v-icon icon="mdi-chevron-down" class="text-zinc-600 group-hover:text-white transition-colors" />
            </div>
        </div>

        <div v-if="isActive"
            class="absolute inset-0 border-2 border-emerald-500/20 pointer-events-none rounded-[20px]" />
    </div>
</template>