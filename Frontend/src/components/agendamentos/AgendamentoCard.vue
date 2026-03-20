<script setup>
const props = defineProps(['agendamento', 'userType']);
defineEmits(['open-history']);

const getStatusColor = (status) => {
    const map = {
        pendente: 'amber-accent-3',
        confirmado: 'green-accent-3',
        concluido: 'blue-accent-3',
        cancelado: 'red-accent-3'
    };
    return map[status] || 'grey';
};
</script>

<template>
    <div
        class="group bg-[#111111] border border-white/5 rounded-[40px] overflow-hidden hover:border-white/20 transition-all duration-500 shadow-2xl">
        <div class="flex flex-col md:flex-row">
            <div class="md:w-72 h-48 md:h-auto relative overflow-hidden">
                <v-img :src="agendamento.propertyImage" cover
                    class="h-full group-hover:scale-110 transition-transform duration-700"></v-img>
                <div class="absolute inset-0 bg-gradient-to-t from-[#111111] via-transparent to-transparent"></div>
            </div>

            <div class="flex-1 p-8 flex flex-col justify-between">
                <div>
                    <div class="flex justify-between items-start mb-4">
                        <div>
                            <h3 class="text-xl font-black mb-1">{{ agendamento.propertyTitle }}</h3>
                            <p class="text-gray-500 text-sm flex items-center gap-2">
                                <v-icon size="16" icon="mdi-map-marker-outline"></v-icon>
                                {{ agendamento.propertyAddress }}
                            </p>
                        </div>
                        <v-chip :color="getStatusColor(agendamento.status)" variant="tonal"
                            class="font-black uppercase text-[10px] px-4">
                            {{ agendamento.status }}
                        </v-chip>
                    </div>

                    <div class="grid grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
                        <div class="flex flex-col">
                            <span class="text-[10px] uppercase font-black text-gray-600 tracking-widest mb-1">
                                {{ userType === 'construction' ? 'Corretor' : 'Cliente' }}
                            </span>
                            <span class="font-bold">{{ userType === 'construction' ? agendamento.brokerName :
                                agendamento.clientName }}</span>
                        </div>
                        <div class="flex flex-col">
                            <span class="text-[10px] uppercase font-black text-gray-600 tracking-widest mb-1">Data da
                                Visita</span>
                            <span class="font-bold">{{ agendamento.visitDate }} às {{ agendamento.visitTime }}</span>
                        </div>
                    </div>
                </div>

                <div class="flex flex-wrap items-center gap-3 mt-8 pt-6 border-t border-white/5">
                    <v-btn @click="$emit('open-history', agendamento)" variant="tonal" color="white" rounded="pill"
                        class="font-black px-6" size="small">
                        Histórico
                    </v-btn>
                    <v-btn variant="tonal" color="grey" rounded="pill" class="font-black px-6" size="small">
                        Reagendar
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn v-if="userType === 'broker'" color="green-accent-3" rounded="pill"
                        class="font-black px-8 text-black" size="small">
                        Criar Proposta
                    </v-btn>
                </div>
            </div>
        </div>
    </div>
</template>