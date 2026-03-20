<script setup lang="ts">
import { ref, computed } from 'vue';
import { User, Lock, Briefcase, Building2, Phone, ShieldCheck, Mail } from 'lucide-vue-next';
import Input from '@/components/ui/Input.vue';
import Button from '@/components/ui/Button.vue';
import Label from '@/components/ui/Label.vue';

const emit = defineEmits(['signup', 'navigate-login']);

const formData = ref({
  userType: 'broker' as 'broker' | 'construction',
  fullName: '',
  document: '', // CRECI ou CNPJ
  phone: '',
  email: '',
  password: ''
});

const isFormValid = computed(() => {
  return formData.value.fullName.length > 3 && 
         formData.value.email.includes('@') && 
         formData.value.password.length >= 6;
});

const handleSubmit = () => {
  if (isFormValid.value) emit('signup', formData.value);
};
</script>

<template>
  <div class="w-full space-y-6">
    <div class="flex p-1 bg-gray-100 rounded-full w-full max-w-[320px] mx-auto">
      <button type="button" @click="formData.userType = 'broker'" :class="['flex-1 flex items-center justify-center py-2.5 rounded-full transition-all duration-200', formData.userType === 'broker' ? 'bg-white text-black shadow-sm' : 'text-gray-500 hover:text-gray-700']">
        <Briefcase class="w-4 h-4 mr-2" :class="formData.userType === 'broker' ? 'text-[#10B981]' : ''" />
        <span class="text-sm font-medium">Corretor</span>
      </button>
      <button type="button" @click="formData.userType = 'construction'" :class="['flex-1 flex items-center justify-center py-2.5 rounded-full transition-all duration-200', formData.userType === 'construction' ? 'bg-white text-black shadow-sm' : 'text-gray-500 hover:text-gray-700']">
        <Building2 class="w-4 h-4 mr-2" :class="formData.userType === 'construction' ? 'text-[#10B981]' : ''" />
        <span class="text-sm font-medium">Construtora</span>
      </button>
    </div>

    <form @submit.prevent="handleSubmit" class="space-y-4 pt-2">
      <div class="space-y-1">
        <Label>Nome Completo / Razão Social</Label>
        <Input v-model="formData.fullName" placeholder="Digite aqui" :icon="User" />
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="space-y-1">
          <Label>{{ formData.userType === 'broker' ? 'CRECI' : 'CNPJ' }}</Label>
          <Input v-model="formData.document" placeholder="Documento" :icon="ShieldCheck" />
        </div>
        <div class="space-y-1">
          <Label>Telefone / WhatsApp</Label>
          <Input v-model="formData.phone" placeholder="(00) 00000-0000" :icon="Phone" />
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="space-y-1">
          <Label>E-mail Corporativo</Label>
          <Input v-model="formData.email" type="email" placeholder="Digite aqui" :icon="Mail" />
        </div>
        <div class="space-y-1">
          <Label>Criar Senha</Label>
          <Input v-model="formData.password" type="password" placeholder="Senha forte" :icon="Lock" />
        </div>
      </div>

      <div class="pt-2">
        <Button type="submit" :disabled="!isFormValid" variant="primary" :showArrow="true">
          CRIAR CONTA B2B
        </Button>
      </div>
    </form>

    <div class="flex justify-center pt-2">
      <button @click="emit('navigate-login')" class="text-sm text-[#A4A6B0] hover:text-gray-900 transition-all">
        Já tem uma conta? <span class="text-black font-medium hover:underline">Fazer login</span>
      </button>
    </div>
  </div>
</template>