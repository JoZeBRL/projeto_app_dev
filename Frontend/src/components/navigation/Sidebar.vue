<script setup lang="ts">
import { computed } from 'vue';

const props = withDefaults(defineProps<{ activeId: string; userType?: 'broker' | 'construction' }>(), { userType: 'broker' });
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
    <aside class="w-64 hidden lg:flex flex-col pt-8 pr-6 border-r border-[var(--glass-border)] min-h-[calc(100vh-6rem)]">
        <button @click="emit('navigate', 'add-property')"
            class="btn-premium !py-4 mb-10 w-full">
            <v-icon icon="mdi-plus-circle-outline" size="20" />
            <span class="italic text-[10px]">NOVO ANÚNCIO</span>
        </button>

        <nav class="flex-1 space-y-2">
            <button v-for="item in navItems" :key="item.id"
                @click="emit('navigate', item.id)" 
                :class="[
                    'w-full flex items-center gap-4 px-6 py-4 rounded-[40px] transition-all duration-300 group relative',
                    activeId === item.id
                        ? 'bg-[var(--text-color)] text-[var(--bg-color)] shadow-xl'
                        : 'text-[var(--label-color)] hover:bg-[var(--glass-border)] hover:text-[var(--text-color)]'
                ]"
            >
                <v-icon :icon="item.icon" size="20" />
                <span class="font-[900] uppercase tracking-[0.2em] text-[10px]">{{ item.label }}</span>
                <div v-if="activeId === item.id" class="absolute right-4 w-1.5 h-1.5 rounded-full bg-[var(--bg-color)]"></div>
            </button>
        </nav>
    </aside>
</template>