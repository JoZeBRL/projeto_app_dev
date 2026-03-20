<script setup lang="ts">
import { computed } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import Sidebar from '@/components/navigation/Sidebar.vue';
import DashboardCard from '@/components/dashboard/DashboardCard.vue';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();
const userName = computed(() => authStore.user?.nome?.split(' ')[0] || 'Gestor');

const cards = [
    { id: 'empreendimentos', title: 'Empreendimentos', description: 'Gestão de obras e torres', icon: 'mdi-crane' },
    { id: 'unidades', title: 'Unidades Disponíveis', description: 'Estoque atualizado em tempo real', icon: 'mdi-domain' },
    { id: 'propostas', title: 'Propostas Recebidas', description: 'Aprovação de negociações', icon: 'mdi-file-document-edit-outline', badge: 5 },
    { id: 'relatorios', title: 'Relatórios Financeiros', description: 'VGV e previsões de recebimento', icon: 'mdi-chart-line' },
];

const stats = [
    { label: 'VGV Potencial (M)', value: 'R$ 142' },
    { label: 'Unidades Vendidas', value: '84' },
    { label: 'Propostas Pendentes', value: '05', isHighlight: true },
];
</script>

<template>
    <div class="min-h-screen bg-black text-white selection:bg-emerald-500/30">
        <GlobalHeader :userName="userName" userType="construction" />

        <div class="max-w-[1600px] mx-auto flex">
            <Sidebar activeId="dashboard" userType="construction" />

            <main class="flex-1 pt-32 pb-20 px-10">
                <div class="mb-16 space-y-4">
                    <div class="flex items-center gap-6">
                        <h1 class="text-7xl font-[900] uppercase tracking-tighter italic leading-none">
                            Olá, <span class="text-zinc-800">{{ userName }}</span>
                        </h1>
                        <div class="h-[2px] flex-1 bg-gradient-to-r from-emerald-500/20 to-transparent mt-4"></div>
                    </div>
                    <p class="text-[10px] font-[900] uppercase tracking-[0.5em] text-emerald-500">
                        Painel de Controle da Construtora
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-8">
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
                        <h2 class="text-3xl font-[900] uppercase tracking-tighter italic">Visão Geral de <span class="text-zinc-500">Vendas</span></h2>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-16 relative z-10">
                        <div v-for="stat in stats" :key="stat.label" class="space-y-4 group">
                            <div :class="[
                                    'text-7xl font-[900] tracking-tighter italic transition-all duration-500 group-hover:scale-105 origin-left',
                                    stat.isHighlight ? 'text-emerald-500' : 'text-white'
                                ]">
                                {{ stat.value }}
                            </div>
                            <div class="text-[10px] font-[900] uppercase tracking-[0.3em] text-zinc-500 group-hover:text-zinc-300 transition-colors">
                                {{ stat.label }}
                            </div>
                        </div>
                    </div>
                </section>
            </main>
        </div>
    </div>
</template>