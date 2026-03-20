<script setup lang="ts">
import { useRouter } from 'vue-router';
import LoginForm from '@/components/auth/LoginForm.vue';
import { useAuthStore } from '@/stores/auth';

const router = useRouter();
const authStore = useAuthStore();

const handleLogin = async (data: any) => {
    // Sincronizado com Pinia store
    authStore.login({ nome: 'Gestor Corretiza', tipo: data.type }, 'token_premium_noir');
    router.push('/dashboard');
};
</script>

<template>
    <div class="min-h-screen flex flex-col items-center justify-center bg-black p-6 selection:bg-emerald-500/30">
        <div class="text-center mb-12 space-y-4">
            <div class="flex items-center justify-center gap-4">
                <div class="w-16 h-16 glass-container !rounded-2xl flex items-center justify-center border-white/20 shadow-[0_0_30px_rgba(255,255,255,0.05)]">
                    <v-icon icon="mdi-shield-home" size="40" color="white" />
                </div>
                <h1 class="text-6xl font-[900] uppercase tracking-tighter italic text-white leading-none">CORRETIZA</h1>
            </div>
            <p class="text-[10px] font-[900] uppercase tracking-[0.5em] text-zinc-600">
                CONECTANDO CORRETORES E CONSTRUTORAS EM CHAPECÓ
            </p>
        </div>

        <div class="w-full max-w-[480px]">
            <LoginForm @login="handleLogin" @navigate-signup="router.push('/register')" />
        </div>

        <div class="mt-16 text-center opacity-30 hover:opacity-100 transition-opacity duration-700">
            <p class="text-[9px] font-[900] text-zinc-500 uppercase tracking-[0.3em] mb-1">ACESSO DE TESTE</p>
            <p class="text-[10px] font-bold text-zinc-400">ADMIN@EXEMPLO.COM / 123456</p>
        </div>
    </div>
</template>