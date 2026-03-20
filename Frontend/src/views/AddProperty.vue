<script setup>
import { ref, reactive, computed } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import Sidebar from '@/components/navigation/Sidebar.vue';
import StepPropertyBasicInfo from '@/components/add-property/StepPropertyBasicInfo.vue';
import StepPropertyDetails from '@/components/add-property/StepPropertyDetails.vue';
import StepPropertyPhotos from '@/components/add-property/StepPropertyPhotos.vue';

const props = defineProps({
    userType: { type: String, default: 'broker' } // 'broker' ou 'construction'
});

const showPropertyTypeChoice = ref(props.userType === 'construction');

const formData = reactive({
    title: '',
    description: '',
    propertyType: 'apartamento',
    transactionType: 'venda',
    price: '',
    commission: '',
    address: '',
    neighborhood: '',
    city: 'Chapecó',
    state: 'SC',
    zipCode: '',
    area: '',
    bedrooms: '',
    bathrooms: '',
    parking: '',
    amenities: [],
    images: []
});

const handleSubmit = () => {
    console.log('Finalizando cadastro Premium Black:', formData);
    // Integração com API aqui
};
</script>

<template>
    <div class="min-h-screen bg-[#0A0A0A] text-white font-sans">
        <GlobalHeader />
        <Sidebar />

        <main class="max-w-5xl mx-auto px-6 pt-32 pb-20">
            <div class="mb-12">
                <h1 class="text-4xl font-black tracking-tighter mb-2">Novo Imóvel</h1>
                <p class="text-gray-400">Cadastre propriedades individuais com padrão de alta fidelidade.</p>
            </div>

            <div v-if="showPropertyTypeChoice" class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <button @click="showPropertyTypeChoice = false"
                    class="bg-[#141414] border border-white/5 p-10 rounded-[40px] hover:border-green-500/50 transition-all group text-left shadow-2xl">
                    <div
                        class="w-16 h-16 bg-green-500/10 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <v-icon icon="mdi-home-variant" color="green-accent-3" size="32"></v-icon>
                    </div>
                    <h3 class="text-2xl font-black mb-2 text-white">Unidade Individual</h3>
                    <p class="text-gray-500 text-sm">Ideal para casas ou revendas rápidas de apartamentos prontos.</p>
                </button>

                <button @click="$router.push('/add-development')"
                    class="bg-[#141414] border border-white/5 p-10 rounded-[40px] hover:border-blue-500/50 transition-all group text-left shadow-2xl">
                    <div
                        class="w-16 h-16 bg-blue-500/10 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <v-icon icon="mdi-office-building" color="blue-accent-3" size="32"></v-icon>
                    </div>
                    <h3 class="text-2xl font-black mb-2 text-white">Empreendimento</h3>
                    <p class="text-gray-500 text-sm">Prédios completos com múltiplas torres, plantas e tabelas.</p>
                </button>
            </div>

            <div v-else class="space-y-8">
                <StepPropertyBasicInfo v-model="formData" />
                <StepPropertyDetails v-model="formData" />
                <StepPropertyPhotos v-model="formData.images" />

                <div class="flex justify-end gap-4 pt-8">
                    <v-btn variant="text" color="grey-lighten-1" size="large" rounded="pill"
                        class="font-bold">Cancelar</v-btn>
                    <v-btn @click="handleSubmit" color="white" size="large" rounded="pill"
                        class="font-black px-10 text-black">
                        Publicar Imóvel
                    </v-btn>
                </div>
            </div>
        </main>
    </div>
</template>