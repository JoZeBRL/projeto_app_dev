<script setup lang="ts">
import { ref } from 'vue';

const emit = defineEmits(['search']);

const filters = ref({
    query: '',
    location: null,
    propertyType: null,
    transactionType: null
});

const locations = ['Chapecó - Centro', 'Chapecó - Efapi', 'Chapecó - Passo dos Fortes', 'Xanxerê'];
const propertyTypes = ['Apartamento', 'Casa', 'Terreno', 'Sala Comercial'];
const transactionTypes = ['Comprar', 'Alugar', 'Planta'];

const handleSearch = () => emit('search', filters.value);
</script>

<template>
    <div class="flex flex-col xl:flex-row items-center gap-3 w-full">
        <div class="flex-1 w-full">
            <v-text-field 
                v-model="filters.query" 
                placeholder="Buscar por empreendimento ou código..." 
                variant="solo-filled" 
                flat 
                hide-details 
                prepend-inner-icon="mdi-magnify"
                class="premium-input-field !rounded-[40px]" 
                @keyup.enter="handleSearch"
            />
        </div>
        
        <div class="w-full xl:w-[220px]">
            <v-select 
                v-model="filters.location" 
                :items="locations" 
                placeholder="Localização" 
                variant="solo-filled" 
                flat 
                hide-details 
                append-inner-icon="mdi-chevron-down"
                class="premium-input-field !rounded-[40px]" 
                @update:model-value="handleSearch"
            />
        </div>
        
        <div class="w-full xl:w-[220px]">
            <v-select 
                v-model="filters.propertyType" 
                :items="propertyTypes" 
                placeholder="Tipo de Imóvel" 
                variant="solo-filled" 
                flat 
                hide-details 
                append-inner-icon="mdi-chevron-down"
                class="premium-input-field !rounded-[40px]" 
                @update:model-value="handleSearch"
            />
        </div>

        <div class="w-full xl:w-[220px]">
            <v-select 
                v-model="filters.transactionType" 
                :items="transactionTypes" 
                placeholder="Negócio" 
                variant="solo-filled" 
                flat 
                hide-details 
                append-inner-icon="mdi-chevron-down"
                class="premium-input-field !rounded-[40px]" 
                @update:model-value="handleSearch"
            />
        </div>
    </div>
</template>