<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import LoginForm from '@/components/auth/LoginForm.vue';

const router = useRouter();
const authStore = useAuthStore();

const handleLogin = async (data: any) => {
  // Simulando login
  authStore.login({ nome: 'Gestor Corretiza', tipo: data.type }, 'token_auth');
  router.push('/dashboard');
};
</script>

<template>
  <div class="min-h-screen flex flex-col items-center justify-center p-6 bg-[#1a1a1a] transition-colors">
    <div class="w-full max-w-md space-y-8">
      
      <div class="text-center space-y-3">
        <div class="flex items-center justify-center gap-3 select-none">
          <div class="w-12 h-12 bg-white rounded-[12px] flex items-center justify-center shadow-lg">
            <span class="text-black font-black italic tracking-tighter text-3xl">C.</span>
          </div>
          <div class="flex flex-col -space-y-1 text-left">
            <span class="text-white font-black text-xl italic uppercase tracking-tighter">Corretiza</span>
            <span class="text-[8px] font-bold text-gray-400 uppercase tracking-[0.4em] ml-1">Elite Real Estate</span>
          </div>
        </div>
        <p class="text-gray-400 text-sm">Conectando Corretores e Construtoras em Chapecó</p>
      </div>

      <div class="bg-white border border-gray-200 shadow-xl p-8 rounded-[24px]">
        <LoginForm 
          @login="handleLogin" 
          @navigate-signup="router.push('/register')" 
          @navigate-forgot-password="router.push('/forgot-password')"
        />
      </div>

      <div class="text-center text-xs text-gray-500 space-y-1">
        <p>Acesso B2B Habilitado</p>
      </div>
    </div>
  </div>
</template>