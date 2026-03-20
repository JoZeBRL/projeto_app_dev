<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
    modelValue: { type: Boolean, required: true },
    clientInfo: {
        type: Object,
        default: () => ({ name: '', phone: '', email: '' })
    },
    initialDate: { type: String, default: '' },
    initialTime: { type: String, default: '' },
    initialObservations: { type: String, default: '' }
})

const emit = defineEmits(['update:modelValue', 'submit'])

const date = ref(props.initialDate)
const time = ref(props.initialTime)
const observations = ref(props.initialObservations)

// Sincronizar campos quando o modal abre ou as props iniciais mudam
watch(() => props.modelValue, (isOpen) => {
    if (isOpen) {
        date.ref = props.initialDate
        time.ref = props.initialTime
        observations.ref = props.initialObservations
    }
})

const close = () => {
    emit('update:modelValue', false)
}

const handleSubmit = () => {
    emit('submit', {
        date: date.value,
        time: time.value,
        observations: observations.value
    })
    close()
}
</script>

<template>
    <v-dialog :model-value="modelValue" @update:model-value="emit('update:modelValue', $event)" max-width="840"
        persistent transition="dialog-bottom-transition" class="rounded-[40px]">
        <v-card class="!rounded-[32px] overflow-hidden bg-white dark:bg-[#14161C] pa-2 md:pa-6">
            <div class="flex justify-between items-center p-6 mb-2">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 bg-gray-100 dark:bg-white/5 rounded-full flex items-center justify-center">
                        <v-icon icon="mdi-calendar-edit" color="white" size="24"></v-icon>
                    </div>
                    <div>
                        <h2
                            class="text-2xl font-black italic uppercase tracking-tighter text-[#14161C] dark:text-white leading-none">
                            Reagendar <span class="text-emerald-400">Visita</span>
                        </h2>
                    </div>
                </div>
                <v-btn icon="mdi-close" variant="text" color="grey-lighten-1" @click="close"></v-btn>
            </div>

            <v-divider class="opacity-10 mb-8 mx-6"></v-divider>

            <v-form @submit.prevent="handleSubmit" class="px-6 pb-8">
                <v-row>
                    <v-col cols="12" md="6" class="space-y-6">
                        <div class="flex items-center gap-2 text-gray-900 dark:text-white mb-4">
                            <v-icon icon="mdi-account-circle-outline" size="20"></v-icon>
                            <h3 class="text-lg font-black uppercase italic">Cliente</h3>
                        </div>

                        <div
                            class="bg-gray-50 dark:bg-[#0A0B0E] rounded-[24px] p-6 space-y-4 border border-gray-100 dark:border-white/5 shadow-inner">
                            <div class="flex items-center gap-3 text-gray-900 dark:text-white">
                                <v-icon icon="mdi-account" size="18" class="opacity-40"></v-icon>
                                <span class="text-md font-bold">{{ clientInfo.name }}</span>
                            </div>
                            <div class="flex items-center gap-3 text-gray-600 dark:text-gray-400">
                                <v-icon icon="mdi-phone" size="18" class="opacity-40"></v-icon>
                                <span class="text-sm">{{ clientInfo.phone }}</span>
                            </div>
                            <div class="flex items-center gap-3 text-gray-600 dark:text-gray-400">
                                <v-icon icon="mdi-email" size="18" class="opacity-40"></v-icon>
                                <span class="text-sm break-all">{{ clientInfo.email }}</span>
                            </div>
                        </div>

                        <div
                            class="flex items-start gap-3 p-4 bg-amber-50 dark:bg-amber-900/10 rounded-[20px] text-amber-800 dark:text-amber-200 text-xs border border-amber-200/20">
                            <v-icon icon="mdi-information" color="amber" size="18"></v-icon>
                            <p class="font-medium">Aguarde aprovação da construtora para confirmar a nova data
                                selecionada.</p>
                        </div>
                    </v-col>

                    <v-col cols="12" md="6" class="space-y-6">
                        <div class="flex items-center gap-2 text-gray-900 dark:text-white mb-4">
                            <v-icon icon="mdi-clock-outline" size="20"></v-icon>
                            <h3 class="text-lg font-black uppercase italic">Novo Horário</h3>
                        </div>

                        <v-row dense>
                            <v-col cols="6">
                                <p class="text-[10px] font-black uppercase text-gray-500 mb-2 ml-4">Data</p>
                                <v-text-field v-model="date" type="date" variant="solo-filled" flat
                                    density="comfortable" rounded="pill" bg-color="#0A0B0E" hide-details
                                    class="dark-input-custom"></v-text-field>
                            </v-col>
                            <v-col cols="6">
                                <p class="text-[10px] font-black uppercase text-gray-500 mb-2 ml-4">Horário</p>
                                <v-text-field v-model="time" type="time" variant="solo-filled" flat
                                    density="comfortable" rounded="pill" bg-color="#0A0B0E" hide-details
                                    class="dark-input-custom"></v-text-field>
                            </v-col>
                        </v-row>

                        <div class="mt-4">
                            <p class="text-[10px] font-black uppercase text-gray-500 mb-2 ml-4">Observações para o
                                cliente</p>
                            <v-textarea v-model="observations"
                                placeholder="Ex: Tivemos um imprevisto, podemos visitar neste novo horário?"
                                variant="solo-filled" flat bg-color="#0A0B0E" rounded="xl" rows="4" hide-details
                                class="dark-input-custom"></v-textarea>
                        </div>
                    </v-col>
                </v-row>

                <div
                    class="flex flex-col md:flex-row items-center justify-end gap-4 pt-10 mt-6 border-t border-white/5">
                    <v-btn variant="outlined" height="48"
                        class="w-full md:w-auto px-10 !rounded-full !font-black text-gray-400 border-white/10"
                        @click="close">
                        DESCARTAR
                    </v-btn>
                    <v-btn color="white" theme="dark" height="48"
                        class="w-full md:w-auto px-12 !rounded-full !font-black !text-black shadow-lg" type="submit">
                        CONFIRMAR REAGENDAMENTO
                    </v-btn>
                </div>
            </v-form>
        </v-card>
    </v-dialog>
</template>

<style scoped>
.dark-input-custom :deep(.v-field) {
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    transition: all 0.3s ease;
}

.dark-input-custom :deep(.v-field--focused) {
    border-color: #10b981 !important;
    /* emerald */
}
</style>