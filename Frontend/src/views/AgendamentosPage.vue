<script setup>
import { ref, computed } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import Sidebar from '@/components/navigation/Sidebar.vue';
import AgendamentoCard from '@/components/agendamentos/AgendamentoCard.vue';
import HistoryDrawer from '@/components/agendamentos/HistoryDrawer.vue';

const props = defineProps({
    userType: { type: String, default: 'broker' }, // 'broker' | 'construction'
    userName: { type: String, default: 'Usuário' }
});

const filterStatus = ref('todos');
const selectedAgendamento = ref(null);
const isHistoryOpen = ref(false);

// Mock Data migrado
const agendamentos = ref([
    {
        id: 1,
        propertyTitle: 'Apartamento Vista Legacy',
        propertyAddress: 'Av. Getúlio Vargas, 123 - Centro, Chapecó',
        propertyImage: 'https://images.unsplash.com/photo-1720970228640-ac22842d782a?w=800&q=80',
        clientName: 'Maria Silva',
        visitDate: '2025-10-14',
        visitTime: '14:00',
        status: 'confirmado',
        brokerName: 'Carlos Mendes'
    },
    // ... demais itens do mock
]);

const filteredAgendamentos = computed(() => {
    if (filterStatus.value === 'todos') return agendamentos.value;
    return agendamentos.value.filter(ag => ag.status === filterStatus.value);
});

const openHistory = (agendamento) => {
    selectedAgendamento.value = agendamento;
    isHistoryOpen.value = true;
};
</script>

<template>
    <div class="min-h-screen bg-[#0A0A0A] text-white font-sans">
        <GlobalHeader />
        <Sidebar />

        <main class="max-w-7xl mx-auto px-6 pt-32 pb-20">
            <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
                <div>
                    <h1 class="text-4xl font-black tracking-tighter mb-2">
                        {{ userType === 'construction' ? 'Gestão de Visitas' : 'Meus Agendamentos' }}
                    </h1>
                    <p class="text-gray-400 max-w-xl">
                        Acompanhe o fluxo de visitas e interações em tempo real com padrão de alta fidelidade.
                    </p>
                </div>

                <div class="flex bg-[#141414] p-1.5 rounded-full border border-white/5 shadow-2xl">
                    <button @click="filterStatus = 'todos'"
                        :class="filterStatus === 'todos' ? 'bg-white text-black font-black' : 'text-gray-400 hover:text-white'"
                        class="px-6 py-2 rounded-full text-sm transition-all duration-300">
                        Todos
                    </button>
                    <button @click="filterStatus = 'pendente'"
                        :class="filterStatus === 'pendente' ? 'bg-white text-black font-black' : 'text-gray-400 hover:text-white'"
                        class="px-6 py-2 rounded-full text-sm transition-all duration-300">
                        Pendentes
                    </button>
                    <button @click="filterStatus = 'confirmado'"
                        :class="filterStatus === 'confirmado' ? 'bg-white text-black font-black' : 'text-gray-400 hover:text-white'"
                        class="px-6 py-2 rounded-full text-sm transition-all duration-300">
                        Confirmados
                    </button>
                </div>
            </div>

            <div class="space-y-6">
                <v-empty-state v-if="filteredAgendamentos.length === 0" icon="mdi-calendar-blank"
                    title="Nenhum agendamento" text="Não encontramos visitas para este filtro." bg-color="transparent"
                    theme="dark"></v-empty-state>

                <AgendamentoCard v-for="item in filteredAgendamentos" :key="item.id" :agendamento="item"
                    :user-type="userType" @open-history="openHistory" />
            </div>
        </main>

        <HistoryDrawer v-model="isHistoryOpen" :agendamento="selectedAgendamento" />
    </div>
</template>