<script setup>
const props = defineProps(['modelValue']);
const emit = defineEmits(['update:modelValue']);
</script>

<template>
    <div class="bg-[#111111] p-10 rounded-[40px] border border-white/5 shadow-inner">
        <h2 class="text-2xl font-black mb-8 flex items-center gap-3">
            <v-icon icon="mdi-map-marker-outline" color="green-accent-3"></v-icon>
            Dados Principais e Localização
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="md:col-span-2">
                <label class="text-xs font-black uppercase tracking-widest text-gray-500 ml-4 mb-2 block">Título do
                    Anúncio</label>
                <v-text-field v-model="modelValue.title" placeholder="Ex: Penthouse de Luxo com Vista Mar"
                    variant="solo-filled" flat rounded="pill" bg-color="#1A1A1A" class="font-medium"></v-text-field>
            </div>

            <v-select v-model="modelValue.propertyType" label="Tipo"
                :items="['Apartamento', 'Casa', 'Cobertura', 'Terreno']" variant="solo-filled" flat rounded="pill"
                bg-color="#1A1A1A"></v-select>

            <v-text-field v-model="modelValue.price" label="Valor de Venda (R$)" prefix="R$" variant="solo-filled" flat
                rounded="pill" bg-color="#1A1A1A"></v-text-field>

        </div>
    </div>
</template>