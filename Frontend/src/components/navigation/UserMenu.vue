<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { 
  User, 
  Handshake, 
  Heart, 
  Bell, 
  Settings, 
  LogOut, 
  ChevronDown 
} from 'lucide-vue-next';
import AppImage from '@/components/common/UI/AppImage.vue';

interface UserMenuProps {
    userName: string;
    userType?: 'broker' | 'construction';
    compact?: boolean;
}

const props = withDefaults(defineProps<UserMenuProps>(), {
    userType: 'broker',
    compact: false
});

const emit = defineEmits(['navigate', 'logout']);

const isOpen = ref(false);
const menuRef = ref<HTMLElement | null>(null);

const toggleMenu = () => {
    isOpen.value = !isOpen.value;
};

const closeMenu = (e: MouseEvent) => {
    if (menuRef.value && !menuRef.value.contains(e.target as Node)) {
        isOpen.value = false;
    }
};

onMounted(() => {
    window.addEventListener('click', closeMenu);
});

onUnmounted(() => {
    window.removeEventListener('click', closeMenu);
});

const menuItems = [
    { id: 'profile', title: 'Meu Perfil', icon: User },
    { id: 'negociacoes', title: 'Negociações', icon: Handshake },
    { id: 'favorites', title: 'Favoritos', icon: Heart },
    { id: 'notifications', title: 'Notificações', icon: Bell, badge: true },
    { id: 'settings', title: 'Configurações', icon: Settings },
];

const handleNavigate = (id: string) => {
    isOpen.value = false;
    emit('navigate', id);
};

const handleLogout = () => {
    isOpen.value = false;
    emit('logout');
};
</script>

<template>
    <div class="relative" ref="menuRef">
        <div class="flex items-center gap-4">
            <div v-if="!compact" class="hidden sm:block text-right">
                <p class="text-[9px] font-[900] uppercase tracking-[0.3em] text-zinc-500 leading-none mb-1">Bem-vindo,</p>
                <p class="text-sm font-[900] text-black tracking-tighter italic">{{ userName }}</p>
            </div>

            <button 
                @click="toggleMenu"
                class="relative p-0.5 rounded-full border-2 border-transparent hover:border-emerald-500 transition-all duration-500 active:scale-95 group flex items-center gap-2"
            >
                <div class="w-11 h-11 rounded-full overflow-hidden shadow-lg bg-zinc-100 flex items-center justify-center border border-zinc-200">
                    <AppImage src="https://ui-avatars.com/api/?name=Admin&background=0D0D0D&color=fff" alt="Avatar" />
                </div>
                <div class="absolute -top-1 -right-1 w-4 h-4 bg-black border-2 border-white rounded-full flex items-center justify-center">
                    <div class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse shadow-[0_0_10px_#10B981]"></div>
                </div>
                <ChevronDown :class="['w-4 h-4 text-zinc-400 transition-transform duration-300', isOpen ? 'rotate-180' : '']" />
            </button>
        </div>

        <!-- Dropdown Menu -->
        <transition
            enter-active-class="transition duration-200 ease-out"
            enter-from-class="transform scale-95 opacity-0 -translate-y-2"
            enter-to-class="transform scale-100 opacity-100 translate-y-0"
            leave-active-class="transition duration-150 ease-in"
            leave-from-class="transform scale-100 opacity-100 translate-y-0"
            leave-to-class="transform scale-95 opacity-0 -translate-y-2"
        >
            <div 
                v-if="isOpen"
                class="absolute right-0 mt-4 w-64 bg-white border border-zinc-200 rounded-[24px] shadow-2xl overflow-hidden z-[100] py-2"
            >
                <div class="px-6 py-4 border-b border-zinc-100 bg-zinc-50/50">
                    <p class="text-[8px] font-[900] uppercase tracking-[0.3em] text-zinc-400 mb-1">Acesso B2B</p>
                    <p class="text-xs font-[900] text-emerald-600 uppercase italic tracking-widest">
                        {{ userType === 'construction' ? 'Construtora' : 'Corretor' }}
                    </p>
                </div>

                <div class="p-2">
                    <button 
                        v-for="item in menuItems" 
                        :key="item.id"
                        @click="handleNavigate(item.id)"
                        class="w-full flex items-center gap-3 px-4 py-3 rounded-[16px] hover:bg-zinc-50 text-zinc-600 hover:text-black transition-all group"
                    >
                        <component :is="item.icon" class="w-4 h-4 text-zinc-400 group-hover:text-emerald-500 transition-colors" />
                        <span class="text-xs font-bold uppercase tracking-widest">{{ item.title }}</span>
                        <div v-if="item.badge" class="ml-auto w-1.5 h-1.5 bg-emerald-500 rounded-full"></div>
                    </button>

                    <div class="h-px bg-zinc-100 my-2 mx-4"></div>

                    <button 
                        @click="handleLogout"
                        class="w-full flex items-center gap-3 px-4 py-3 rounded-[16px] hover:bg-red-50 text-red-500/80 hover:text-red-600 transition-all group"
                    >
                        <LogOut class="w-4 h-4 opacity-70 group-hover:opacity-100" />
                        <span class="text-xs font-bold uppercase tracking-widest">Sair da Conta</span>
                    </button>
                </div>
            </div>
        </transition>
    </div>
</template>