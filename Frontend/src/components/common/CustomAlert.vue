<script setup>
/**
 * CUSTOM ALERT - PADRÃO CORRETIZA PREMIUM BLACK
 * Utilizado para feedbacks de sucesso, alertas informativos e confirmações de fluxo.
 */
import { computed } from 'vue';

const props = defineProps({
    modelValue: { type: Boolean, required: true },
    title: { type: String, default: 'Sucesso!' },
    message: { type: String, default: 'Operação realizada com êxito.' },
    confirmText: { type: String, default: 'OK' },
    cancelText: { type: String, default: 'Cancelar' },
    confirmVariant: { type: String, default: 'primary' }, // 'primary' | 'success'
    hideCancel: { type: Boolean, default: false }
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
    <v-dialog v-model="isOpen" max-width="440" transition="scale-transition" persistent>
        <div class="bg-[#111111] border border-white/10 rounded-[40px] p-8 relative overflow-hidden shadow-2xl">

            <button @click="handleCancel"
                class="absolute top-6 right-6 text-gray-500 hover:text-white transition-colors">
                <v-icon icon="mdi-close" size="24"></v-icon>
            </button>

            <div class="flex justify-center mb-6 mt-4">
                <div class="relative flex items-center justify-center">
                    <div class="absolute w-24 h-24 bg-green-500/20 blur-2xl rounded-full"></div>

                    <div
                        class="w-20 h-20 rounded-full border-2 border-green-500/30 flex items-center justify-center bg-[#111111] relative z-10">
                        <v-icon icon="mdi-check-bold" color="green-accent-3" size="40"></v-icon>
                    </div>
                </div>
            </div>

            <div class="text-center space-y-3 mb-10">
                <h3 class="text-2xl font-black text-white tracking-tighter">
                    {{ title }}
                </h3>
                <p class="text-gray-400 text-sm leading-relaxed px-2 font-medium">
                    {{ message }}
                </p>
            </div>

            <div class="flex gap-3">
                <v-btn v-if="!hideCancel" @click="handleCancel" variant="outlined" color="grey-darken-3" rounded="pill"
                    size="x-large"
                    class="flex-1 !border-white/10 !text-gray-400 font-black !capitalize !tracking-normal" flat>
                    {{ cancelText }}
                </v-btn>

                <v-btn @click="handleConfirm" :color="confirmVariant === 'success' ? 'green-accent-4' : 'white'" :class="[
                    'flex-1 font-black !capitalize !tracking-normal',
                    confirmVariant === 'success' ? '!text-white' : '!text-black'
                ]" rounded="pill" size="x-large" flat>
                    {{ confirmText }}
                </v-btn>
            </div>
        </div>
    </v-dialog>
</template>

<style scoped>
/* Garante que o container do Vuetify não sobrescreva o arredondamento de 40px */
:deep(.v-overlay__content) {
    border-radius: 40px !important;
}
</style>