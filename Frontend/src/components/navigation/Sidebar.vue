<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { 
  LayoutDashboard, Search, Heart, 
  Calendar, Building, Wallet, 
  X, LogOut, Settings 
} from 'lucide-vue-next';

const props = defineProps<{
  isOpen: boolean;
}>();

const emit = defineEmits(['close']);
const route = useRoute();
const router = useRouter();

const menuItems = [
  { title: 'Dashboard', icon: LayoutDashboard, path: '/dashboard' },
  { title: 'Buscar Imóveis', icon: Search, path: '/search' },
  { title: 'Favoritos', icon: Heart, path: '/favorites' },
  { title: 'Agendamentos', icon: Calendar, path: '/agendamentos' },
  { title: 'Meus Imóveis', icon: Building, path: '/my-properties' },
  { title: 'Carteira', icon: Wallet, path: '/wallet' },
  { title: 'Configurações', icon: Settings, path: '/settings' },
];

const isActive = (path: string) => route.path === path;

const navigateTo = (path: string) => {
  router.push(path);
  if (window.innerWidth < 1024) emit('close');
};
</script>

<template>
  <!-- Overlay (Mobile) -->
  <transition
    enter-active-class="transition-opacity duration-300 ease-out"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
    leave-active-class="transition-opacity duration-200 ease-in"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div 
      v-if="isOpen" 
      class="fixed inset-0 bg-black/60 backdrop-blur-sm z-[60] lg:hidden"
      @click="emit('close')"
    ></div>
  </transition>

  <!-- Painel Lateral -->
  <aside 
    :class="[
      'fixed left-0 top-0 h-full bg-white dark:bg-[#0A0A0B] border-r border-gray-100 dark:border-white/5 z-[70] transition-all duration-500 ease-in-out w-80',
      isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
    ]"
  >
    <div class="flex flex-col h-full p-8 pt-6">
      <!-- Header Mobile -->
      <div class="flex items-center justify-between mb-12 lg:hidden">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-black rounded-lg flex items-center justify-center">
            <span class="text-white font-black italic text-lg">C.</span>
          </div>
          <span class="font-black italic text-xl tracking-tighter">CORRETIZA</span>
        </div>
        <button @click="emit('close')" class="p-2 hover:bg-gray-100 dark:hover:bg-white/5 rounded-full transition-colors">
          <X :size="20" />
        </button>
      </div>

      <!-- Links de Navegação -->
      <nav class="flex-1 space-y-2 overflow-y-auto custom-scrollbar -mx-2 px-2">
        <button 
          v-for="item in menuItems" 
          :key="item.path"
          @click="navigateTo(item.path)"
          :class="[
            'w-full flex items-center gap-4 px-4 py-4 rounded-2xl transition-all font-bold text-sm group relative overflow-hidden',
            isActive(item.path) 
              ? 'bg-black text-white shadow-xl shadow-black/10' 
              : 'text-gray-400 hover:bg-gray-50 dark:hover:bg-white/5 hover:text-black dark:hover:text-white'
          ]"
        >
          <component 
            :is="item.icon" 
            :size="20" 
            :class="[
              'transition-all duration-300',
              isActive(item.path) ? 'text-white scale-110' : 'text-gray-400 group-hover:text-black dark:group-hover:text-white group-hover:scale-110'
            ]"
          />
          <span class="tracking-widest uppercase text-[10px]">{{ item.title }}</span>
          
          <div v-if="isActive(item.path)" class="absolute right-0 top-0 bottom-0 w-1 bg-emerald-500"></div>
        </button>
      </nav>

      <!-- Rodapé Sair -->
      <div class="pt-6 border-t border-gray-100 dark:border-white/5">
        <button 
          @click="navigateTo('/login')"
          class="w-full flex items-center gap-4 px-4 py-4 rounded-2xl text-red-500 hover:bg-red-50 dark:hover:bg-red-500/10 transition-all font-black text-[11px] italic uppercase tracking-widest group"
        >
          <div class="p-2 bg-white dark:bg-white/10 rounded-xl shadow-sm group-hover:scale-110 transition-transform">
            <LogOut :size="20" />
          </div>
          SAIR DA CONTA
        </button>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #f1f1f1;
  border-radius: 10px;
}
.dark .custom-scrollbar::-webkit-scrollbar-thumb {
  background: #1f1f1f;
}
</style>