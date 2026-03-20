<script setup lang="ts">
interface Props {
    title: string;
    description: string;
    icon: string; // Agora recebe apenas a string do MDI (ex: 'mdi-magnify')
    badge?: number;
}

defineProps<Props>();
</script>

<template>
    <button
        class="group glass-container relative p-10 hover:-translate-y-2 transition-all duration-500 text-left flex flex-col h-full overflow-hidden"
    >
        <div class="absolute -top-10 -right-10 w-32 h-32 bg-white/5 blur-3xl rounded-full group-hover:bg-emerald-500/10 transition-colors duration-700"></div>

        <div class="flex items-start justify-between mb-10 relative z-10">
            <div
                class="p-4 rounded-[24px] bg-white/5 border border-white/5 group-hover:bg-white group-hover:border-transparent transition-all duration-500"
            >
                <v-icon 
                    :icon="icon" 
                    size="28" 
                    class="text-zinc-400 group-hover:text-black transition-colors duration-500" 
                />
            </div>

            <span v-if="badge"
                class="bg-emerald-500 text-black text-[9px] font-black px-3 py-1 rounded-full shadow-[0_0_20px_rgba(16,185,129,0.3)] uppercase tracking-widest"
            >
                {{ badge }} Mensagens
            </span>
        </div>

        <div class="flex-1 relative z-10">
            <h3
                class="text-xl font-black uppercase tracking-tighter italic mb-3 text-white group-hover:text-emerald-400 transition-colors"
            >
                {{ title }}
            </h3>
            <p class="text-[10px] font-black text-zinc-500 uppercase tracking-[0.2em] leading-relaxed">
                {{ description }}
            </p>
        </div>

        <div class="mt-10 flex justify-end relative z-10">
            <div
                class="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center group-hover:bg-white transition-all duration-500 transform translate-x-4 opacity-0 group-hover:translate-x-0 group-hover:opacity-100"
            >
                <v-icon icon="mdi-chevron-right" size="24" class="text-black" />
            </div>
        </div>
    </button>
</template>