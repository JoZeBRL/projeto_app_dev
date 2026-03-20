<script setup lang="ts">
import { Maximize, BedDouble, Bath, Car, Sparkles } from 'lucide-vue-next';

const props = defineProps<{ modelValue: any }>();

const availableAmenities = [
    "Piscina", "Academia", "Churrasqueira", "Salão de Festas", "Playground",
    "Quadra Esportiva", "Portaria 24h", "Elevador", "Sacada", "Varanda Gourmet",
    "Ar Condicionado", "Mobiliado", "Semi-mobiliado"
];

const toggleAmenity = (amenity: string) => {
    const index = props.modelValue.amenities.indexOf(amenity);
    if (index === -1) props.modelValue.amenities.push(amenity);
    else props.modelValue.amenities.splice(index, 1);
};
</script>

<template>
    <div class="bg-gray-50 dark:bg-white/5 p-8 md:p-12 rounded-[40px] space-y-10">
        <div class="flex items-center gap-3">
            <div class="w-2 h-8 bg-green-600 rounded-full"></div>
            <h2 class="text-2xl font-black uppercase tracking-tighter">Características</h2>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
            <v-text-field v-model="modelValue.features.area" label="Área (m²)" variant="outlined" class="font-black">
                <template v-slot:prepend-inner>
                    <Maximize class="w-4 h-4 text-gray-400" />
                </template>
            </v-text-field>

            <v-text-field v-model="modelValue.features.bedrooms" label="Quartos" variant="outlined" type="number"
                class="font-black">
                <template v-slot:prepend-inner>
                    <BedDouble class="w-4 h-4 text-gray-400" />
                </template>
            </v-text-field>

            <v-text-field v-model="modelValue.features.bathrooms" label="Banheiros" variant="outlined" type="number"
                class="font-black">
                <template v-slot:prepend-inner>
                    <Bath class="w-4 h-4 text-gray-400" />
                </template>
            </v-text-field>

            <v-text-field v-model="modelValue.features.parking" label="Vagas" variant="outlined" type="number"
                class="font-black">
                <template v-slot:prepend-inner>
                    <Car class="w-4 h-4 text-gray-400" />
                </template>
            </v-text-field>
        </div>

        <div class="space-y-6">
            <div class="flex items-center gap-2">
                <Sparkles class="w-4 h-4 text-amber-500" />
                <span class="text-xs font-black uppercase tracking-widest text-gray-400">Comodidades e
                    Diferenciais</span>
            </div>

            <div class="flex flex-wrap gap-3">
                <button v-for="item in availableAmenities" :key="item" type="button" @click="toggleAmenity(item)"
                    :class="[
                        'px-6 py-3 rounded-2xl border-2 font-bold text-xs uppercase tracking-wider transition-all duration-300',
                        modelValue.amenities.includes(item)
                            ? 'border-green-600 bg-green-600 text-white shadow-lg shadow-green-900/20 scale-105'
                            : 'border-gray-200 dark:border-white/10 bg-white dark:bg-black text-gray-500 hover:border-gray-400'
                    ]">
                    {{ item }}
                </button>
            </div>
        </div>

        <v-textarea v-model="modelValue.description" label="Descrição do Imóvel" variant="outlined" rows="4"
            placeholder="Destaque os pontos fortes, sol da manhã, vista, acabamentos..." class="font-bold" />
    </div>
</template>