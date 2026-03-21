<script setup lang="ts">
import { ref } from 'vue';
import { Menu, Search, Bell, User } from 'lucide-vue-next';
import UserMenu from './UserMenu.vue';
import Logo from './Logo.vue';

const props = defineProps<{
  userName?: string;
  userType?: 'broker' | 'construction';
}>();

const emit = defineEmits(['open-sidebar', 'logout']);

const searchQuery = ref('');
const showUserMenu = ref(false);
</script>

<template>
  <header class="fixed top-0 left-0 right-0 h-20 bg-white/80 dark:bg-[#0A0A0B]/80 backdrop-blur-md border-b border-gray-100 dark:border-white/5 z-50 px-6 transition-all duration-300">
    <div class="max-w-7xl mx-auto h-full flex items-center justify-between gap-8">
      
      <div class="flex items-center gap-4">
        <button 
          @click="emit('open-sidebar')"
          class="lg:hidden p-2 text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-white/5 rounded-xl transition-colors"
        >
          <Menu :size="24" />
        </button>
        <Logo class="w-32" variant="light" />
      </div>

      <!-- Barra de Busca -->
      <div class="hidden md:flex flex-1 max-w-2xl relative group">
        <Search class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-black transition-colors" :size="20" />
        <input 
          v-model="searchQuery"
          type="text" 
          placeholder="Buscar imóveis, construtoras ou cidades..."
          class="w-full bg-[#f3f3f5] dark:bg-white/5 border-transparent border-2 rounded-full py-2.5 pl-12 pr-4 text-sm focus:border-black focus:bg-white transition-all outline-none font-medium"
        />
      </div>

      <div class="flex items-center gap-3">
        <!-- Notificações -->
        <button class="relative p-2.5 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-white/5 rounded-full transition-all active:scale-95">
          <Bell :size="22" />
          <span class="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full border-2 border-white dark:border-[#0A0A0B]"></span>
        </button>
        
        <div class="h-8 w-px bg-gray-200 dark:bg-white/10 mx-2"></div>

        <!-- Popover do Usuário (Sinalizador) -->
        <button 
          @click="showUserMenu = !showUserMenu"
          class="flex items-center gap-2 p-1 pl-3 bg-gray-50 dark:bg-white/5 rounded-full border border-gray-100 dark:border-white/5 hover:shadow-sm transition-all active:scale-95 group"
          :class="showUserMenu ? 'ring-2 ring-black' : ''"
        >
          <span class="text-[10px] font-black text-gray-900 dark:text-white hidden sm:block italic tracking-widest uppercase">
            {{ userName || 'MEU PERFIL' }}
          </span>
          <div class="w-8 h-8 rounded-full bg-black flex items-center justify-center text-white shadow-lg group-hover:scale-105 transition-transform">
            <User :size="18" />
          </div>
        </button>

        <!-- Menu Dropdown REAL (Floating Popover) -->
        <UserMenu 
          v-if="showUserMenu" 
          :user-name="userName"
          :user-type="userType"
          @close="showUserMenu = false"
          @logout="emit('logout')"
        />
      </div>
    </div>
  </header>
</template>