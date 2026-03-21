<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { 
  Search, Home, Heart, Bell, Handshake, Calendar, TrendingUp 
} from 'lucide-vue-next';
import { useAuthStore } from '@/stores/auth';
import DashboardCard from '@/components/dashboard/DashboardCard.vue';

const router = useRouter();
const authStore = useAuthStore();

const userName = computed(() => authStore.user?.nome || 'Corretor');

const cards = [
  {
    id: 'search',
    title: 'Buscar Imóveis',
    description: 'Encontre imóveis disponíveis para seus clientes agora mesmo.',
    icon: Search,
    route: '/search',
    color: 'bg-gray-50 hover:bg-gray-100 dark:bg-white/5'
  },
  {
    id: 'my-properties',
    title: 'Minha Carteira',
    description: 'Gerencie seus imóveis cadastrados e propostas ativas.',
    icon: Home,
    route: '/my-properties',
    color: 'bg-gray-50 hover:bg-gray-100 dark:bg-white/5'
  },
  {
    id: 'favorites',
    title: 'Favoritos',
    description: 'Acesse rapidamente os imóveis que você marcou como interesse.',
    icon: Heart,
    route: '/favorites',
    color: 'bg-gray-50 hover:bg-gray-100 dark:bg-white/5'
  },
  {
    id: 'negociacoes',
    title: 'Negociações',
    description: 'Acompanhe o status de todas as suas propostas em tempo real.',
    icon: Handshake,
    route: '/negociacoes',
    color: 'bg-gray-50 hover:bg-gray-100 dark:bg-white/5'
  },
  {
    id: 'agendamentos',
    title: 'Agendamentos',
    description: 'Organize suas visitas e reuniões com clientes e construtoras.',
    icon: Calendar,
    route: '/agendamentos',
    color: 'bg-gray-50 hover:bg-gray-100 dark:bg-white/5'
  },
  {
    id: 'notifications',
    title: 'Notificações',
    description: 'Fique por dentro de atualizações e novas oportunidades.',
    icon: Bell,
    route: '/notifications',
    color: 'bg-gray-50 hover:bg-gray-100 dark:bg-white/5'
  }
];

const navigateTo = (path: string) => {
  router.push(path);
};
</script>

<template>
  <div class="bg-white dark:bg-[#0A0A0B] transition-colors duration-300">
    <main class="max-w-7xl mx-auto px-6 py-12">
      <div class="mb-12">
        <h1 class="text-4xl font-black text-gray-900 dark:text-white tracking-tighter italic mb-2 uppercase">
          OLÁ, {{ userName }}!
        </h1>
        <p class="text-gray-500 dark:text-gray-400 text-lg font-medium">
          O que vamos realizar hoje no Corretiza?
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <DashboardCard 
          v-for="card in cards" 
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :icon="card.icon"
          :color-class="card.color"
          @click="navigateTo(card.route)"
        />
      </div>

      <section class="mt-16 bg-gray-50 dark:bg-white/5 rounded-[40px] p-10 border border-gray-100 dark:border-white/5">
        <div class="flex items-center gap-3 mb-8">
          <TrendingUp class="text-gray-900 dark:text-white" :size="24" />
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white italic tracking-tight">RESUMO PROFISSIONAL</h2>
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          <div class="space-y-1">
            <p class="text-4xl font-black text-gray-900 dark:text-white tracking-tighter">12</p>
            <p class="text-xs text-gray-500 font-bold uppercase tracking-widest">Imóveis na Carteira</p>
          </div>
          <div class="space-y-1 text-emerald-600">
            <p class="text-4xl font-black tracking-tighter">05</p>
            <p class="text-xs font-bold uppercase tracking-widest">Negociações Ativas</p>
          </div>
          <div class="space-y-1">
            <p class="text-4xl font-black text-gray-900 dark:text-white tracking-tighter">45</p>
            <p class="text-xs text-gray-500 font-bold uppercase tracking-widest">Imóveis Favoritados</p>
          </div>
          <div class="space-y-1 text-gray-900 dark:text-white">
            <p class="text-4xl font-black tracking-tighter">08</p>
            <p class="text-xs text-gray-500 font-bold uppercase tracking-widest">Visitas este mês</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
/* Transições suaves */
.dashboard-enter-active, .dashboard-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.dashboard-enter-from, .dashboard-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>