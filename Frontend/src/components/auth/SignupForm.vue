<script setup lang="ts">
import { ref, reactive } from 'vue';

const emit = defineEmits(['signup']);

const userType = ref<'broker' | 'construction'>('broker');
const formData = reactive({
    fullName: '',
    creciOrCnpj: '',
    phone: '',
    email: '',
    password: ''
});

const onPhoneInput = (val: string) => {
    const numbers = val.replace(/\D/g, '');
    if (numbers.length <= 2) formData.phone = numbers;
    else if (numbers.length <= 7) formData.phone = `(${numbers.slice(0, 2)}) ${numbers.slice(2)}`;
    else formData.phone = `(${numbers.slice(0, 2)}) ${numbers.slice(2, 7)}-${numbers.slice(7, 11)}`;
};

const submitForm = () => {
    emit('signup', { ...formData, userType: userType.value });
};
</script>

<template>
    <div class="glass-container !p-12 space-y-10">
        <div class="flex p-1.5 bg-black/40 rounded-full border border-white/5 max-w-[380px] mx-auto">
            <button type="button" @click="userType = 'broker'" :class="[
                'flex-1 flex items-center justify-center gap-3 py-4 rounded-full transition-all duration-500 font-black text-[10px] uppercase tracking-widest',
                userType === 'broker' ? 'bg-white text-black shadow-xl' : 'text-zinc-500 hover:text-zinc-300'
            ]">
                <v-icon icon="mdi-briefcase-variant" :color="userType === 'broker' ? '#10B981' : ''" size="18" />
                Corretor
            </button>
            <button type="button" @click="userType = 'construction'" :class="[
                'flex-1 flex items-center justify-center gap-3 py-4 rounded-full transition-all duration-500 font-black text-[10px] uppercase tracking-widest',
                userType === 'construction' ? 'bg-white text-black shadow-xl' : 'text-zinc-500 hover:text-zinc-300'
            ]">
                <v-icon icon="mdi-office-building" :color="userType === 'construction' ? '#10B981' : ''" size="18" />
                Construtora
            </button>
        </div>

        <div class="space-y-8">
            <div class="flex items-center gap-4">
                <div class="w-8 h-8 rounded-full bg-black border border-white/20 flex items-center justify-center text-[11px] font-black text-white">1</div>
                <h2 class="text-xl font-black uppercase tracking-tighter italic text-white">
                    Informações do {{ userType === 'broker' ? 'Corretor' : 'Gestor' }}
                </h2>
            </div>

            <v-form @submit.prevent="submitForm" class="space-y-6">
                <div class="space-y-2">
                    <label class="v-label ml-4">Nome completo</label>
                    <v-text-field v-model="formData.fullName" variant="solo-filled" flat rounded="pill" 
                        placeholder="Digite seu nome completo" bg-color="rgba(0,0,0,0.4)" 
                        prepend-inner-icon="mdi-account-outline" hide-details class="premium-input" />
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="space-y-2">
                        <label class="v-label ml-4">{{ userType === 'broker' ? 'Número do CRECI' : 'CNPJ da Empresa' }}</label>
                        <v-text-field v-model="formData.creciOrCnpj" variant="solo-filled" flat rounded="pill" 
                            placeholder="Digite aqui" bg-color="rgba(0,0,0,0.4)" 
                            prepend-inner-icon="mdi-shield-check-outline" hide-details class="premium-input" />
                    </div>
                    <div class="space-y-2">
                        <label class="v-label ml-4">Telefone / WhatsApp</label>
                        <v-text-field :model-value="formData.phone" variant="solo-filled" flat rounded="pill" 
                            placeholder="(XX) XXXXX-XXXX" bg-color="rgba(0,0,0,0.4)" 
                            prepend-inner-icon="mdi-whatsapp" hide-details class="premium-input"
                            @update:model-value="onPhoneInput" />
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="space-y-2">
                        <label class="v-label ml-4">E-mail</label>
                        <v-text-field v-model="formData.email" type="email" variant="solo-filled" flat rounded="pill" 
                            placeholder="Digite seu e-mail" bg-color="rgba(0,0,0,0.4)" 
                            prepend-inner-icon="mdi-email-outline" hide-details class="premium-input" />
                    </div>
                    <div class="space-y-2">
                        <label class="v-label ml-4">Senha</label>
                        <v-text-field v-model="formData.password" type="password" variant="solo-filled" flat rounded="pill" 
                            placeholder="Digite sua senha" bg-color="rgba(0,0,0,0.4)" 
                            prepend-inner-icon="mdi-lock-outline" hide-details class="premium-input" />
                    </div>
                </div>

                <button type="submit"
                    class="w-full h-16 bg-zinc-900 hover:bg-zinc-800 text-white rounded-full font-black text-xs uppercase tracking-[0.3em] flex items-center justify-center relative transition-all active:scale-95 border border-white/5"
                >
                    CRIAR CONTA
                    <div class="absolute right-4 w-10 h-10 bg-white/10 rounded-full flex items-center justify-center">
                        <div class="w-6 h-6 bg-white/20 rounded-full"></div> </div>
                </button>
            </v-form>
        </div>

        <div class="text-center">
            <button @click="$router.push('/login')" class="group text-[10px] font-black text-zinc-500 uppercase tracking-widest">
                Já tenho uma conta
            </button>
        </div>
    </div>
</template>

<style scoped>
.premium-input :deep(.v-field__input) {
    font-weight: 700 !important;
    letter-spacing: -0.01em !important;
    padding-left: 20px !important;
    color: white !important;
    font-size: 13px !important;
}

.premium-input :deep(.v-field__outline) {
    display: none !important;
}
</style>