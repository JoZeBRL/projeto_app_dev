<script setup>
const props = defineProps({
    modelValue: Boolean,
    propertyTitle: { type: String, default: 'este imóvel' }
})

const emit = defineEmits(['update:modelValue', 'activate'])

const plans = [
    {
        id: 'silver',
        name: 'Destaque Prata',
        price: '49,90',
        duration: '7 dias',
        features: ['Prioridade média nas buscas', 'Selo visual de Destaque', 'Relatório semanal'],
        icon: 'mdi-trending-up',
        color: 'text-gray-400',
        popular: false
    },
    {
        id: 'gold',
        name: 'Destaque Ouro',
        price: '89,90',
        duration: '15 dias',
        features: ['Alta prioridade (Top 5)', 'Selo Premium Ouro', 'Push inteligente regional', 'Suporte dedicado'],
        icon: 'mdi-lightning-bolt',
        color: 'text-emerald-400',
        popular: true
    },
    {
        id: 'diamond',
        name: 'Destaque Diamante',
        price: '149,90',
        duration: '30 dias',
        features: ['Topo absoluto (Fixado)', 'Selo Diamante Animado', 'Newsletter semanal', 'Acesso prioritário'],
        icon: 'mdi-star',
        color: 'text-blue-400',
        popular: false
    }
]

const handleActivate = (plan) => {
    emit('activate', plan)
    emit('update:modelValue', false)
}
</script>

<template>
    <v-dialog :model-value="props.modelValue" @update:model-value="emit('update:modelValue', $event)" max-width="1000"
        transition="dialog-bottom-transition" scrollable>
        <div class="bg-[#0A0B0E] text-white rounded-[40px] overflow-hidden border border-white/5 shadow-2xl">
            <div class="p-8 md:p-12 flex justify-between items-start">
                <div>
                    <h2 class="text-4xl font-black uppercase italic tracking-tighter mb-2">Promover Imóvel</h2>
                    <p class="text-gray-500 font-bold text-xs uppercase tracking-widest">
                        Destaque <span class="text-white">{{ propertyTitle }}</span> na rede B2B
                    </p>
                </div>
                <v-btn icon="mdi-close" variant="tonal" color="white" density="comfortable" class="!rounded-full"
                    @click="emit('update:modelValue', false)"></v-btn>
            </div>

            <div class="px-8 md:px-12 pb-12">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div v-for="plan in plans" :key="plan.id" :class="[
                        'relative rounded-[32px] p-8 border-2 transition-all duration-500 flex flex-col',
                        plan.popular
                            ? 'border-emerald-500/50 bg-emerald-500/5 shadow-[0_0_40px_-10px_rgba(16,185,129,0.2)]'
                            : 'border-white/5 bg-white/[0.02] hover:border-white/10'
                    ]">
                        <div v-if="plan.popular"
                            class="absolute -top-4 left-1/2 -translate-x-1/2 bg-emerald-500 text-black text-[10px] font-black uppercase px-4 py-1 rounded-full">
                            Recomendado
                        </div>

                        <v-icon :icon="plan.icon" :class="['mb-6', plan.color]" size="32"></v-icon>

                        <div class="mb-6">
                            <h3 class="text-xl font-black uppercase italic">{{ plan.name }}</h3>
                            <p class="text-[10px] font-black text-gray-500 uppercase tracking-widest">{{ plan.duration
                                }}</p>
                        </div>

                        <div class="flex items-baseline gap-1 mb-8">
                            <span class="text-xs font-black text-gray-500 uppercase">R$</span>
                            <span class="text-4xl font-black">{{ plan.price }}</span>
                        </div>

                        <div class="flex-1 space-y-4 mb-10">
                            <div v-for="(feat, i) in plan.features" :key="i" class="flex items-start gap-3">
                                <v-icon icon="mdi-check-circle" color="emerald-darken-1" size="14"
                                    class="mt-1"></v-icon>
                                <span class="text-xs font-bold text-gray-400 leading-snug">{{ feat }}</span>
                            </div>
                        </div>

                        <v-btn block :color="plan.popular ? 'emerald' : 'white'"
                            :variant="plan.popular ? 'elevated' : 'tonal'" height="56"
                            class="!rounded-full !font-black !text-[12px] !uppercase !tracking-widest"
                            @click="handleActivate(plan)">
                            Ativar Agora
                        </v-btn>
                    </div>
                </div>

                <div
                    class="mt-10 p-6 rounded-[32px] bg-white/[0.03] border border-white/5 flex flex-col md:flex-row items-center gap-6">
                    <div class="w-16 h-16 rounded-2xl bg-emerald-500/10 flex items-center justify-center flex-shrink-0">
                        <v-icon icon="mdi-trending-up" color="emerald" size="28"></v-icon>
                    </div>
                    <div>
                        <h4 class="text-sm font-black uppercase italic mb-1">Impacto Imediato</h4>
                        <p class="text-xs font-bold text-gray-500 leading-relaxed uppercase tracking-tight">
                            Imóveis promovidos recebem até <span class="text-emerald-400 font-black">4x mais
                                cliques</span>.
                            A visibilidade é priorizada para corretores com alto índice de fechamento.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </v-dialog>
</template>

<style scoped>
:deep(.v-overlay__content) {
    border-radius: 40px !important;
}
</style>