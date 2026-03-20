<script setup lang="ts">
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth';
import DashboardCard from '@/components/dashboard/DashboardCard.vue';

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
    <div class="space-y-12 animate-fade-in">
        <div class="space-y-4">
            <h1 class="text-7xl font-[900] uppercase tracking-tighter italic leading-none text-[var(--text-color)]">
                Olá, <span class="text-emerald-500">{{ userName }}</span>
            </h1>
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
                <h2 class="text-3xl font-[900] uppercase tracking-tighter italic text-[var(--text-color)]">Visão Geral de <span class="text-zinc-500">Vendas</span></h2>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-16 relative z-10">
                <div v-for="stat in stats" :key="stat.label" class="space-y-4 group">
                    <div :class="[
                            'text-7xl font-[900] tracking-tighter italic transition-all duration-500 group-hover:scale-105 origin-left',
                            stat.isHighlight ? 'text-emerald-500' : 'text-[var(--text-color)]'
                        ]">
                        {{ stat.value }}
                    </div>
                    <div class="text-[10px] font-[900] uppercase tracking-[0.2em] text-[var(--label-color)] group-hover:text-zinc-300 transition-colors">
                        {{ stat.label }}
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<style scoped>
.animate-fade-in { animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1); }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style>