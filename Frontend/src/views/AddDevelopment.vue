<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { ArrowLeft, Sparkles, Check } from 'lucide-vue-next';
import StepGeneralInfo from '@/components/add-development/StepGeneralInfo.vue';
import StepFloorPlans from '@/components/add-development/StepFloorPlans.vue';
import StepUnits from '@/components/add-development/StepUnits.vue';

const router = useRouter();
const currentStep = ref(1);

// Estado Global do Formulário (Baseado na interface do arquivo original)
const formData = ref({
    name: '',
    location: '',
    description: '',
    category: 'Residencial',
    status: 'Lancamento',
    images: [] as File[],
    features: [] as string[],
    plans: [] as any[],
    units: [] as any[]
});

const steps = [
    { title: 'Geral', icon: 'mdi-office-building-cog' },
    { title: 'Plantas', icon: 'mdi-layers-triple' },
    { title: 'Unidades', icon: 'mdi-table-large' }
];

const handleNext = () => { if (currentStep.value < 3) currentStep.value++; };
const handleBack = () => { if (currentStep.value > 1) currentStep.value--; else router.back(); };
</script>

<template>
    <div class="min-h-screen bg-[#F9FAFB] dark:bg-gray-950 pb-20">
        <header
            class="sticky top-0 z-50 bg-white/80 dark:bg-gray-900/80 backdrop-blur-xl border-b border-gray-100 dark:border-white/5 p-4">
            <div class="max-w-5xl mx-auto flex items-center justify-between">
                <div class="flex items-center gap-4">
                    <v-btn icon variant="text" @click="handleBack" class="rounded-xl">
                        <ArrowLeft class="w-5 h-5" />
                    </v-btn>
                    <div>
                        <h1 class="text-xl font-black text-gray-900 dark:text-white tracking-tight uppercase">
                            Novo Empreendimento
                        </h1>
                        <p
                            class="text-[10px] font-bold text-green-600 uppercase tracking-widest flex items-center gap-1">
                            <Sparkles class="w-3 h-3 text-green-500" /> Gestão de Portfólio 2026
                        </p>
                    </div>
                </div>

                <div class="hidden md:flex gap-2">
                    <v-btn variant="tonal" class="rounded-full font-bold text-none" color="grey">Salvar Rascunho</v-btn>
                </div>
            </div>
        </header>

        <main class="max-w-4xl mx-auto p-6 mt-6">
            <div class="flex justify-between mb-10 px-4 relative">
                <div class="absolute top-5 left-0 w-full h-[2px] bg-gray-200 dark:bg-gray-800 z-0"></div>
                <div v-for="(step, i) in steps" :key="i" class="relative z-10 flex flex-col items-center gap-3">
                    <div :class="[
                        'w-10 h-10 rounded-2xl flex items-center justify-center transition-all duration-500 border-4',
                        currentStep > i + 1 ? 'bg-green-600 border-green-100 text-white' :
                            currentStep === i + 1 ? 'bg-black border-gray-100 text-white scale-110 shadow-xl' : 'bg-gray-100 border-white text-gray-400'
                    ]">
                        <Check v-if="currentStep > i + 1" class="w-5 h-5" />
                        <span v-else class="font-black text-sm">{{ i + 1 }}</span>
                    </div>
                    <span
                        :class="['text-[11px] font-black uppercase tracking-tighter', currentStep >= i + 1 ? 'text-black' : 'text-gray-400']">
                        {{ step.title }}
                    </span>
                </div>
            </div>

            <v-card class="rounded-[40px] border-none shadow-2xl shadow-gray-200/50 dark:shadow-none overflow-visible">
                <div class="p-8 md:p-12">
                    <v-window v-model="currentStep">
                        <v-window-item :value="1">
                            <StepGeneralInfo v-model="formData" />
                        </v-window-item>

                        <v-window-item :value="2">
                            <StepFloorPlans v-model="formData" />
                        </v-window-item>

                        <v-window-item :value="3">
                            <StepUnits v-model="formData" />
                        </v-window-item>
                    </v-window>

                    <div
                        class="flex items-center justify-between mt-12 pt-8 border-t border-gray-50 dark:border-white/5">
                        <v-btn variant="text" size="large" class="rounded-full px-8 font-bold text-none"
                            @click="handleBack">
                            {{ currentStep === 1 ? 'Cancelar' : 'Voltar' }}
                        </v-btn>

                        <v-btn color="black" size="x-large" class="rounded-full px-12 font-bold text-none shadow-xl"
                            @click="handleNext">
                            {{ currentStep === 3 ? 'Finalizar e Publicar' : 'Próxima Etapa' }}
                        </v-btn>
                    </div>
                </div>
            </v-card>
        </main>
    </div>
</template>