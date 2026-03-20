<script setup lang="ts">
import { ref, watch } from 'vue';

interface Props {
    src?: string;
    alt?: string;
    className?: string;
    aspectRatio?: string;
}

const props = defineProps<Props>();

const didError = ref(false);
const ERROR_IMG_SRC = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODgiIGhlaWdodD0iODgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLW9wYWNpdHk9IjAuMSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIzLjciPjxyZWN0IHg9IjE2IiB5PSIxNiIgd2lkdGg9IjU2IiBoZWlnaHQ9IjU2IiByeD0iNiIvPjxwYXRoIGQ9Im0xNiA1OCAxNi0xOCAzMiAzMiIvPjxjaXJjbGUgY3g9IjUzIiBjeT0iMzUiIHI9IjciLz48L3N2Zz4=';

const handleError = () => {
    didError.value = true;
};

// Resetar erro se o SRC mudar (ex: navegação entre imóveis)
watch(() => props.src, () => {
    didError.value = false;
});
</script>

<template>
    <div :class="[
        'overflow-hidden relative flex items-center justify-center transition-all duration-500',
        didError ? 'bg-zinc-900/50 backdrop-blur-xl border border-white/10' : 'bg-zinc-800',
        className
    ]">
        <img v-if="!didError && src" :src="src" :alt="alt" class="w-full h-full object-cover" @error="handleError" />

        <div v-else class="flex flex-col items-center justify-center p-4">
            <img :src="ERROR_IMG_SRC" class="w-12 h-12 mb-2 opacity-20" alt="Erro" />
            <span v-if="didError" class="text-[8px] font-black uppercase tracking-[0.2em] text-white/20">
                Mídia Indisponível
            </span>
        </div>
    </div>
</template>