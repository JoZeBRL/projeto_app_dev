<script setup>
import { computed } from 'vue';

// Importação dos assets conforme o Figma (Caminhos simulados para a estrutura Vite)
const logos = [
    { src: '/assets/partners/bci.png', alt: "BCI" },
    { src: '/assets/partners/tgt.png', alt: "TGT" },
    { src: '/assets/partners/bellei.png', alt: "Bellei Salvador" },
    { src: '/assets/partners/famex.png', alt: "Famex" },
    { src: '/assets/partners/santa-maria.png', alt: "Santa Maria" },
    { src: '/assets/partners/nostra-casa.png', alt: "Nostra Casa" },
    { src: '/assets/partners/fiorini.png', alt: "Fiorini" },
    { src: '/assets/partners/pax.png', alt: "PAX" },
    { src: '/assets/partners/holder.png', alt: "Holder" },
    { src: '/assets/partners/jbw.png', alt: "JBW" }
];

// Duplicamos a lista para garantir que o scroll infinito não tenha espaços vazios
const doubledLogos = computed(() => [...logos, ...logos, ...logos]);
</script>

<template>
    <div class="w-full pt-10 pb-6 overflow-hidden bg-transparent">
        <div class="relative flex overflow-hidden group">
            <div class="flex gap-12 items-center animate-infinite-scroll group-hover:pause">
                <div v-for="(logo, index) in doubledLogos" :key="`${logo.alt}-${index}`"
                    class="flex items-center justify-center grayscale opacity-40 hover:grayscale-0 hover:opacity-100 transition-all duration-500 cursor-pointer px-4">
                    <img :src="logo.src" :alt="logo.alt"
                        class="h-8 md:h-10 w-auto min-w-[80px] max-w-[120px] object-contain filter drop-shadow-sm" />
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Animação de Scroll Infinito Pura (Alta Performance) */
@keyframes scroll {
    0% {
        transform: translateX(0);
    }

    100% {
        transform: translateX(-33.33%);
    }
}

.animate-infinite-scroll {
    display: flex;
    width: max-content;
    animation: scroll 40s linear infinite;
}

.pause {
    animation-play-state: paused;
}

/* Ajuste para telas menores */
@media (max-width: 768px) {
    .animate-infinite-scroll {
        animation-duration: 25s;
        /* Um pouco mais rápido no mobile para manter o dinamismo */
    }
}
</style>