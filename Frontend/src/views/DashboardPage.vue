<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { Search, Calendar, Handshake, Home, Heart, Bell, ArrowRight } from 'lucide-vue-next';

const router = useRouter();
const notifications = ref(3);

const dashboardCards = [
  { id: 'search', title: 'Buscar Imóveis', description: 'Encontre imóveis disponíveis', icon: Search },
  { id: 'agendamentos', title: 'Agendamentos', description: 'Gerencie suas visitas', icon: Calendar },
  { id: 'negociacoes', title: 'Negociações', description: 'Acompanhe suas propostas', icon: Handshake },
  { id: 'my-properties', title: 'Meus Imóveis', description: 'Gerencie seus imóveis', icon: Home },
  { id: 'favorites', title: 'Favoritos', description: 'Imóveis salvos como favoritos', icon: Heart },
  { id: 'notifications', title: 'Notificações', description: 'Atualizações e mensagens', icon: Bell, badge: notifications.value }
];

const navigateTo = (routeName: string) => {
  router.push({ name: routeName });
};
</script>

<template>
  <div class="animate-fade-in">
    <div class="mb-8">
      <h1 class="text-gray-900 text-3xl font-medium">Dashboard</h1>
      <p class="text-gray-500 mt-1">Gerencie e acesse rapidamente as funcionalidades da plataforma</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <button
        v-for="card in dashboardCards"
        :key="card.id"
        @click="navigateTo(card.id)"
        class="p-6 rounded-[24px] border border-gray-200 transition-all duration-200 text-left group bg-white hover:-translate-y-1 hover:shadow-md outline-none relative"
      >
        <div class="flex items-start justify-between mb-4">
          <div class="p-3 rounded-2xl bg-gray-50 group-hover:bg-[#10B981]/10 transition-colors">
            <component :is="card.icon" class="h-6 w-6 text-gray-700 group-hover:text-[#10B981] transition-colors" />
          </div>
          
          <span v-if="card.badge" class="bg-[#10B981] text-white text-xs px-2 py-1 rounded-full min-w-[20px] text-center font-bold shadow-sm">
            {{ card.badge }}
          </span>
        </div>
        
        <div>
          <h3 class="font-medium text-gray-900 mb-1 group-hover:text-black transition-colors">
            {{ card.title }}
          </h3>
          <p class="text-sm text-gray-500 group-hover:text-gray-700 transition-colors line-clamp-2">
            {{ card.description }}
          </p>
        </div>
        
        <div class="mt-4 opacity-0 group-hover:opacity-100 transition-all transform -translate-x-2 group-hover:translate-x-0">
          <div class="w-8 h-8 bg-black rounded-full flex items-center justify-center shadow-sm">
            <ArrowRight class="w-4 h-4 text-white" />
          </div>
        </div>
      </button>
    </div>

    <div class="mt-12 bg-white rounded-[24px] border border-gray-200 p-8 shadow-sm">
      <h2 class="text-xl font-medium text-gray-900 mb-6">Resumo Profissional</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="text-center p-6 bg-gray-50 rounded-[16px] border border-transparent hover:border-[#10B981]/30 transition-all">
          <div class="text-3xl font-bold text-gray-900 mb-1">12</div>
          <div class="text-sm text-gray-500">Imóveis na Carteira</div>
        </div>
        <div class="text-center p-6 bg-gray-50 rounded-[16px] border border-transparent hover:border-[#10B981]/30 transition-all">
          <div class="text-3xl font-bold text-gray-900 mb-1">45</div>
          <div class="text-sm text-gray-500">Imóveis Favoritados</div>
        </div>
        <div class="text-center p-6 bg-gray-50 rounded-[16px] border border-transparent hover:border-[#10B981]/30 transition-all">
          <div class="text-3xl font-bold text-[#10B981] mb-1">{{ notifications }}</div>
          <div class="text-sm text-gray-500">Novas Notificações</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.animate-fade-in { animation: fadeIn 0.4s ease-out; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>