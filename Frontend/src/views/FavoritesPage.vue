<script setup>
import { ref, computed } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import FavoriteCard from '@/components/favorites/FavoriteCard.vue';

const selectedList = ref('Todas as listas');
const isGridView = ref(true);

const propertyLists = [
    'Todas as listas', 'Casas de Luxo', 'Apartamentos Centro',
    'Famílias Grandes', 'Primeira Moradia', 'Imóveis Premium'
];

const favoriteProperties = ref([
    { id: 1, title: 'Casa em Condomínio no Efapi', price: 'R$ 850.000', location: 'Efapi, Chapecó - SC', type: 'Casa', area: '180m²', image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800', dateAdded: '15/12/2024', list: 'Casas de Luxo' },
    { id: 2, title: 'Apartamento Moderno Centro', price: 'R$ 420.000', location: 'Centro, Chapecó - SC', type: 'Apartamento', area: '95m²', image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800', dateAdded: '14/12/2024', list: 'Apartamentos Centro' },
    // ... demais dados omitidos para brevidade no exemplo
]);

const filteredProperties = computed(() => {
    if (selectedList.value === 'Todas as listas') return favoriteProperties.value;
    return favoriteProperties.value.filter(p => p.list === selectedList.value);
});

const removeFavorite = (id) => {
    favoriteProperties.value = favoriteProperties.value.filter(p => p.id !== id);
};
</script>

<template>
    <div class="min-h-screen bg-[#0A0A0A] text-white">
        <GlobalHeader />

        <main class="max-w-[1440px] mx-auto px-6 py-12 pt-32">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-12 gap-6">
                <div>
                    <h1 class="text-5xl font-black tracking-tighter mb-4">Meus Favoritos</h1>
                    <p class="text-gray-500 font-medium">Você tem {{ filteredProperties.length }} imóveis salvos em suas
                        listas.</p>
                </div>

                <div class="flex bg-white/5 p-1.5 rounded-full border border-white/10">
                    <button @click="isGridView = true"
                        :class="['p-3 rounded-full transition-all', isGridView ? 'bg-white text-black shadow-lg' : 'text-gray-500']">
                        <v-icon icon="mdi-view-grid" size="20"></v-icon>
                    </button>
                    <button @click="isGridView = false"
                        :class="['p-3 rounded-full transition-all', !isGridView ? 'bg-white text-black shadow-lg' : 'text-gray-500']">
                        <v-icon icon="mdi-format-list-bulleted" size="20"></v-icon>
                    </button>
                </div>
            </div>

            <div class="flex flex-wrap gap-3 mb-12">
                <v-btn v-for="list in propertyLists" :key="list" @click="selectedList = list"
                    :variant="selectedList === list ? 'flat' : 'outlined'"
                    :color="selectedList === list ? 'white' : 'grey-darken-3'" rounded="pill"
                    class="!font-black !capitalize !tracking-normal !px-6"
                    :class="{ 'text-black': selectedList === list, 'text-gray-400 !border-white/10': selectedList !== list }">
                    {{ list }}
                </v-btn>
            </div>

            <div v-if="filteredProperties.length > 0">
                <div
                    :class="[isGridView ? 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8' : 'flex flex-col gap-6']">
                    <FavoriteCard v-for="item in filteredProperties" :key="item.id" :property="item"
                        :is-grid="isGridView" @remove="removeFavorite" />
                </div>
            </div>

            <div v-else class="text-center py-24 bg-[#111111] rounded-[40px] border border-white/5">
                <v-icon icon="mdi-heart-broken" size="64" color="grey-darken-2" class="mb-6"></v-icon>
                <h3 class="text-2xl font-black mb-2">Sua lista está vazia</h3>
                <p class="text-gray-500 mb-8">Nenhum imóvel encontrado em "{{ selectedList }}"</p>
                <v-btn color="white" rounded="pill" class="!text-black !font-black !px-10" size="large">Explorar
                    Mercado</v-btn>
            </div>
        </main>
    </div>
</template>