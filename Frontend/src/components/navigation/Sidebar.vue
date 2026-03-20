<script setup lang="ts">
import { computed } from 'vue';

interface Props {
    activeId: string;
    userType?: 'broker' | 'construction';
}

const props = withDefaults(defineProps<Props>(), {
    userType: 'broker'
});

const emit = defineEmits(['navigate', 'logout']);

const navItems = computed(() => [
    { id: 'dashboard', label: 'Dashboard', icon: 'mdi-view-dashboard-outline' },
    { id: 'search', label: props.userType === 'construction' ? 'Dashboard' : 'Explorar', icon: 'mdi-magnify' },
    { id: 'favorites', label: 'Favoritos', icon: 'mdi-heart-outline' },
    { id: 'agendamentos', label: 'Agendamentos', icon: 'mdi-calendar-clock' },
    { id: 'negociacoes', label: 'Negociações', icon: 'mdi-handshake-outline' },
    { id: 'my-properties', label: 'Meus Imóveis', icon: 'mdi-home-city-outline' },
    { id: 'wallet', label: 'Carteira', icon: 'mdi-wallet-outline' },
]);
</script>

<template>
    <v-navigation-drawer 
        permanent 
        width="280"
        class="!bg-black !border-r !border-white/5 !pt-[100px]"
    >
        <div class="px-6 flex flex-col h-full">
            <button @click="emit('navigate', 'add-property')"
                class="w-full btn-premium !py-4 mb-10 shadow-[0_0_20px_rgba(255,255,255,0.05)]">
                <v-icon icon="mdi-plus-circle-outline" size="20" />
                <span class="italic">NOVO ANÚNCIO</span>
            </button>

            <nav class="flex-1 space-y-2 custom-nav">
                <button v-for="item in navItems" :key="item.id"
                    @click="emit('navigate', item.id)" 
                    :class="[
                        'w-full flex items-center gap-4 px-6 py-4 rounded-[40px] transition-all duration-500 group relative',
                        activeId === item.id
                            ? 'bg-white text-black shadow-[0_10px_30px_rgba(255,255,255,0.1)]'
                            : 'text-zinc-500 hover:text-white hover:bg-white/5'
                    ]"
                >
                    <v-icon :icon="item.icon" size="20" 
                        :class="activeId === item.id ? 'text-black' : 'text-zinc-600 group-hover:text-emerald-500'" />
                    <span class="font-[900] uppercase tracking-[0.2em] text-[10px]">{{ item.label }}</span>

                    <div v-if="activeId === item.id" class="absolute right-4 w-1.5 h-1.5 rounded-full bg-black"></div>
                </button>
            </nav>

            <div class="mb-8 glass-container !p-6 !rounded-3xl border-dashed border-white/10">
                <p class="text-[8px] font-[900] uppercase tracking-[0.3em] text-zinc-600 mb-1">Suporte VIP</p>
                <p class="text-[10px] font-bold text-zinc-300 mb-4">ajuda@corretiza.com.br</p>
                <v-btn block variant="tonal" color="white" size="small" 
                    class="!rounded-xl !font-[900] !text-[9px] !tracking-widest uppercase"
                    @click="emit('logout')">
                    Encerrar Sessão
                </v-btn>
            </div>
        </div>
    </v-navigation-drawer>
</template>

<style scoped>
.custom-nav {
    scrollbar-width: none;
    -ms-overflow-style: none;
}
.custom-nav::-webkit-scrollbar { display: none; }
</style>