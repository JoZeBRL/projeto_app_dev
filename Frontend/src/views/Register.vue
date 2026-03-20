<script setup lang="ts">
import { useRouter } from 'vue-router';
import SignupForm from '@/components/auth/SignupForm.vue';

const router = useRouter();

const handleSignup = (userData: any) => {
  console.log('Dados registrados:', userData);
  router.push('/login');
};
</script>

<template>
  <div class="min-h-screen flex flex-col items-center justify-center p-6 bg-[#1a1a1a] transition-colors">
    <div class="w-full max-w-xl space-y-8">
      
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
        <p class="text-gray-400 text-sm">Acesse a maior rede imobiliária B2B da região</p>
      </div>

      <div class="bg-white border border-gray-200 shadow-xl p-8 rounded-[24px]">
        <SignupForm @signup="handleSignup" @navigate-login="router.push('/login')" />
      </div>

    </div>
  </div>
</template>