<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { 
  AlertCircle, User, Lock, Building2, 
  Briefcase, Eye, EyeOff, ChevronRight 
} from 'lucide-vue-next';

// Props e Emits (Alinhados com Login.vue)
const props = defineProps<{
  error?: string;
}>();

const emit = defineEmits<{
  (e: 'login', payload: { email: string; password: string; type: 'broker' | 'construction' }): void;
  (e: 'navigate-signup'): void;
  (e: 'navigate-forgot-password'): void;
}>();

// Estado (Refs)
const email = ref('');
const password = ref('');
const userType = ref<'broker' | 'construction'>('broker');
const keepLoggedIn = ref(false);
const showPassword = ref(false);

// Lógica de "Lembrar-me" (Mantida conforme solicitado)
onMounted(() => {
  const savedEmail = localStorage.getItem('corretiza_email');
  const savedKeepLoggedIn = localStorage.getItem('corretiza_keepLoggedIn') === 'true';
  const savedUserType = localStorage.getItem('corretiza_userType') as 'broker' | 'construction';

  if (savedUserType) userType.value = savedUserType;
  if (savedKeepLoggedIn && savedEmail) {
    email.value = savedEmail;
    keepLoggedIn.value = true;
  }
});

const isFormValid = computed(() => {
  return email.value.includes('@') && password.value.length >= 6;
});

const handleSubmit = () => {
  if (keepLoggedIn.value) {
    localStorage.setItem('corretiza_email', email.value);
    localStorage.setItem('corretiza_keepLoggedIn', 'true');
    localStorage.setItem('corretiza_userType', userType.value);
  } else {
    localStorage.removeItem('corretiza_email');
    localStorage.removeItem('corretiza_keepLoggedIn');
  }
  
  emit('login', { 
    email: email.value, 
    password: password.value, 
    type: userType.value 
  });
};
</script>

<template>
  <div class="w-full max-w-md mx-auto space-y-6">
    <!-- Toggle Tipo de Usuário -->
    <div class="flex p-1 bg-gray-100 rounded-2xl mb-8">
      <button 
        type="button"
        @click="userType = 'broker'"
        :class="[
          'flex-1 flex items-center justify-center gap-2 py-3 rounded-xl transition-all font-medium text-sm',
          userType === 'broker' ? 'bg-white shadow-sm text-black' : 'text-gray-500 hover:text-gray-700'
        ]"
      >
        <Briefcase :size="18" :class="userType === 'broker' ? 'text-emerald-500' : ''" /> Corretor
      </button>
      <button 
        type="button"
        @click="userType = 'construction'"
        :class="[
          'flex-1 flex items-center justify-center gap-2 py-3 rounded-xl transition-all font-medium text-sm',
          userType === 'construction' ? 'bg-white shadow-sm text-black' : 'text-gray-500 hover:text-gray-700'
        ]"
      >
        <Building2 :size="18" :class="userType === 'construction' ? 'text-emerald-500' : ''" /> Construtora
      </button>
    </div>

    <!-- Formulário -->
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <div class="space-y-2">
        <label class="text-xs font-black uppercase tracking-widest text-gray-400 ml-1">E-mail</label>
        <div class="relative group">
          <User class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-black transition-colors" :size="20" />
          <input 
            v-model="email"
            type="email" 
            placeholder="seu@email.com"
            class="w-full pl-12 pr-4 py-4 bg-[var(--input-background)] border-transparent border-2 rounded-2xl focus:border-black focus:bg-white transition-all outline-none font-medium text-sm"
            required
          />
        </div>
      </div>

      <div class="space-y-2">
        <div class="flex justify-between items-center px-1">
          <label class="text-xs font-black uppercase tracking-widest text-gray-400">Senha</label>
          <button 
            type="button" 
            @click="emit('navigate-forgot-password')"
            class="text-[10px] uppercase font-black tracking-widest text-gray-400 hover:text-black transition-colors"
          >
            Esqueci minha senha
          </button>
        </div>
        <div class="relative group">
          <Lock class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-black transition-colors" :size="20" />
          <input 
            v-model="password"
            :type="showPassword ? 'text' : 'password'" 
            placeholder="••••••••"
            class="w-full pl-12 pr-12 py-4 bg-[var(--input-background)] border-transparent border-2 rounded-2xl focus:border-black focus:bg-white transition-all outline-none font-medium text-sm"
            required
          />
          <button 
            type="button"
            @click="showPassword = !showPassword"
            class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-black transition-colors"
          >
            <Eye v-if="!showPassword" :size="20" />
            <EyeOff v-else :size="20" />
          </button>
        </div>
      </div>

      <!-- Manter Conectado -->
      <div class="flex items-center gap-2 px-1 py-1">
        <label class="relative flex items-center cursor-pointer group">
          <div :class="[
            'w-5 h-5 rounded-md border-2 transition-all flex items-center justify-center',
            keepLoggedIn ? 'bg-black border-black' : 'border-gray-200 group-hover:border-gray-400'
          ]">
            <input 
              type="checkbox" 
              v-model="keepLoggedIn" 
              class="sr-only" 
            />
            <div v-if="keepLoggedIn" class="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse shadow-[0_0_8px_#10B981]"></div>
          </div>
          <span class="ml-3 text-xs font-bold text-gray-400 group-hover:text-gray-600 transition-colors uppercase tracking-widest">Manter conectado</span>
        </label>
      </div>

      <!-- Erros -->
      <div v-if="error" class="bg-red-50 text-red-600 p-4 rounded-2xl flex items-center gap-3 text-sm animate-shake">
        <AlertCircle :size="18" />
        <span class="font-bold">{{ error }}</span>
      </div>

      <!-- Botão Entrar -->
      <button 
        type="submit"
        :disabled="!isFormValid"
        class="w-full bg-black text-white py-4 rounded-[200px] font-black text-lg tracking-tighter flex items-center justify-center gap-2 hover:bg-gray-800 disabled:opacity-30 disabled:grayscale disabled:cursor-not-allowed transition-all relative overflow-hidden group active:scale-[0.98]"
      >
        ENTRAR
        <div class="absolute right-4 w-10 h-10 bg-white rounded-full flex items-center justify-center group-hover:scale-110 transition-transform">
          <ChevronRight class="text-black" :size="20" />
        </div>
      </button>
    </form>

    <!-- Cadastro -->
    <div class="text-center pt-4">
      <button 
        @click="emit('navigate-signup')"
        class="text-xs uppercase font-black tracking-widest text-gray-400 hover:text-black transition-colors"
      >
        Ainda não tem uma conta? <span class="text-black underline underline-offset-4 decoration-emerald-500 decoration-2">Cadastre-se</span>
      </button>
    </div>
  </div>
</template>

<style scoped>
.animate-shake {
  animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both;
}

@keyframes shake {
  10%, 90% { transform: translate3d(-1px, 0, 0); }
  20%, 80% { transform: translate3d(2px, 0, 0); }
  30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
  40%, 60% { transform: translate3d(4px, 0, 0); }
}
</style>