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
    <div class="flex flex-col lg:flex-row items-center gap-4 w-full">
        <div class="flex-1 w-full">
            <v-text-field 
                v-model="filters.query" 
                placeholder="Buscar propriedades..." 
                variant="solo" 
                flat 
                hide-details 
                prepend-inner-icon="mdi-magnify"
            />
        </div>
        
        <div class="w-full lg:w-[200px]">
            <v-select 
                v-model="filters.location" 
                :items="locations" 
                placeholder="Localização" 
                variant="solo" 
                flat 
                hide-details 
            />
        </div>
        
        <div class="w-full lg:w-[200px]">
            <v-select 
                v-model="filters.propertyType" 
                :items="propertyTypes" 
                placeholder="Tipo" 
                variant="solo" 
                flat 
                hide-details 
            />
        </div>
    </div>
</template>