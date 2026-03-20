<script setup>
const props = defineProps({
    proposal: {
        type: Object,
        default: () => ({
            totalValue: 'R$ 1.250.000,00',
            entry: 'R$ 250.000,00',
            installments: '36x R$ 15.277,77',
            balloons: '3x R$ 150.000,00 (Anuais)',
            conditions: 'Correção pelo INCC-M até a entrega.',
            includedItems: ['Vaga extra', 'Churrasqueira gourmet', 'Automação básica']
        })
    }
})
</script>

<template>
    <div class="bg-gray-50 rounded-[40px] p-8 border border-gray-100 h-full">
        <div class="flex items-center gap-2 mb-6">
            <v-icon icon="mdi-calculator" color="black" size="small"></v-icon>
            <h3 class="text-sm font-black uppercase tracking-widest text-black">Resumo da Proposta</h3>
        </div>

        <div class="mb-8">
            <span class="text-xs font-bold text-gray-400 uppercase tracking-tighter">Valor Total do Imóvel</span>
            <div class="text-3xl font-black text-black leading-none mt-1">{{ proposal.totalValue }}</div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div class="space-y-1">
                <span class="text-[10px] font-black text-gray-400 uppercase">Entrada / Sinal</span>
                <p class="font-bold text-black">{{ proposal.entry }}</p>
            </div>
            <div class="space-y-1">
                <span class="text-[10px] font-black text-gray-400 uppercase">Parcelamento Mensal</span>
                <p class="font-bold text-black">{{ proposal.installments }}</p>
            </div>
            <div class="space-y-1">
                <span class="text-[10px] font-black text-gray-400 uppercase">Reforços / Balões</span>
                <p class="font-bold text-black">{{ proposal.balloons }}</p>
            </div>
            <div class="space-y-1">
                <span class="text-[10px] font-black text-gray-400 uppercase">Indexador / Reajuste</span>
                <p class="font-bold text-emerald-600 italic text-xs">{{ proposal.conditions }}</p>
            </div>
        </div>

        <div class="pt-6 border-t border-gray-200/50">
            <span class="text-[10px] font-black text-gray-400 uppercase mb-3 block">Diferenciais Negociados</span>
            <div class="flex flex-wrap gap-2">
                <span v-for="item in proposal.includedItems" :key="item"
                    class="bg-white border border-gray-200 px-3 py-1 rounded-full text-[10px] font-bold text-gray-600 shadow-sm">
                    + {{ item }}
                </span>
            </div>
        </div>
    </div>
</template>