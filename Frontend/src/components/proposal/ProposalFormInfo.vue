<script setup>
const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])
</script>

<template>
    <v-card class="!rounded-[40px] pa-8 bg-[#14161C] border border-white/5 text-white">
        <div class="flex items-center gap-4 mb-8">
            <div class="w-12 h-12 rounded-full bg-emerald-500/10 flex items-center justify-center">
                <v-icon icon="mdi-account" color="emerald"></v-icon>
            </div>
            <h2 class="text-xl font-black uppercase italic">Dados do Proponente</h2>
        </div>

        <v-row>
            <v-col cols="12" md="6">
                <label class="text-[10px] font-black uppercase text-gray-500 mb-2 block">Nome Completo</label>
                <v-text-field v-model="props.modelValue.nome" variant="solo-filled" flat bg-color="#0A0B0E"
                    class="!rounded-xl" placeholder="Ex: João Silva"></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
                <label class="text-[10px] font-black uppercase text-gray-500 mb-2 block">CPF / CNPJ</label>
                <v-text-field v-model="props.modelValue.cpf" variant="solo-filled" flat bg-color="#0A0B0E"
                    class="!rounded-xl" placeholder="000.000.000-00"></v-text-field>
            </v-col>
        </v-row>
    </v-card>
</template>