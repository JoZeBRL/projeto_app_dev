<script setup lang="ts">
import { ref } from 'vue';
import {
    Plus, Trash2, Maximize2, Bed, Bath, Car,
    DollarSign, Percent, ImageIcon, Check
} from 'lucide-vue-next';

interface Plan {
    id: string;
    name: string;
    area: string | number;
    bedrooms: string | number;
    bathrooms: string | number;
    parking: string | number;
    basePrice: string | number;
    commission: string | number;
    features: string[];
    image: File | null;
}

const props = defineProps<{
    modelValue: {
        plans: Plan[]
    }
}>();

// Template para um novo modelo de planta
const createEmptyPlan = (): Plan => ({
    id: crypto.randomUUID(),
    name: '',
    area: '',
    bedrooms: '',
    bathrooms: '',
    parking: '',
    basePrice: '',
    commission: '',
    features: [],
    image: null
});

const addPlan = () => {
    props.modelValue.plans.push(createEmptyPlan());
};

const removePlan = (index: number) => {
    props.modelValue.plans.splice(index, 1);
};

// Se não houver nenhuma planta, inicia com uma
if (props.modelValue.plans.length === 0) {
    addPlan();
}
</script>

<template>
    <div class="space-y-8 animate-in fade-in slide-in-from-right-4 duration-500">
        <div class="flex items-center justify-between">
            <div>
                <h3 class="text-xl font-black text-gray-900 dark:text-white uppercase tracking-tighter">
                    Modelos de Plantas
                </h3>
                <p class="text-xs text-gray-500 font-medium">Cadastre as variações de unidades disponíveis</p>
            </div>
            <v-btn color="black" variant="flat" class="rounded-xl font-bold text-none px-6" @click="addPlan">
                <template v-slot:prepend>
                    <Plus class="w-4 h-4" />
                </template>
                Adicionar Planta
            </v-btn>
        </div>

        <div class="space-y-6">
            <v-expansion-panels variant="accordion"
                class="rounded-[32px] overflow-hidden border border-gray-100 dark:border-white/5">
                <v-expansion-panel v-for="(plan, index) in modelValue.plans" :key="plan.id" elevation="0"
                    class="bg-white dark:bg-gray-900 mb-2 border-b border-gray-50">
                    <v-expansion-panel-title class="py-6">
                        <template v-slot:default="{ expanded }">
                            <div class="flex items-center gap-4 w-full">
                                <div
                                    class="w-12 h-12 bg-gray-100 dark:bg-gray-800 rounded-2xl flex items-center justify-center">
                                    <ImageIcon class="w-6 h-6 text-gray-400" />
                                </div>
                                <div class="flex-1 text-left">
                                    <p
                                        class="text-sm font-black uppercase tracking-tight text-gray-900 dark:text-white">
                                        {{ plan.name || `Planta Modelo #${index + 1}` }}
                                    </p>
                                    <p class="text-[10px] font-bold text-gray-400 uppercase">
                                        {{ plan.area ? `${plan.area}m²` : 'Área não definida' }} •
                                        {{ Number(plan.bedrooms) || '0' }} Quartos
                                    </p>
                                </div>
                                <v-btn v-if="modelValue.plans.length > 1" icon variant="text" color="error" size="small"
                                    @click.stop="removePlan(index)">
                                    <Trash2 class="w-4 h-4" />
                                </v-btn>
                            </div>
                        </template>
                    </v-expansion-panel-title>

                    <v-expansion-panel-text class="pt-4 pb-8">
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <div class="md:col-span-3">
                                <v-text-field v-model="plan.name" label="Nome Comercial da Planta" variant="outlined"
                                    placeholder="Ex: Garden Loft, Duplex Master" class="font-bold" />
                            </div>

                            <v-text-field v-model="plan.area" label="Área Privativa (m²)" variant="outlined"
                                type="number" class="font-bold">
                                <template v-slot:prepend-inner>
                                    <Maximize2 class="w-4 h-4 mr-2 text-gray-400" />
                                </template>
                            </v-text-field>

                            <v-text-field v-model="plan.bedrooms" label="Dormitórios" variant="outlined" type="number"
                                class="font-bold">
                                <template v-slot:prepend-inner>
                                    <Bed class="w-4 h-4 mr-2 text-gray-400" />
                                </template>
                            </v-text-field>

                            <v-text-field v-model="plan.bathrooms" label="Suítes/Banheiros" variant="outlined"
                                type="number" class="font-bold">
                                <template v-slot:prepend-inner>
                                    <Bath class="w-4 h-4 mr-2 text-gray-400" />
                                </template>
                            </v-text-field>

                            <v-text-field v-model="plan.basePrice" label="Preço Inicial (R$)" variant="outlined"
                                prefix="R$" class="font-bold">
                                <template v-slot:prepend-inner>
                                    <DollarSign class="w-4 h-4 mr-2 text-gray-400" />
                                </template>
                            </v-text-field>

                            <v-text-field v-model="plan.commission" label="Comissão (%)" variant="outlined" suffix="%"
                                class="font-bold">
                                <template v-slot:prepend-inner>
                                    <Percent class="w-4 h-4 mr-2 text-gray-400" />
                                </template>
                            </v-text-field>

                            <v-text-field v-model="plan.parking" label="Vagas de Garagem" variant="outlined"
                                type="number" class="font-bold">
                                <template v-slot:prepend-inner>
                                    <Car class="w-4 h-4 mr-2 text-gray-400" />
                                </template>
                            </v-text-field>
                        </div>
                    </v-expansion-panel-text>
                </v-expansion-panel>
            </v-expansion-panels>
        </div>
    </div>
</template>

<style scoped>
:deep(.v-expansion-panel-title--active) {
    background-color: rgba(0, 0, 0, 0.02);
}

:deep(.v-expansion-panel) {
    border-radius: 24px !important;
    margin-bottom: 12px;
}
</style>