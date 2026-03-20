<script setup>
import { ref, computed } from 'vue'
import GlobalHeader from '@/components/navigation/GlobalHeader.vue'

const props = defineProps({
    userName: { type: String, default: 'Usuário' },
    userType: { type: String, default: 'broker' }
})

// --- ESTADO REATIVO ---
const activeTab = ref('todas')

const notifications = ref([
    {
        id: 1,
        type: 'negociacao',
        title: 'Negociação avançou para Proposta Aceita',
        description: 'A negociação do Apartamento na Rua 7 de Setembro avançou para a etapa de Proposta Aceita',
        time: 'Há 5 minutos',
        isRead: false,
        icon: 'mdi-check-circle',
        color: 'success'
    },
    {
        id: 2,
        type: 'agendamento',
        title: 'Novo agendamento de visita',
        description: 'Corretor Carlos Mendes agendou visita para Casa em Condomínio - Efapi para amanhã às 14h',
        time: 'Há 15 minutos',
        isRead: false,
        icon: 'mdi-calendar',
        color: 'info'
    },
    {
        id: 3,
        type: 'interesse',
        title: 'Interesse em seu imóvel',
        description: 'Corretora Maria Santos demonstrou interesse no Apartamento 3 Quartos - Centro',
        time: 'Há 1 hora',
        isRead: false,
        icon: 'mdi-eye',
        color: 'warning'
    },
    {
        id: 6,
        type: 'cancelamento',
        title: 'Agendamento cancelado',
        description: 'A visita ao Apartamento Studio - São Cristóvão foi cancelada pelo corretor',
        time: 'Há 4 horas',
        isRead: true,
        icon: 'mdi-close-circle',
        color: 'error'
    }
])

const notificationSettings = ref({
    negociacoesAvancadas: true,
    novosAgendamentos: true,
    cancelamentoAgendamentos: true,
    interesseImoveis: true
})

// --- LÓGICA ---
const unreadCount = computed(() => notifications.value.filter(n => !n.isRead).length)

const filteredNotifications = computed(() => {
    if (activeTab.value === 'nao-lidas') return notifications.value.filter(n => !n.isRead)
    return notifications.value
})

const markAsRead = (id) => {
    const note = notifications.value.find(n => n.id === id)
    if (note) note.isRead = true
}

const markAllAsRead = () => {
    notifications.value.forEach(n => n.isRead = true)
}
</script>

<template>
    <div class="min-h-screen bg-[#F8F9FA]">
        <GlobalHeader :userName="props.userName" :userType="props.userType" />

        <main class="max-w-5xl mx-auto px-6 pt-32 pb-20">
            <div class="mb-12 flex flex-col md:flex-row md:items-end justify-between gap-6">
                <div>
                    <div class="flex items-center gap-4 mb-2">
                        <h1 class="text-4xl font-black text-black tracking-tighter uppercase italic">Notificações</h1>
                        <v-badge v-if="unreadCount > 0" :content="unreadCount" color="black" class="font-black"
                            inline></v-badge>
                    </div>
                    <p class="text-gray-500 font-bold uppercase text-[10px] tracking-[2px]">
                        Acompanhe a atividade da plataforma em tempo real
                    </p>
                </div>

                <v-btn v-if="activeTab !== 'configuracoes' && unreadCount > 0" variant="tonal" color="black"
                    class="!rounded-full !font-black !text-[10px] !tracking-widest" prepend-icon="mdi-check-all"
                    @click="markAllAsRead">
                    Marcar todas como lidas
                </v-btn>
            </div>

            <div class="bg-white rounded-[40px] p-2 mb-10 border border-gray-100 shadow-sm flex gap-2">
                <button
                    v-for="tab in [{ id: 'todas', label: 'Todas', icon: 'mdi-bell' }, { id: 'nao-lidas', label: 'Não Lidas', icon: 'mdi-bell-outline' }, { id: 'configuracoes', label: 'Configurações', icon: 'mdi-cog' }]"
                    :key="tab.id" @click="activeTab = tab.id" :class="[
                        'flex-1 py-4 rounded-[40px] font-black text-[10px] uppercase tracking-widest transition-all flex items-center justify-center gap-2',
                        activeTab === tab.id ? 'bg-black text-white shadow-xl scale-[1.02]' : 'text-gray-400 hover:text-black hover:bg-gray-50'
                    ]">
                    <v-icon :icon="tab.icon" size="16"></v-icon>
                    {{ tab.label }}
                </button>
            </div>

            <div v-if="activeTab !== 'configuracoes'" class="space-y-4">
                <div v-for="n in filteredNotifications" :key="n.id" @click="markAsRead(n.id)" :class="[
                    'bg-white rounded-[32px] p-6 border transition-all cursor-pointer flex gap-6 items-start group',
                    n.isRead ? 'border-gray-100 opacity-60' : 'border-black/5 shadow-md scale-[1.01]'
                ]">
                    <div
                        :class="[`w-14 h-14 rounded-2xl flex items-center justify-center flex-shrink-0 bg-gray-50 group-hover:bg-black group-hover:text-white transition-colors`]">
                        <v-icon :icon="n.icon" :color="n.isRead ? 'gray' : 'black'"></v-icon>
                    </div>

                    <div class="flex-1">
                        <div class="flex justify-between items-start mb-1">
                            <h3
                                :class="['text-sm font-black uppercase tracking-tight', n.isRead ? 'text-gray-500' : 'text-black']">
                                {{ n.title }}
                            </h3>
                            <span class="text-[9px] font-black text-gray-400 uppercase italic">{{ n.time }}</span>
                        </div>
                        <p class="text-xs font-bold text-gray-500 leading-relaxed">{{ n.description }}</p>
                    </div>

                    <div v-if="!n.isRead" class="w-2 h-2 bg-black rounded-full mt-2"></div>
                </div>

                <div v-if="filteredNotifications.length === 0"
                    class="text-center py-20 bg-white rounded-[40px] border border-dashed border-gray-200">
                    <v-icon icon="mdi-bell-off-outline" size="48" color="gray-lighten-2" class="mb-4"></v-icon>
                    <p class="text-gray-400 font-black uppercase text-xs tracking-widest">Nenhuma notificação por aqui
                    </p>
                </div>
            </div>

            <div v-else class="bg-white rounded-[40px] p-10 border border-gray-100 shadow-sm space-y-8">
                <div>
                    <h2 class="text-xl font-black text-black uppercase italic mb-2">Preferências de Alerta</h2>
                    <p class="text-xs font-bold text-gray-400 uppercase tracking-wider">Gerencie como você recebe
                        atualizações da plataforma</p>
                </div>

                <div class="space-y-6">
                    <div v-for="(val, key) in notificationSettings" :key="key"
                        class="flex items-center justify-between py-4 border-b border-gray-50 last:border-0">
                        <div>
                            <h4 class="text-xs font-black text-black uppercase tracking-widest mb-1">{{
                                key.replace(/([A-Z])/g, ' $1') }}</h4>
                            <p class="text-[10px] font-bold text-gray-400">Receber notificações push e via sistema para
                                este evento.</p>
                        </div>
                        <v-switch v-model="notificationSettings[key]" color="black" inset hide-details></v-switch>
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>

<style scoped>
.v-switch :deep(.v-selection-control__wrapper) {
    color: #000 !important;
}
</style>