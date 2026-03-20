<script setup>
/**
 * CONFIRM MODAL - PADRÃO CORRETIZA PREMIUM BLACK
 * Componente versátil para diálogos de confirmação.
 */
import { computed } from 'vue';

const props = defineProps({
    modelValue: { type: Boolean, required: true },
    title: { type: String, default: 'Confirmar Ação' },
    message: { type: String, default: 'Deseja realmente prosseguir com esta operação?' },
    confirmText: { type: String, default: 'Confirmar' },
    cancelText: { type: String, default: 'Cancelar' },
    variant: { type: String, default: 'default' }, // 'default' | 'destructive'
    icon: { type: String, default: 'mdi-alert-circle-outline' }
});

const emit = defineEmits(['update:modelValue', 'confirm', 'cancel']);

const isOpen = computed({
    get: () => props.modelValue,
    set: (val) => emit('update:modelValue', val)
});

const handleConfirm = () => {
    emit('confirm');
    isOpen.value = false;
};

const handleCancel = () => {
    emit('cancel');
    isOpen.value = false;
};
</script>

<template>
    <v-dialog v-model="isOpen" max-width="480" overlay-color="#000" overlay-opacity="0.8" transition="scale-transition"
        persistent>
        <div class="bg-[#111111] border border-white/10 rounded-[40px] p-10 shadow-2xl relative overflow-hidden">
            <div v-if="variant === 'destructive'" class="absolute -top-24 -left-24 w-48 h-48 bg-red-600/10 blur-[80px]">
            </div>

            <div class="flex justify-center mb-6">
                <div :class="[
                    'w-20 h-20 rounded-full flex items-center justify-center border transition-all duration-500',
                    variant === 'destructive'
                        ? 'bg-red-500/10 border-red-500/20'
                        : 'bg-green-500/10 border-green-500/20'
                ]">
                    <v-icon :icon="icon" :color="variant === 'destructive' ? 'red-accent-3' : 'green-accent-3'"
                        size="40"></v-icon>
                </div>
            </div>

            <div class="text-center mb-10">
                <h3 class="text-2xl font-black text-white tracking-tighter mb-4">
                    {{ title }}
                </h3>
                <p class="text-gray-400 text-sm leading-relaxed px-4">
                    {{ message }}
                </p>
            </div>

            <div class="flex flex-col sm:flex-row gap-4">
                <v-btn @click="handleCancel" variant="tonal" color="grey-lighten-1" rounded="pill" size="x-large"
                    class="flex-1 font-black !capitalize !tracking-normal" flat>
                    {{ cancelText }}
                </v-btn>

                <v-btn @click="handleConfirm" :color="variant === 'destructive' ? 'red-accent-3' : 'white'" :class="[
                    'flex-1 font-black !capitalize !tracking-normal text-black',
                    variant === 'destructive' ? '!text-white' : '!text-black'
                ]" rounded="pill" size="x-large" flat>
                    {{ confirmText }}
                </v-btn>
            </div>
        </div>
    </v-dialog>
</template>

<style scoped>
/* Ajuste de profundidade do Vuetify para alinhar com o design Premium Black */
:deep(.v-overlay__content) {
    border-radius: 40px !important;
}
</style>