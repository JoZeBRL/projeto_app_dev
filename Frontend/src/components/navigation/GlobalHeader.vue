<script setup lang="ts">
import { computed } from 'vue';
import { Menu } from 'lucide-vue-next';
import UserMenu from './UserMenu.vue';

const props = defineProps<{
  userName: string;
  userType?: 'broker' | 'construction';
  currentPage: string;
}>();

const emit = defineEmits(['open-sidebar', 'navigate', 'logout']);

const navLinks = computed(() => [
  { id: 'search', label: props.userType === 'construction' ? 'Dashboard' : 'Pesquisar' },
  { id: 'my-properties', label: 'Meus Imóveis' },
  { id: 'negociacoes', label: 'Negociações' },
  { id: 'favorites', label: 'Favoritos' },
]);
</script>

<template>
  <header class="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
      
      <div class="flex items-center gap-4">
        <button @click="emit('open-sidebar')" class="lg:hidden p-2 -ml-2 rounded-lg text-gray-600 hover:bg-gray-100 transition-colors">
          <Menu class="w-6 h-6" />
        </button>

        <div class="flex items-center gap-3 cursor-pointer select-none" @click="emit('navigate', 'dashboard')">
          <div class="w-10 h-10 bg-black rounded-[10px] flex items-center justify-center shadow-md">
            <span class="text-white font-black italic text-xl">C.</span>
          </div>
          <span class="hidden sm:block text-black font-black text-xl italic uppercase tracking-tighter">Corretiza</span>
        </div>
      </div>

      <nav class="hidden lg:flex items-center gap-8">
        <button 
          v-for="link in navLinks" 
          :key="link.id"
          @click="emit('navigate', link.id)"
          :class="[
            'text-sm font-medium transition-colors hover:text-black outline-none',
            currentPage === link.id ? 'text-black' : 'text-gray-500'
          ]"
        >
          {{ link.label }}
        </button>
      </nav>

      <UserMenu 
        :userName="userName" 
        :userType="userType" 
        @navigate="(id) => emit('navigate', id)" 
        @logout="emit('logout')" 
      />
    </div>
  </header>
</template>