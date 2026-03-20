<script setup>
import { ref, reactive } from 'vue'
import ProposalFormInfo from '@/components/proposal/ProposalFormInfo.vue'
import ProposalFormPayment from '@/components/proposal/ProposalFormPayment.vue'

const props = defineProps({
    propertyTitle: { type: String, default: 'Imóvel Exemplo' },
    propertyId: Number
})

const isSubmitting = ref(false)
const proposalData = reactive({
    nome: '',
    cpf: '',
    valorProposta: '',
    entrada: '',
    parcelas: 12,
    observacoes: '',
    documentos: []
})

const submitProposal = async () => {
    isSubmitting.value = true
    // Simulação de envio
    setTimeout(() => {
        isSubmitting.value = false
        alert('Proposta enviada com sucesso!')
    }, 2000)
}
</script>

<template>
    <v-container class="pt-32 pb-16 bg-[#0A0B0E] min-h-screen" fluid>
        <div class="max-w-5xl mx-auto">
            <div class="mb-10 flex items-center justify-between">
                <div class="space-y-2">
                    <v-btn icon="mdi-arrow-left" variant="tonal" @click="$emit('back')" class="mb-4"></v-btn>
                    <h1 class="text-4xl font-black uppercase italic tracking-tighter text-white">
                        Criar <span class="text-emerald-400">Proposta</span>
                    </h1>
                    <p class="text-gray-500 font-medium">Imóvel: {{ propertyTitle }}</p>
                </div>
                <div class="hidden md:block">
                    <v-icon icon="mdi-handshake" size="80" color="white" class="opacity-10"></v-icon>
                </div>
            </div>

            <v-form @submit.prevent="submitProposal">
                <v-row>
                    <v-col cols="12" lg="8" class="space-y-6">
                        <ProposalFormInfo v-model="proposalData" />
                        <ProposalFormPayment v-model="proposalData" />
                    </v-col>

                    <v-col cols="12" lg="4">
                        <v-card
                            class="!rounded-[40px] pa-8 bg-[#14161C] border border-white/5 text-white sticky top-24">
                            <h3 class="text-xl font-black uppercase mb-6">Resumo da Oferta</h3>

                            <div class="space-y-4 mb-8">
                                <div class="flex justify-between border-b border-white/5 pb-2">
                                    <span class="text-gray-500 text-xs font-black uppercase">Valor Total</span>
                                    <span class="font-bold text-emerald-400">{{ proposalData.valorProposta || 'R$ 0,00'
                                        }}</span>
                                </div>
                                <div class="flex justify-between border-b border-white/5 pb-2">
                                    <span class="text-gray-500 text-xs font-black uppercase">Entrada</span>
                                    <span class="font-bold">{{ proposalData.entrada || 'R$ 0,00' }}</span>
                                </div>
                                <div class="flex justify-between">
                                    <span class="text-gray-500 text-xs font-black uppercase">Parcelamento</span>
                                    <span class="font-bold">{{ proposalData.parcelas }}x</span>
                                </div>
                            </div>

                            <v-btn block height="64" color="emerald" type="submit" :loading="isSubmitting"
                                class="!rounded-full !font-black mb-4 shadow-xl">
                                ENVIAR PROPOSTA
                            </v-btn>

                            <p class="text-[10px] text-center text-gray-600 uppercase font-bold px-4">
                                Ao enviar, você concorda com os termos de intermediação da Corretiza.
                            </p>
                        </v-card>
                    </v-col>
                </v-row>
            </v-form>
        </div>
    </v-container>
</template>