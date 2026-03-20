<script setup lang="ts">
import { useRouter } from 'vue-router';
import SignupForm from '@/components/auth/SignupForm.vue';

const router = useRouter();

const handleSignup = (userData: any) => {
    console.log('Integrando com API conforme docs/frontend.md:', userData);
    router.push('/login');
};
</script>

<template>
    <div class="min-h-screen flex flex-col items-center justify-center bg-black p-6 selection:bg-emerald-500/30">
        <div class="text-center mb-10 space-y-3">
            <div class="flex items-center justify-center gap-3">
                <v-icon icon="mdi-shield-home" size="44" color="white" />
                <h1 class="text-5xl font-black uppercase tracking-tighter italic text-white leading-none">Corretiza</h1>
            </div>
            <p class="text-[11px] font-black uppercase tracking-[0.3em] text-zinc-500">
                Acesse a maior rede imobiliária B2B da região
            </p>
        </div>

        <div class="w-full max-w-[560px]">
            <SignupForm @signup="handleSignup" />
        </div>
    </div>
</template>