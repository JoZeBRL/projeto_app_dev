<script setup>
import { ref, onMounted } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';

// Mock de dados para o gráfico (Poderia ser movido para uma composable futuramente)
const mockData = [
    { name: 'Seg', visitas: 4, views: 24 },
    { name: 'Ter', visitas: 7, views: 32 },
    { name: 'Qua', visitas: 5, views: 28 },
    { name: 'Qui', visitas: 8, views: 45 },
    { name: 'Sex', visitas: 12, views: 52 },
    { name: 'Sab', visitas: 15, views: 68 },
    { name: 'Dom', visitas: 10, views: 42 },
];

const stats = [
    { label: 'Imóveis Ativos', value: '12', change: '+2 este mês', icon: 'mdi-home-variant-outline', color: 'text-blue-400', bg: 'bg-blue-500/10' },
    { label: 'Visualizações Totais', value: '1.284', change: '+14%', icon: 'mdi-eye-outline', color: 'text-emerald-400', bg: 'bg-emerald-500/10' },
    { label: 'Agendamentos', value: '24', change: '6 pendentes', icon: 'mdi-calendar-check', color: 'text-orange-400', bg: 'bg-orange-500/10' },
    { label: 'Propostas', value: '8', change: '2 novas', icon: 'mdi-handshake-outline', color: 'text-purple-400', bg: 'bg-purple-500/10' }
];

const activities = [
    { title: 'Novo agendamento', time: '10 min', desc: 'Residencial Aurora - Apto 302', icon: 'mdi-calendar', color: 'text-orange-500' },
    { title: 'Imóvel visualizado', time: '25 min', desc: 'Corretor João Silva visualizou Garden Ville', icon: 'mdi-eye', color: 'text-emerald-500' },
    { title: 'Nova negociação', time: '2h', desc: 'Proposta recebida para o Ed. Bellagio', icon: 'mdi-trending-up', color: 'text-blue-500' }
];
</script>

<template>
    <div class="min-h-screen bg-[#0A0A0A] text-white font-sans">
        <GlobalHeader />

        <main class="max-w-[1440px] mx-auto px-6 py-10 pt-32">
            <section class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-12">
                <div>
                    <h1 class="text-4xl font-black tracking-tighter mb-2">Olá, Construtora Realist</h1>
                    <p class="text-gray-400 font-medium">Desempenho dos seus lançamentos na plataforma.</p>
                </div>
                <v-btn prepend-icon="mdi-plus" size="x-large" color="white" rounded="pill"
                    class="!font-black !text-black shadow-xl hover:scale-105 transition-transform" flat>
                    Cadastrar Imóvel
                </v-btn>
            </section>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                <div v-for="(stat, index) in stats" :key="index"
                    class="bg-[#111111] border border-white/5 p-8 rounded-[40px] hover:border-white/20 transition-colors group">
                    <div class="flex items-center justify-between mb-6">
                        <div :class="['p-4 rounded-3xl transition-transform group-hover:scale-110', stat.bg]">
                            <v-icon :icon="stat.icon" :class="stat.color" size="28"></v-icon>
                        </div>
                        <span
                            class="text-[11px] font-black uppercase tracking-widest text-emerald-400 bg-emerald-400/10 px-3 py-1 rounded-full">
                            {{ stat.change }}
                        </span>
                    </div>
                    <h3 class="text-gray-500 text-xs font-black uppercase tracking-widest mb-1">{{ stat.label }}</h3>
                    <p class="text-3xl font-black text-white">{{ stat.value }}</p>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div
                    class="lg:col-span-2 bg-[#111111] border border-white/5 rounded-[40px] p-10 relative overflow-hidden">
                    <div class="flex justify-between items-start mb-10">
                        <div>
                            <h2 class="text-2xl font-black tracking-tight">Interesse nos Imóveis</h2>
                            <p class="text-gray-500 text-sm mt-1 font-medium">Visualizações vs Visitas semanais</p>
                        </div>
                        <v-select density="compact" variant="outlined" :items="['Últimos 7 dias', 'Últimos 30 dias']"
                            model-value="Últimos 7 dias" rounded="pill"
                            class="max-w-[180px] !text-xs font-bold"></v-select>
                    </div>

                    <div class="h-[300px] w-full flex items-end justify-between px-2 gap-4">
                        <div v-for="item in mockData" :key="item.name"
                            class="flex-1 flex flex-col items-center gap-4 group">
                            <div
                                class="w-full flex flex-col-reverse items-center h-48 bg-white/5 rounded-t-2xl relative overflow-hidden">
                                <div class="w-full bg-emerald-500/40 transition-all duration-1000 ease-out rounded-t-lg"
                                    :style="{ height: (item.views * 1.5) + 'px' }"></div>
                                <div class="absolute bottom-0 w-full bg-blue-500 transition-all duration-1000 ease-out z-10"
                                    :style="{ height: (item.visitas * 3) + 'px' }"></div>
                            </div>
                            <span class="text-[10px] font-black text-gray-500 uppercase tracking-tighter">{{ item.name
                                }}</span>
                        </div>
                    </div>
                </div>

                <div class="bg-[#111111] border border-white/5 rounded-[40px] p-10">
                    <h2 class="text-2xl font-black tracking-tight mb-8">Atividade</h2>
                    <div class="space-y-8">
                        <div v-for="(activity, i) in activities" :key="i" class="flex gap-5">
                            <div class="relative">
                                <div
                                    :class="['w-12 h-12 rounded-2xl flex items-center justify-center bg-white/5 border border-white/10']">
                                    <v-icon :icon="activity.icon" :class="activity.color" size="20"></v-icon>
                                </div>
                                <div v-if="i !== activities.length - 1"
                                    class="absolute top-14 left-1/2 -translate-x-1/2 w-px h-6 bg-white/10"></div>
                            </div>
                            <div class="flex-1">
                                <div class="flex justify-between items-start mb-1">
                                    <h4 class="text-sm font-black text-white">{{ activity.title }}</h4>
                                    <span class="text-[10px] text-gray-500 font-black uppercase">{{ activity.time
                                        }}</span>
                                </div>
                                <p class="text-xs text-gray-400 font-medium leading-relaxed">{{ activity.desc }}</p>
                            </div>
                        </div>
                    </div>
                    <v-btn block variant="outlined" rounded="pill"
                        class="mt-10 !border-white/10 !text-gray-400 font-black !capitalize" size="large">
                        Ver Relatório Completo
                    </v-btn>
                </div>
            </div>
        </main>
    </div>
</template>

<style scoped>
/* Customização para manter o "Figma Feel" sem sobrecarga de bibliotecas */
:deep(.v-field) {
    border-radius: 50px !important;
    background: rgba(255, 255, 255, 0.05) !important;
    border-color: rgba(255, 255, 255, 0.1) !important;
}
</style>