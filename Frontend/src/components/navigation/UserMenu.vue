<script setup lang="ts">
import { User, Settings, LogOut, ChevronRight, Handshake, Heart, Bell } from 'lucide-vue-next';
import { useRouter } from 'vue-router';

const props = defineProps<{
  userName?: string;
  userType?: 'broker' | 'construction';
}>();

const emit = defineEmits(['close', 'logout']);
const router = useRouter();

const navigateTo = (path: string) => {
  router.push(path);
  emit('close');
};

const handleLogout = () => {
    emit('logout');
    emit('close');
};
</script>

<template>
  <div 
    class="absolute top-full right-0 mt-3 w-72 bg-white dark:bg-[#121214] rounded-3xl shadow-2xl border border-gray-100 dark:border-white/5 p-3 z-[100] animate-in fade-in slide-in-from-top-2 duration-300"
  >
    <!-- Header do Menu -->
    <div class="p-5 mb-2 bg-gray-50/50 dark:bg-white/5 rounded-2xl border border-gray-100 dark:border-white/5">
      <p class="text-[9px] text-gray-400 font-black uppercase tracking-[0.3em] mb-1 leading-none">CONTA CONECTADA</p>
      <p class="text-sm font-black text-gray-900 dark:text-white italic tracking-tighter truncate uppercase">
        {{ userName || 'Visitante' }}
      </p>
      <p class="text-[10px] font-bold text-emerald-500 uppercase tracking-widest mt-1">
        {{ userType === 'construction' ? 'Construtora' : 'Corretor' }}
      </p>
    </div>

    <!-- Opções -->
    <div class="space-y-1">
      <button 
        @click="navigateTo('/profile')"
        class="w-full flex items-center justify-between p-3.5 rounded-2xl hover:bg-gray-100 dark:hover:bg-white/5 transition-all group border border-transparent hover:border-gray-200 dark:hover:border-white/10"
      >
        <div class="flex items-center gap-3">
          <div class="p-2 bg-white dark:bg-white/10 rounded-xl shadow-sm group-hover:scale-110 transition-transform">
            <User :size="18" class="text-gray-400 group-hover:text-black dark:group-hover:text-white" />
          </div>
          <span class="text-sm font-bold text-gray-600 dark:text-gray-300 group-hover:text-black dark:group-hover:text-white italic">Meu Perfil</span>
        </div>
        <ChevronRight :size="14" class="text-gray-300 opacity-0 group-hover:opacity-100 transition-all" />
      </button>

      <button 
        @click="navigateTo('/settings')"
        class="w-full flex items-center justify-between p-3.5 rounded-2xl hover:bg-gray-100 dark:hover:bg-white/5 transition-all group border border-transparent hover:border-gray-200 dark:hover:border-white/10"
      >
        <div class="flex items-center gap-3">
          <div class="p-2 bg-white dark:bg-white/10 rounded-xl shadow-sm group-hover:scale-110 transition-transform">
            <Settings :size="18" class="text-gray-400 group-hover:text-black dark:group-hover:text-white" />
          </div>
          <span class="text-sm font-bold text-gray-600 dark:text-gray-300 group-hover:text-black dark:group-hover:text-white italic">Configurações</span>
        </div>
        <ChevronRight :size="14" class="text-gray-300 opacity-0 group-hover:opacity-100 transition-all" />
      </button>
    </div>

    <!-- Rodapé Sair -->
    <div class="mt-2 pt-2 border-t border-gray-100 dark:border-white/5">
      <button 
        @click="handleLogout"
        class="w-full flex items-center gap-3 p-3.5 rounded-2xl text-red-500 hover:bg-red-50 dark:hover:bg-red-500/10 transition-all font-black text-sm italic uppercase tracking-tighter"
      >
        <div class="p-2 bg-white dark:bg-white/10 rounded-xl shadow-sm">
          <LogOut :size="18" />
        </div>
        Sair da Conta
      </button>
    </div>
  </div>
</template>
late>