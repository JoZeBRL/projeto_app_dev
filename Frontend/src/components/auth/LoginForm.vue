<script setup lang="ts">
import { ref, computed } from 'vue';
import { User, Lock, Briefcase, Building2, AlertCircle } from 'lucide-vue-next';
import Input from '@/components/ui/Input.vue';
import Button from '@/components/ui/Button.vue';
import Label from '@/components/ui/Label.vue';

const props = defineProps<{ error?: string }>();
const emit = defineEmits(['login', 'navigate-signup', 'navigate-forgot-password']);

const email = ref('');
const password = ref('');
const userType = ref<'broker' | 'construction'>('broker');
const keepLoggedIn = ref(false);

const isFormValid = computed(() => email.value.trim() !== '' && password.value.trim() !== '');

const handleSubmit = () => {
  if (isFormValid.value) {
    emit('login', { email: email.value, password: password.value, type: userType.value });
  }
};
</script>

<template>
  <div class="w-full space-y-6">
    <div class="flex p-1 bg-gray-100 rounded-full w-full max-w-[320px] mx-auto">
      <button
        type="button"
        @click="userType = 'broker'"
        :class="[
          'flex-1 flex items-center justify-center py-2.5 rounded-full transition-all duration-200',
          userType === 'broker' ? 'bg-white text-black shadow-sm' : 'text-gray-500 hover:text-gray-700'
        ]"
      >
        <Briefcase class="w-4 h-4 mr-2" :class="userType === 'broker' ? 'text-[#10B981]' : ''" />
        <span class="text-sm font-medium">Corretor</span>
      </button>
      <button
        type="button"
        @click="userType = 'construction'"
        :class="[
          'flex-1 flex items-center justify-center py-2.5 rounded-full transition-all duration-200',
          userType === 'construction' ? 'bg-white text-black shadow-sm' : 'text-gray-500 hover:text-gray-700'
        ]"
      >
        <Building2 class="w-4 h-4 mr-2" :class="userType === 'construction' ? 'text-[#10B981]' : ''" />
        <span class="text-sm font-medium">Construtora</span>
      </button>
    </div>

    <form @submit.prevent="handleSubmit" class="space-y-4 pt-2">
      <div class="space-y-1">
        <Label for="email">E-mail</Label>
        <Input id="email" v-model="email" type="email" placeholder="Digite aqui" :icon="User" />
      </div>

      <div class="space-y-1">
        <Label for="password">Senha</Label>
        <Input id="password" v-model="password" type="password" placeholder="Digite aqui" :icon="Lock" />
      </div>

      <div class="flex items-center justify-between px-2 py-2">
        <label class="flex items-center space-x-2 cursor-pointer group">
          <div class="relative flex items-center justify-center w-4 h-4 border-2 border-gray-400 rounded group-hover:border-gray-600 transition-colors">
            <input v-model="keepLoggedIn" type="checkbox" class="sr-only" />
            <svg v-if="keepLoggedIn" class="w-3 h-3 text-black" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <span class="text-xs text-gray-500 select-none">Manter logado</span>
        </label>

        <button type="button" @click="emit('navigate-forgot-password')" class="text-xs text-[#A4A6B0] hover:text-gray-900 hover:underline transition-all">
          Esqueci minha senha
        </button>
      </div>

      <div v-if="error" class="bg-red-50 text-red-600 p-3 rounded-lg flex items-center gap-2 text-sm mb-4">
        <AlertCircle class="h-4 w-4" />
        <span>{{ error }}</span>
      </div>

      <Button type="submit" :disabled="!isFormValid" variant="primary" :showArrow="true">
        ENTRAR
      </Button>
    </form>

    <div class="flex justify-center pt-2">
      <button @click="emit('navigate-signup')" class="text-sm text-[#A4A6B0] hover:text-gray-900 transition-all">
        Ainda não tem conta? <span class="text-black font-medium hover:underline">Criar conta</span>
      </button>
    </div>
  </div>
</template>