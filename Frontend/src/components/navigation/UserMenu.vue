<script setup lang="ts">
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

const menuItems = [
    { id: 'profile', title: 'Meu Perfil', icon: 'mdi-account-outline' },
    { id: 'negociacoes', title: 'Negociações', icon: 'mdi-handshake-outline' },
    { id: 'favorites', title: 'Favoritos', icon: 'mdi-heart-outline' },
    { id: 'notifications', title: 'Notificações', icon: 'mdi-bell-outline', badge: true },
    { id: 'settings', title: 'Configurações', icon: 'mdi-cog-outline' },
];
</script>

<template>
    <div class="flex items-center gap-4">
        <div v-if="!compact" class="hidden sm:block text-right">
            <p class="text-[9px] font-[900] uppercase tracking-[0.3em] text-zinc-600 leading-none mb-1">Bem-vindo,</p>
            <p class="text-sm font-[900] text-white tracking-tighter italic">{{ userName }}</p>
        </div>

        <v-menu location="bottom end" transition="slide-y-transition" offset="12">
            <template v-slot:activator="{ props: menu }">
                <button v-bind="menu"
                    class="relative p-0.5 rounded-full border-2 border-transparent hover:border-emerald-500 transition-all duration-500 active:scale-95 group"
                >
                    <v-avatar size="44" class="shadow-2xl">
                        <AppImage src="https://cdn.vuetifyjs.com/images/john.jpg" alt="Avatar" />
                    </v-avatar>
                    <div class="absolute top-0 right-0 w-3.5 h-3.5 bg-black border-2 border-black rounded-full flex items-center justify-center">
                        <div class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse shadow-[0_0_10px_#10B981]"></div>
                    </div>
                </button>
            </template>

            <v-list width="260" class="!bg-[#0a0a0a] !border !border-white/10 !rounded-[32px] !p-3 mt-4 overflow-hidden">
                <div class="px-4 py-4 mb-2">
                    <p class="text-[8px] font-[900] uppercase tracking-[0.3em] text-zinc-600 mb-1">Acesso B2B</p>
                    <p class="text-xs font-[900] text-emerald-500 uppercase italic tracking-widest">
                        {{ userType === 'construction' ? 'Construtora' : 'Corretio' }}
                    </p>
                </div>

                <v-divider class="!border-white/5 mb-2" />

                <v-list-item v-for="item in menuItems" :key="item.id" 
                    @click="emit('navigate', item.id)"
                    class="!rounded-[20px] mb-1 hover:!bg-white/5 group transition-colors"
                >
                    <template v-slot:prepend>
                        <v-icon :icon="item.icon" size="20" class="text-zinc-600 group-hover:text-white transition-colors" />
                    </template>
                    <v-list-item-title class="!text-[11px] !font-[900] !uppercase !tracking-widest !text-zinc-400 group-hover:!text-white">
                        {{ item.title }}
                    </v-list-item-title>
                    <template v-slot:append v-if="item.badge">
                        <div class="w-1.5 h-1.5 bg-emerald-500 rounded-full"></div>
                    </template>
                </v-list-item>

                <v-divider class="!border-white/5 my-2" />

                <v-list-item @click="emit('logout')" class="!rounded-[20px] hover:!bg-red-500/10 group transition-colors">
                    <template v-slot:prepend>
                        <v-icon icon="mdi-logout" size="20" class="text-red-500/60 group-hover:text-red-500" />
                    </template>
                    <v-list-item-title class="!text-[11px] !font-[900] !uppercase !tracking-widest !text-red-500/60 group-hover:!text-red-500">
                        Sair da Conta
                    </v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
    </div>
</template>