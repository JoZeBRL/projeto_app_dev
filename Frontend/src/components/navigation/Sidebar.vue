<script setup lang="ts">
import { computed } from 'vue';
import { LayoutDashboard, Search, Heart, Calendar, Handshake, Building, Wallet, X, LogOut } from 'lucide-vue-next';

const props = withDefaults(defineProps<{
  isOpen: boolean;
  currentPage: string;
  userName?: string;
  userType?: 'broker' | 'construction';
}>(), { userType: 'broker' });

const emit = defineEmits(['close', 'navigate', 'logout']);

const navItems = computed(() => [
  { id: 'my-properties', label: 'Meus Imóveis', icon: Building },
  { id: 'search', label: props.userType === 'construction' ? 'Dashboard' : 'Pesquisar', icon: Search },
  { id: 'favorites', label: 'Favoritos', icon: Heart },
  { id: 'agendamentos', label: 'Agendamentos', icon: Calendar },
  { id: 'wallet', label: 'Carteira', icon: Wallet },
  { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
]);
</script>

<template>
  <div v-if="isOpen" class="fixed inset-0 z-[100] lg:hidden">
    <div 
      class="fixed inset-0 bg-black/50 transition-opacity" 
      @click="emit('close')"
    ></div>
    
    <div class="fixed left-0 top-0 h-full w-80 bg-white border-r border-gray-200 shadow-2xl flex flex-col animate-slide-right">
      
      <div class="flex items-center justify-between p-6 border-b border-gray-100">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-black rounded-lg flex items-center justify-center">
            <span class="text-white font-black italic text-lg">C.</span>
          </div>
          <span class="text-black font-black text-lg italic uppercase tracking-tighter">Corretiza</span>
        </div>
        <button @click="emit('close')" class="p-2 rounded-lg hover:bg-gray-100 transition-colors text-gray-500">
          <X class="w-5 h-5" />
        </button>
      </div>

      <nav class="flex-1 overflow-y-auto p-6 space-y-2">
        <button
          v-for="item in navItems"
          :key="item.id"
          @click="emit('navigate', item.id)"
          :class="[
            'w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 outline-none',
            currentPage === item.id ? 'bg-gray-100/60 text-black font-medium' : 'text-gray-600 hover:bg-gray-50 hover:text-black font-medium'
          ]"
        >
          <component :is="item.icon" class="w-5 h-5" />
          <span class="text-sm">{{ item.label }}</span>
        </button>
      </nav>

      <div class="p-6 border-t border-gray-100 bg-gray-50/50">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs text-gray-500 font-medium">{{ userType === 'construction' ? 'Construtora' : 'Corretor' }}</p>
            <p class="text-sm font-bold text-gray-900">{{ userName }}</p>
          </div>
          <button @click="emit('logout')" class="p-2 rounded-lg hover:bg-gray-200 transition-colors text-gray-600">
            <LogOut class="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.animate-slide-right {
  animation: slideRight 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes slideRight {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}
</style>