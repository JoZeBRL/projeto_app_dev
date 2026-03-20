<script setup lang="ts">
import { ref, computed } from 'vue';
import { useAuthStore } from '@/stores/auth';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import Sidebar from '@/components/navigation/Sidebar.vue';
import DashboardCard from '@/components/dashboard/DashboardCard.vue';

const authStore = useAuthStore();
const userName = computed(() => authStore.user?.nome?.split(' ')[0] || 'Corretor');
const notificationCount = ref(3);

const cards = [
    { id: 'search', title: 'Buscar Imóveis', description: 'Inteligência de mercado e oportunidades', icon: 'mdi-magnify' },
    { id: 'schedule', title: 'Agendamentos', description: 'Gestão de visitas e reuniões técnicas', icon: 'mdi-calendar-clock' },
    { id: 'deals', title: 'Negociações', description: 'Acompanhamento de propostas em tempo real', icon: 'mdi-handshake-outline' },
    { id: 'portfolio', title: 'Meus Imóveis', description: 'Gestão de ativos e carteira exclusiva', icon: 'mdi-home-city-outline' },
    { id: 'favorites', title: 'Favoritos', description: 'Seleção estratégica de oportunidades', icon: 'mdi-heart-outline' },
    { id: 'notifications', title: 'Notificações', description: 'Alertas críticos e mensagens do sistema', icon: 'mdi-bell-outline', badge: notificationCount.value },
];

const stats = [
    { label: 'Ativos na Carteira', value: '12' },
    { label: 'Potenciais Clientes', value: '45' },
    { label: 'Novos Alertas', value: notificationCount.value, isHighlight: true },
];
</script>

<template>
    <div class="min-h-screen bg-black text-white selection:bg-emerald-500/30">
        <GlobalHeader :user-name="userName" user-type="broker" />

        <div class="max-w-[1600px] mx-auto flex">
            <Sidebar active-id="dashboard" />

            <main class="flex-1 pt-32 pb-20 px-10">
                <div class="mb-16 space-y-4">
                    <div class="flex items-center gap-6">
                        <h1 class="text-7xl font-black uppercase tracking-tighter italic leading-none">
                            Olá, <span class="text-zinc-800">{{ userName }}</span>
                        </h1>
                        <div class="h-[2px] flex-1 bg-gradient-to-r from-emerald-500/20 to-transparent mt-4"></div>
                    </div>
                    <p class="text-[10px] font-black uppercase tracking-[0.5em] text-emerald-500">
                        Central de Comando Operacional B2B
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
                    <DashboardCard 
                        v-for="card in cards" 
                        :key="card.id" 
                        v-bind="card" 
                        @click="$router.push({ name: card.id })" 
                    />
                </div>

                <section class="mt-20 glass-container p-16 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-1/3 h-full bg-emerald-500/5 blur-[120px] pointer-events-none"></div>
                    
                    <div class="flex items-center gap-4 mb-12 relative z-10">
                        <div class="w-1.5 h-8 bg-emerald-500 rounded-full shadow-[0_0_15px_rgba(16,185,129,0.5)]"></div>
                        <h2 class="text-3xl font-black uppercase tracking-tighter italic">Resumo de <span class="text-zinc-500">Performance</span></h2>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-16 relative z-10">
                        <div v-for="stat in stats" :key="stat.label" class="space-y-4 group">
                            <div 
                                :class="[
                                    'text-7xl font-black tracking-tighter italic transition-all duration-500 group-hover:scale-105 origin-left',
                                    stat.isHighlight ? 'text-emerald-500' : 'text-white'
                                ]"
                            >
                                {{ stat.value }}
                            </div>
                            <div class="text-[10px] font-black uppercase tracking-[0.3em] text-zinc-500 group-hover:text-zinc-300 transition-colors">
                                {{ stat.label }}
                            </div>
                        </div>
                    </div>
                </section>
            </main>
        </div>
    </div>
</template>

<style scoped>
/* Transição suave para o hover dos cards */
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s ease;
}
</style>