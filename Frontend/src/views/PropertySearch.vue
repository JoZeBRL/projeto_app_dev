<script setup lang="ts">
import { ref } from 'vue';
import SearchBar from '@/components/search/SearchBar.vue';
import PropertyCard from '@/components/search/PropertyCard.vue';

// Mock Data Tipado
const properties = ref([
    { id: 1, title: 'Edifício Horizon', type: 'Apartamento', location: 'Centro, Chapecó', price: 'R$ 1.250.000', beds: 3, baths: 2, parking: 2, image: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=400&q=80' },
    { id: 2, title: 'Residencial Viverti', type: 'Casa', location: 'Efapi, Chapecó', price: 'R$ 850.000', beds: 2, baths: 1, parking: 1, image: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=400&q=80' },
    { id: 3, title: 'Sky Tower', type: 'Apartamento', location: 'Passo dos Fortes, Chapecó', price: 'R$ 2.100.000', beds: 4, baths: 3, parking: 3, image: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=400&q=80' }
]);

const handleSearchUpdate = (filters: any) => {
    console.log('Filtros aplicados:', filters);
    // Lógica futura de API
};
</script>

<template>
    <div class="space-y-10 animate-fade-in">
        
        <div class="space-y-2">
            <h1 class="text-4xl font-[900] uppercase tracking-tighter italic text-[var(--text-color)]">
                Explorar <span class="text-emerald-500">Mercado</span>
            </h1>
            <p class="text-[10px] font-[900] uppercase tracking-[0.3em] text-[var(--label-color)]">
                Motor de busca B2B
            </p>
        </div>

        <div class="bg-[var(--bg-color)] rounded-[48px] shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-[var(--glass-border)] p-6 lg:p-8 transition-colors duration-500">
            <SearchBar @search="handleSearchUpdate" />
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
            <PropertyCard 
                v-for="prop in properties" 
                :key="prop.id" 
                v-bind="prop" 
                @click="$router.push({ name: 'PropertyDetail', params: { id: prop.id } })"
            />
        </div>

    </div>
</template>

<style scoped>
.animate-fade-in { animation: fadeIn 0.5s ease-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style>