<script setup lang="ts">
import { ref, computed, watch } from 'vue'

interface ClientReservationData {
    clientName: string
    clientPhone: string
    clientEmail: string
    observations: string
    reservationDate: string
    visitTime: string
}

interface Props {
    modelValue: boolean
    propertyTitle: string
}

const props = defineProps<Props>()
const emit = defineEmits(['update:modelValue', 'reserve'])

// Estado do Formulário
const selectedDate = ref<string | null>(null)
const selectedTime = ref('')
const clientName = ref('')
const clientPhone = ref('')
const clientEmail = ref('')
const observations = ref('')
const isSubmitting = ref(false)

// Mock de reservas existentes (Poderia vir de uma Store/API)
const existingReservations = [
    { date: '2026-10-10', time: '10:00', broker: 'Carlos Mendes' },
    { date: '2026-10-10', time: '14:00', broker: 'Ana Paula' },
    { date: '2026-10-11', time: '09:00', broker: 'Roberto Silva' },
]

const availableTimeSlots = [
    '09:00', '10:00', '11:00', '12:00', '13:00',
    '14:00', '15:00', '16:00', '17:00', '18:00'
]

// Máscara de Telefone
const handlePhoneInput = (e: Event) => {
    const target = e.target as HTMLInputElement
    let value = target.value.replace(/\D/g, '')
    if (value.length > 11) value = value.slice(0, 11)

    if (value.length > 10) {
        value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7)}`
    } else if (value.length > 6) {
        value = `(${value.slice(0, 2)}) ${value.slice(2, 6)}-${value.slice(6)}`
    } else if (value.length > 2) {
        value = `(${value.slice(0, 2)}) ${value.slice(2)}`
    } else if (value.length > 0) {
        value = `(${value}`
    }
    clientPhone.value = value
}

const isTimeSlotOccupied = (time: string): boolean => {
    if (!selectedDate.value) return false
    return existingReservations.some(
        r => r.date === selectedDate.value && r.time === time
    )
}

const getBrokerForTime = (time: string): string | undefined => {
    if (!selectedDate.value) return undefined
    return existingReservations.find(
        r => r.date === selectedDate.value && r.time === time
    )?.broker
}

const isFormValid = computed(() => {
    return selectedDate.value && selectedTime.value && clientName.value.trim() && clientPhone.value.length >= 14
})

const close = () => {
    emit('update:modelValue', false)
}

const handleSubmit = async () => {
    if (!isFormValid.value) return

    isSubmitting.value = true
    try {
        const data: ClientReservationData = {
            clientName: clientName.value,
            clientPhone: clientPhone.value,
            clientEmail: clientEmail.value,
            observations: observations.value,
            reservationDate: selectedDate.value!,
            visitTime: selectedTime.value
        }

        emit('reserve', data)

        // Reset
        clientName.value = ''
        clientPhone.value = ''
        clientEmail.value = ''
        observations.value = ''
        selectedDate.value = null
        selectedTime.value = ''

        close()
    } finally {
        isSubmitting.value = false
    }
}
</script>

<template>
    <v-dialog :model-value="modelValue" @update:model-value="emit('update:modelValue', $event)" max-width="900px"
        class="premium-dialog">
        <v-card class="rounded-[40px] pa-8 overflow-hidden bg-white border-none shadow-2xl">
            <div class="flex items-center justify-between mb-8">
                <h3 class="text-2xl font-black text-black">Agendar Visita</h3>
                <v-btn icon="mdi-close" variant="text" class="rounded-full bg-gray-100" @click="close"></v-btn>
            </div>

            <div class="mb-8 p-5 bg-emerald-50 rounded-[25px] border border-emerald-100">
                <div class="flex items-start gap-4">
                    <v-icon color="emerald-darken-2" icon="mdi-office-building-marker" size="large" />
                    <div>
                        <p class="font-bold text-emerald-900">{{ propertyTitle }}</p>
                        <p class="text-sm text-emerald-700 mt-1">
                            Escolha data e horário disponível. Cada visita tem duração de 1 hora.
                        </p>
                    </div>
                </div>
            </div>

            <v-form @submit.prevent="handleSubmit">
                <div class="grid md:grid-cols-2 gap-8">

                    <div class="space-y-6">
                        <div class="input-group">
                            <label class="block text-sm font-black mb-2 px-2 uppercase tracking-wider">Nome do Cliente
                                *</label>
                            <input v-model="clientName" type="text" placeholder="Nome completo"
                                class="w-full h-14 px-6 rounded-[40px] border-2 border-gray-100 bg-gray-50 focus:border-black focus:bg-white transition-all outline-none"
                                required />
                        </div>

                        <div class="input-group">
                            <label class="block text-sm font-black mb-2 px-2 uppercase tracking-wider">Telefone
                                *</label>
                            <input :value="clientPhone" @input="handlePhoneInput" type="text"
                                placeholder="(49) 99999-9999"
                                class="w-full h-14 px-6 rounded-[40px] border-2 border-gray-100 bg-gray-50 focus:border-black focus:bg-white transition-all outline-none"
                                required />
                        </div>

                        <div class="input-group">
                            <label class="block text-sm font-black mb-2 px-2 uppercase tracking-wider">E-mail</label>
                            <input v-model="clientEmail" type="email" placeholder="cliente@email.com"
                                class="w-full h-14 px-6 rounded-[40px] border-2 border-gray-100 bg-gray-50 focus:border-black focus:bg-white transition-all outline-none" />
                        </div>
                    </div>

                    <div class="space-y-6">
                        <div class="input-group">
                            <label class="block text-sm font-black mb-2 px-2 uppercase tracking-wider">Data da Visita
                                *</label>
                            <v-text-field v-model="selectedDate" type="date" variant="outlined" rounded="pill"
                                color="black" hide-details class="premium-input-vue"
                                :min="new Date().toISOString().split('T')[0]"></v-text-field>
                        </div>

                        <div class="input-group">
                            <label class="block text-sm font-black mb-2 px-2 uppercase tracking-wider">Horários
                                *</label>
                            <v-select v-model="selectedTime" :items="availableTimeSlots" :disabled="!selectedDate"
                                placeholder="Selecione um horário" variant="outlined" rounded="pill" color="black"
                                hide-details class="premium-input-vue">
                                <template v-slot:item="{ props: itemProps, item }">
                                    <v-list-item v-bind="itemProps" :disabled="isTimeSlotOccupied(item.value)"
                                        :subtitle="isTimeSlotOccupied(item.value) ? `Ocupado: ${getBrokerForTime(item.value)}` : 'Disponível'"></v-list-item>
                                </template>
                            </v-select>
                        </div>

                        <div class="input-group">
                            <label
                                class="block text-sm font-black mb-2 px-2 uppercase tracking-wider">Observações</label>
                            <textarea v-model="observations" rows="2"
                                placeholder="Ex: Cliente tem interesse em financiamento..."
                                class="w-full p-4 px-6 rounded-[25px] border-2 border-gray-100 bg-gray-50 focus:border-black focus:bg-white transition-all outline-none resize-none"></textarea>
                        </div>
                    </div>
                </div>

                <div class="flex gap-4 mt-10">
                    <v-btn variant="tonal" height="56" rounded="pill" class="flex-1 font-black" color="grey-darken-3"
                        @click="close">
                        Cancelar
                    </v-btn>
                    <v-btn type="submit" height="56" rounded="pill" class="flex-1 font-black bg-black text-white"
                        :loading="isSubmitting" :disabled="!isFormValid">
                        Confirmar Reserva
                    </v-btn>
                </div>
            </v-form>
        </v-card>
    </v-dialog>
</template>

<style scoped>
.premium-input-vue :deep(.v-field__outline) {
    --v-field-border-width: 2px !important;
    --v-field-border-opacity: 1 !important;
    border-color: #F3F4F6 !important;
}

.premium-input-vue :deep(.v-field--focused .v-field__outline) {
    border-color: #000 !important;
}

.premium-dialog :deep(.v-overlay__scrim) {
    background: rgba(0, 0, 0, 0.8) !important;
    backdrop-filter: blur(4px);
}
</style>