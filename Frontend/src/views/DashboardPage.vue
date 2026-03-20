<script setup lang="ts">
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth';
import DashboardCard from '@/components/dashboard/DashboardCard.vue';

const authStore = useAuthStore();
const userName = computed(() => authStore.user?.nome?.split(' ')[0] || 'Corretor');
const notificationCount = 3;

const cards = [
    { id: 'search', title: 'Buscar Imóveis', description: 'Inteligência de mercado', icon: 'mdi-magnify' },
    { id: 'schedule', title: 'Agendamentos', description: 'Gestão de visitas', icon: 'mdi-calendar-clock' },
    { id: 'deals', title: 'Negociações', description: 'Propostas em tempo real', icon: 'mdi-handshake-outline' },
    { id: 'portfolio', title: 'Meus Imóveis', description: 'Gestão de carteira', icon: 'mdi-home-city-outline' },
];

const stats = [
    { label: 'Ativos na Carteira', value: '12' },
    { label: 'Potenciais Clientes', value: '45' },
    { label: 'Novos Alertas', value: notificationCount, isHighlight: true },
];
</script>

<template>
    <div class="space-y-12 animate-fade-in">
        <div class="space-y-4">
            <h1 class="text-5xl font-[900] uppercase tracking-tighter italic text-[var(--text-color)]">
                Olá, <span class="text-emerald-500">{{ userName }}</span>
            </h1>
            <p class="text-[10px] font-[900] uppercase tracking-[0.5em] text-[var(--label-color)]">
                Central de Comando Operacional B2B
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
            <DashboardCard v-for="card in cards" :key="card.id" v-bind="card" @click="$router.push({ name: card.id })" />
        </div>

        <section class="mt-12 glass-container p-12 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-1/3 h-full bg-emerald-500/5 blur-[120px] pointer-events-none"></div>
            
            <div class="flex items-center gap-4 mb-10 relative z-10">
                <div class="w-1.5 h-8 bg-emerald-500 rounded-full"></div>
                <h2 class="text-2xl font-[900] uppercase tracking-tighter italic text-[var(--text-color)]">Resumo de Performance</h2>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-12 relative z-10">
                <div v-for="stat in stats" :key="stat.label" class="space-y-2">
                    <div :class="['text-6xl font-[900] tracking-tighter italic', stat.isHighlight ? 'text-emerald-500' : 'text-[var(--text-color)]']">
                        {{ stat.value }}
                    </div>
                    <div class="text-[10px] font-[900] uppercase tracking-[0.2em] text-[var(--label-color)]">
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