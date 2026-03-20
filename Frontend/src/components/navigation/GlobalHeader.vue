<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import Logo from './Logo.vue';
import SearchBar from '../search/SearchBar.vue';
import UserMenu from './UserMenu.vue';

interface Props {
    userName: string;
    userType?: 'broker' | 'construction';
    isDarkMode?: boolean;
}

const props = withDefaults(defineProps < Props > (), {
    userType: 'broker',
    isDarkMode: false
});

const emit = defineEmits < {
    (e: 'back'): void;
    (e: 'navigate', destination: string): void;
    (e: 'logout'): void;
    (e: 'search', params: any): void;
    (e: 'toggle-dark-mode'): void;
}> ();

// Estados Reativos
const isScrolled = ref(false);
const isMenuOpen = ref(false);
const searchParams = ref({
    query: '', location: '', type: '', price: '', beds: '', parking: '', baths: ''
});

// Lógica de Scroll para Efeito Floating
const handleScroll = () => {
    isScrolled.value = window.scrollY > 20;
};

onMounted(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });
});

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
});

// Handlers
const onSearch = () => {
    emit('search', { ...searchParams.value });
};

const handleNavigation = (destination: string) => {
    isMenuOpen.value = false;
    emit('navigate', destination);
};
</script>

<template>
    <header :class="[
        'fixed left-0 right-0 z-[60] transition-all duration-700 ease-in-out',
        isScrolled ? 'top-4 px-6' : 'top-0 px-0'
    ]">
        <div :class="[
            'mx-auto transition-all duration-700 border border-white/5 backdrop-blur-xl',
            isScrolled
                ? 'max-w-6xl rounded-[40px] bg-black/90 py-2 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.6)] border-white/10'
                : 'max-w-full rounded-none bg-black py-4 border-b border-white/10'
        ]">
            <div class="px-8 flex items-center justify-between gap-6">

                <div class="flex items-center gap-4">
                    <v-btn v-if="isScrolled" icon="mdi-arrow-left" variant="text" color="white" size="small"
                        class="animate-fade-in" @click="emit('back')"></v-btn>

                    <Logo :compact="isScrolled" class="cursor-pointer hover:scale-105 transition-transform duration-300"
                        @click="handleNavigation('dashboard')" />
                </div>

                <div v-if="userType === 'broker'" class="hidden lg:block flex-1 max-w-lg transition-all duration-500"
                    :class="isScrolled ? 'scale-95' : 'scale-100'">
                    <SearchBar 
                        :search-query="searchParams.query"
                        :location="searchParams.location"
                        :property-type="searchParams.type"
                        :price-range="searchParams.price"
                        :bedrooms="searchParams.beds"
                        :parking-spots="searchParams.parking"
                        :bathrooms="searchParams.baths"
                        :compact="isScrolled" 
                        @update:search-query="searchParams.query = $event"
                        @search="onSearch" 
                    />
                </div>

                <div class="flex items-center gap-2 md:gap-6">
                    <nav class="hidden xl:flex items-center gap-8 text-[10px] font-black uppercase tracking-[0.2em]">
                        <button @click="handleNavigation('agendamentos')"
                            class="text-zinc-500 hover:text-white transition-colors">AGENDAMENTOS</button>
                        <button @click="handleNavigation('negociacoes')"
                            class="text-zinc-500 hover:text-white transition-colors">NEGOCIAÇÕES</button>
                    </nav>

                    <div class="h-6 w-[1px] bg-white/10 hidden md:block"></div>

                    <div class="flex items-center gap-1">
                        <v-btn icon variant="text" color="white" size="small" @click="emit('toggle-dark-mode')">
                            <v-icon :icon="isDarkMode ? 'mdi-white-balance-sunny' : 'mdi-moon-waning-crescent'"
                                size="20"></v-icon>
                        </v-btn>

                        <v-btn class="md:hidden" icon="mdi-menu" variant="text" color="white"
                            @click="isMenuOpen = true"></v-btn>

                        <div class="hidden md:block">
                            <UserMenu 
                                :userName="userName" 
                                :userType="userType" 
                                :compact="isScrolled"
                                @navigate="handleNavigation"
                                @logout="emit('logout')" 
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <v-navigation-drawer v-model="isMenuOpen" location="right" temporary width="320"
        class="!bg-black !border-l !border-white/10">
        <div class="p-8 flex flex-col h-full">
            <div class="mb-10 flex justify-between items-center">
                <Logo compact />
                <v-btn icon="mdi-close" variant="text" color="white" @click="isMenuOpen = false"></v-btn>
            </div>

            <div class="space-y-8">
                <div class="pb-6 border-b border-white/5">
                    <p class="text-[10px] font-black text-zinc-600 uppercase tracking-[3px] mb-2 italic">ACESSO RESTRITO</p>
                    <p class="text-2xl font-black text-white uppercase italic tracking-tighter leading-none">{{ userName }}</p>
                    <p class="text-[9px] font-black text-white/40 uppercase tracking-[0.2em] mt-2">
                        {{ userType === 'broker' ? 'Corretor Autorizado' : 'Construtora Credenciada' }}
                    </p>
                </div>

                <nav class="flex flex-col gap-2">
                    <button v-for="item in ['Dashboard', 'Negociacoes', 'Agendamentos', 'Favoritos', 'Perfil']"
                        :key="item"
                        class="text-left py-4 text-xl font-[900] uppercase italic tracking-tighter text-zinc-500 hover:text-white transition-all border-b border-white/5 last:border-0"
                        @click="handleNavigation(item.toLowerCase())">
                        {{ item }}
                    </button>
                </nav>
            </div>

            <v-spacer></v-spacer>

            <v-btn block height="56" color="white" variant="elevated" 
                class="!text-black !font-black !tracking-[0.2em] !rounded-[40px] italic shadow-2xl" 
                @click="emit('logout')">
                SAIR DA CONTA
            </v-btn>
        </div>
    </v-navigation-drawer>
</template>

<style scoped>
.animate-fade-in {
    animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateX(-10px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>