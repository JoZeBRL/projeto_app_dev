<script setup>
import { computed } from 'vue'

const props = defineProps({
    currentStep: {
        type: Number,
        default: 2 // 1: Proposta, 2: Documentos, 3: Contrato, 4: Concluído
    }
})

const steps = [
    { id: 1, label: 'Proposta', icon: 'mdi-handshake' },
    { id: 2, label: 'Documentos', icon: 'mdi-file-document-edit' },
    { id: 3, label: 'Contrato', icon: 'mdi-fountain-pen-tip' },
    { id: 4, label: 'Escritura', icon: 'mdi-home-check' }
]

const getStepStatus = (stepId) => {
    if (stepId < props.currentStep) return 'completed'
    if (stepId === props.currentStep) return 'active'
    return 'pending'
}
</script>

<template>
    <div class="w-full py-8 px-4 overflow-x-auto">
        <div class="flex items-center justify-between min-w-[600px] relative">

            <div class="absolute top-1/2 left-0 w-full h-[2px] bg-gray-100 -translate-y-1/2 z-0"></div>

            <div v-for="(step, index) in steps" :key="step.id" class="flex flex-col items-center relative z-10 flex-1">
                <div :class="[
                    'w-14 h-14 rounded-2xl flex items-center justify-center transition-all duration-500 border-2',
                    getStepStatus(step.id) === 'completed' ? 'bg-emerald-500 border-emerald-500 shadow-lg shadow-emerald-100' : '',
                    getStepStatus(step.id) === 'active' ? 'bg-black border-black shadow-xl shadow-black/20 scale-110' : '',
                    getStepStatus(step.id) === 'pending' ? 'bg-white border-gray-200 text-gray-300' : ''
                ]">
                    <v-icon :icon="step.icon" :color="getStepStatus(step.id) === 'pending' ? 'gray-lighten-2' : 'white'"
                        size="24"></v-icon>
                </div>

                <div class="mt-4 flex flex-col items-center">
                    <span :class="[
                        'text-[10px] font-black uppercase tracking-widest transition-colors',
                        getStepStatus(step.id) === 'active' ? 'text-black' : 'text-gray-400'
                    ]">
                        {{ step.label }}
                    </span>

                    <span v-if="getStepStatus(step.id) === 'completed'"
                        class="text-[9px] font-bold text-emerald-500 mt-1">
                        CONCLUÍDO
                    </span>
                    <span v-else-if="getStepStatus(step.id) === 'active'" class="text-[9px] font-bold text-black mt-1">
                        EM ANDAMENTO
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Garante que a linha de fundo não ultrapasse os limites visuais dos círculos extremos */
.relative::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 10%;
    right: 10%;
    height: 2px;
    background: inherit;
    z-index: -1;
}
</style>