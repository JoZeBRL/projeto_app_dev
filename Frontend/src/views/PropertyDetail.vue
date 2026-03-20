<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import ReserveModal from '@/components/property/ReserveModal.vue';

const router = useRouter();

// Mock Tipado (Preparado para a API)
const property = ref({
    id: 1,
    title: 'Edifício Horizon',
    type: 'Apartamento Alto Padrão',
    location: 'Centro, Chapecó - SC',
    price: 'R$ 1.250.000',
    commission: 'R$ 62.500 (5%)',
    description: 'Empreendimento com vista panorâmica e acabamento em mármore.',
    amenities: ['3 Suítes', '2 Vagas', 'Piscina Aquecida', 'Academia'],
});

const showReserveModal = ref(false);
</script>

<template>
    <div class="space-y-10 animate-fade-in">
        
        <div class="flex flex-col md:flex-row justify-between items-start gap-6">
            <div class="space-y-2">
                <button @click="router.back()" class="text-[10px] font-[900] uppercase tracking-[0.2em] text-[var(--label-color)] hover:text-[var(--text-color)] transition-colors flex items-center gap-2 mb-4">
                    <v-icon icon="mdi-arrow-left" size="14" /> Voltar para busca
                </button>
                <h1 class="text-5xl font-[900] uppercase tracking-tighter italic text-[var(--text-color)] leading-none">
                    {{ property.title }}
                </h1>
                <p class="text-[11px] font-[900] uppercase tracking-[0.3em] text-[var(--label-color)]">
                    <v-icon icon="mdi-map-marker-outline" size="14" class="mr-1" /> {{ property.location }}
                </p>
            </div>

            <div class="flex gap-4 w-full md:w-auto">
                <button class="w-14 h-14 rounded-full border border-[var(--glass-border)] flex items-center justify-center text-[var(--text-color)] hover:bg-[var(--glass-border)] transition-all">
                    <v-icon icon="mdi-heart-outline" size="24" />
                </button>
                <button @click="showReserveModal = true" class="flex-1 md:flex-none btn-premium !px-8">
                    RESERVAR AGORA
                </button>
            </div>
        </div>

        <div class="glass-container h-[400px] flex items-center justify-center border-[var(--glass-border)] relative overflow-hidden group">
            <div class="absolute inset-0 bg-zinc-800/20"></div>
            <v-icon icon="mdi-image-outline" size="48" class="text-[var(--label-color)] opacity-50 group-hover:scale-110 transition-transform duration-500" />
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div class="glass-container p-8 space-y-6 lg:col-span-1 border-emerald-500/20 bg-emerald-500/5">
                <div>
                    <p class="text-[10px] font-[900] uppercase tracking-[0.2em] text-[var(--label-color)] mb-1">Valor de Venda</p>
                    <p class="text-3xl font-[900] tracking-tighter italic text-[var(--text-color)]">{{ property.price }}</p>
                </div>
                <div class="h-px w-full bg-[var(--glass-border)]"></div>
                <div>
                    <p class="text-[10px] font-[900] uppercase tracking-[0.2em] text-emerald-600 mb-1">Comissão Estimada</p>
                    <p class="text-2xl font-[900] tracking-tighter italic text-emerald-500">{{ property.commission }}</p>
                </div>
            </div>

            <div class="glass-container p-8 lg:col-span-2 space-y-8">
                <div>
                    <h3 class="text-lg font-[900] uppercase tracking-widest text-[var(--text-color)] mb-4">Ficha Técnica</h3>
                    <p class="text-sm font-medium text-[var(--label-color)] leading-relaxed">{{ property.description }}</p>
                </div>
                
                <div class="flex flex-wrap gap-3">
                    <div v-for="amenity in property.amenities" :key="amenity" 
                        class="px-4 py-2 rounded-full border border-[var(--glass-border)] text-[10px] font-[900] uppercase tracking-widest text-[var(--text-color)]">
                        {{ amenity }}
                    </div>
                </div>
            </div>
        </div>

        <ReserveModal v-if="showReserveModal" @close="showReserveModal = false" :property="property" />
    </div>
</template>

<style scoped>
.animate-fade-in { animation: fadeIn 0.5s ease-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style>