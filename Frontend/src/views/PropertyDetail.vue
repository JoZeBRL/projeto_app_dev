<script setup>
import { ref, onMounted } from 'vue'
import ReserveModal from '@/components/property/ReserveModal.vue'

// Mock Data (Integrar com API posteriormente)
const property = ref({
    id: 1,
    title: 'Casa em Condomínio no Efapi',
    address: 'Rua das Palmeiras, 234 - Chapecó - SC',
    price: 'R$ 850.000',
    area: '180m²',
    bedrooms: 3,
    suites: 2,
    bathrooms: 2,
    parking: 2,
    description: 'Elegante casa em condomínio fechado com área gourmet completa...',
    images: [
        'https://images.unsplash.com/photo-1706808849777-96e0d7be3bb7?q=80&w=1080',
        'https://images.unsplash.com/photo-1639059851892-95c80412298c?q=80&w=1080'
    ],
    amenities: ['Piscina', 'Churrasqueira', 'Portaria 24h'],
    extras: ['Cozinha planejada', 'Aquecimento solar']
})

const currentImageIndex = ref(0)
const isFavorite = ref(false)
const showReserveModal = ref(false)
const showSuccessModal = ref(false)

const nextImage = () => {
    currentImageIndex.value = (currentImageIndex.value + 1) % property.value.images.length
}

const prevImage = () => {
    currentImageIndex.value = (currentImageIndex.value - 1 + property.value.images.length) % property.value.images.length
}

const onReserveConfirm = (data) => {
    console.log('Reserva solicitada:', data)
    showReserveModal.value = false
    showSuccessModal.value = true
}
</script>

<template>
    <v-container fluid class="pa-0 bg-[#0A0B0E] min-h-screen">
        <div class="relative h-[60vh] w-full overflow-hidden">
            <v-img :src="property.images[currentImageIndex]" cover class="h-full w-full transition-all duration-700">
                <div class="absolute inset-0 bg-gradient-to-t from-[#0A0B0E] to-transparent"></div>
            </v-img>

            <div class="absolute inset-0 flex items-center justify-between px-6">
                <v-btn icon="mdi-chevron-left" variant="tonal" color="white" @click="prevImage"></v-btn>
                <v-btn icon="mdi-chevron-right" variant="tonal" color="white" @click="nextImage"></v-btn>
            </div>
        </div>

        <v-row class="max-w-[1400px] mx-auto mt-[-100px] relative px-6 pb-12">
            <v-col cols="12" lg="8">
                <v-card class="!rounded-[40px] border border-white/5 pa-8 bg-[#14161C]/80 backdrop-blur-xl text-white">
                    <div class="flex justify-between items-start mb-6">
                        <div>
                            <h1 class="text-4xl font-black uppercase italic tracking-tighter mb-2">{{ property.title }}
                            </h1>
                            <p class="text-gray-400 flex items-center gap-2">
                                <v-icon icon="mdi-map-marker" size="small"></v-icon> {{ property.address }}
                            </p>
                        </div>
                        <v-btn :icon="isFavorite ? 'mdi-heart' : 'mdi-heart-outline'"
                            :color="isFavorite ? 'red' : 'white'" variant="text"
                            @click="isFavorite = !isFavorite"></v-btn>
                    </div>

                    <v-divider class="border-white/10 mb-8"></v-divider>

                    <h3 class="text-xs font-black uppercase tracking-widest text-emerald-400 mb-4">Sobre o Imóvel</h3>
                    <p class="text-gray-400 leading-relaxed mb-8">{{ property.description }}</p>

                    <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                        <div v-for="(val, label) in { Área: property.area, Quartos: property.bedrooms, Suítes: property.suites, Vagas: property.parking }"
                            :key="label">
                            <p class="text-[10px] uppercase font-black text-gray-500 mb-1">{{ label }}</p>
                            <p class="text-xl font-black">{{ val }}</p>
                        </div>
                    </div>
                </v-card>
            </v-col>

            <v-col cols="12" lg="4">
                <v-card class="!rounded-[40px] border border-white/5 pa-8 bg-[#14161C] text-white sticky top-24">
                    <p class="text-[10px] uppercase font-black text-gray-500 mb-1">Valor de Venda</p>
                    <h2 class="text-4xl font-black mb-8">{{ property.price }}</h2>

                    <v-btn block height="64" color="emerald" class="!rounded-full !font-black mb-4"
                        @click="showReserveModal = true">
                        AGENDAR VISITA
                    </v-btn>

                    <v-btn block height="64" variant="outlined" color="white" class="!rounded-full !font-black">
                        FAZER PROPOSTA
                    </v-btn>
                </v-card>
            </v-col>
        </v-row>

        <ReserveModal v-model="showReserveModal" :property-title="property.title" @confirm="onReserveConfirm" />

        <v-dialog v-model="showSuccessModal" max-width="400">
            <v-card class="!rounded-[40px] pa-8 text-center bg-[#14161C] text-white border border-emerald-500/30">
                <v-icon icon="mdi-check-circle" color="emerald" size="64" class="mb-4"></v-icon>
                <h2 class="text-2xl font-black uppercase italic mb-2">Solicitado!</h2>
                <p class="text-gray-400 text-sm mb-6">Sua visita foi agendada. A construtora entrará em contato em
                    breve.</p>
                <v-btn block color="emerald" class="!rounded-full" @click="showSuccessModal = false">Entendido</v-btn>
            </v-card>
        </v-dialog>
    </v-container>
</template>