<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import Logo from './Logo.vue';
import SearchBar from '../search/SearchBar.vue';
import UserMenu from './UserMenu.vue';

defineProps<{ userName: string; userType?: 'broker' | 'construction' }>();
const emit = defineEmits(['navigate', 'logout']);

const isScrolled = ref(false);
const handleScroll = () => isScrolled.value = window.scrollY > 20;

onMounted(() => window.addEventListener('scroll', handleScroll, { passive: true }));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));
</script>

<template>
    <header :class="[
        'fixed top-0 left-0 right-0 z-[60] transition-all duration-500 border-b',
        isScrolled ? 'glass-container !rounded-none !border-x-0 !border-t-0' : 'bg-transparent border-transparent'
    ]">
        <div class="max-w-7xl mx-auto px-6 h-24 flex items-center justify-between gap-6">
            <Logo class="cursor-pointer hover:scale-105 transition-transform" @click="emit('navigate', 'dashboard')" />
            
            <div v-if="userType === 'broker'" class="flex-1 max-w-xl hidden lg:block transition-all" :class="isScrolled ? 'opacity-100' : 'opacity-90'">
                <div class="h-12 w-full rounded-full border border-[var(--glass-border)] bg-[var(--input-bg)] flex items-center px-4">
                    <span class="text-[var(--label-color)] text-xs font-[900] uppercase tracking-widest">Buscar imóveis...</span>
                </div>
            </div>

            <UserMenu :userName="userName" :userType="userType" @navigate="(id) => emit('navigate', id)" @logout="emit('logout')" />
        </div>
    </header>
</template>