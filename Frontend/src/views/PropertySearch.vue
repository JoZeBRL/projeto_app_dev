<script setup>
import { ref, computed } from 'vue'
import PropertyCard from '@/components/search/PropertyCard.vue'
import PartnerCarousel from '@/components/common/PartnerCarousel.vue'

const searchQuery = ref('')
const selectedType = ref('todos')
const showFilters = ref(false)

// Mock de dados extraído do arquivo original
const properties = ref([
    {
        id: 1,
        title: 'Edifício Legacy - Meia Praia',
        address: 'Rua 234, Meia Praia, Itapema - SC',
        price: 'R$ 1.200.000',
        type: 'Apartamento',
        beds: 3,
        baths: 2,
        area: '120m²',
        image: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?q=80&w=800'
    },
    {
        id: 2,
        title: 'Casa Contemporânea - Efapi',
        address: 'Rua das Palmeiras, Chapecó - SC',
        price: 'R$ 850.000',
        type: 'Casa',
        beds: 4,
        baths: 3,
        area: '250m²',
        image: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=800'
    }
])

const filteredProperties = computed(() => {
    return properties.value.filter(p => {
        const matchesSearch = p.title.toLowerCase().includes(searchQuery.value.toLowerCase())
        const matchesType = selectedType.value === 'todos' || p.type === selectedType.value
        return matchesSearch && matchesType
    })
})
</script>

<template>
    <div class="min-h-screen bg-[#0A0B0E] text-white">
        <section class="relative pt-32 pb-20 px-6 bg-gradient-to-b from-black to-[#0A0B0E]">
            <div class="max-w-7xl mx-auto text-center space-y-8">
                <h1 class="text-5xl md:text-7xl font-black uppercase italic tracking-tighter leading-none">
                    Encontre seu próximo <span class="text-emerald-400">Investimento</span>
                </h1>

                <div
                    class="max-w-3xl mx-auto bg-[#14161C] border border-white/10 p-2 rounded-[40px] shadow-2xl flex flex-col md:flex-row gap-2">
                    <v-text-field v-model="searchQuery" placeholder="Cidade, bairro ou nome do empreendimento..."
                        variant="solo" flat hide-details class="flex-grow !rounded-full text-white"
                        prepend-inner-icon="mdi-magnify"></v-text-field>

                    <v-btn color="emerald" height="56" class="!rounded-full px-8 !font-black"
                        @click="showFilters = !showFilters">
                        FILTRAR
                    </v-btn>
                </div>
            </div>
        </section>

        <PartnerCarousel class="py-12 border-y border-white/5" />

        <main class="max-w-7xl mx-auto px-6 py-16">
            <div class="flex justify-between items-end mb-10">
                <div>
                    <p class="text-emerald-400 text-xs font-black uppercase tracking-widest mb-2">Resultados</p>
                    <h2 class="text-3xl font-black uppercase italic">Imóveis Disponíveis</h2>
                </div>
                <p class="text-gray-500 font-medium">{{ filteredProperties.length }} imóveis encontrados</p>
            </div>

            <v-row>
                <v-col v-for="property in filteredProperties" :key="property.id" cols="12" sm="6" lg="4">
                    <PropertyCard :property="property" />
                </v-col>
            </v-row>
        </main>
    </div>
</template>

<style scoped>
:deep(.v-field) {
    border-radius: 40px !important;
    background-color: transparent !important;
}
</style>