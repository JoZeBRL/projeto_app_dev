<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps<{ error?: string }>();
const emit = defineEmits(['login', 'navigate-signup']);

const email = ref('');
const password = ref('');
const userType = ref<'broker' | 'construction'>('broker');
const keepLoggedIn = ref(false);
const showPassword = ref(false);

const handleLogin = () => {
    if (email.value && password.value) {
        emit('login', { email: email.value, password: password.value, type: userType.value });
    }
};
</script>

<template>
    <div class="glass-container !p-12 space-y-10 border-white/5 shadow-[0_40px_80px_-15px_rgba(0,0,0,0.8)]">
        <div class="flex p-1.5 bg-black/80 rounded-full border border-white/5 mx-auto w-full">
            <button 
                type="button" 
                @click="userType = 'broker'" 
                :class="[
                    'flex-1 flex items-center justify-center gap-3 py-4 rounded-full transition-all duration-500 font-[900] text-[10px] uppercase tracking-[0.2em]',
                    userType === 'broker' ? 'bg-white text-black shadow-2xl' : 'text-zinc-600 hover:text-zinc-400'
                ]"
            >
                <v-icon icon="mdi-briefcase-variant" :color="userType === 'broker' ? '#10B981' : 'currentColor'" size="18" />
                CORRETOR
            </button>
            <button 
                type="button" 
                @click="userType = 'construction'" 
                :class="[
                    'flex-1 flex items-center justify-center gap-3 py-4 rounded-full transition-all duration-500 font-[900] text-[10px] uppercase tracking-[0.2em]',
                    userType === 'construction' ? 'bg-white text-black shadow-2xl' : 'text-zinc-600 hover:text-zinc-400'
                ]"
            >
                <v-icon icon="mdi-office-building" :color="userType === 'construction' ? '#10B981' : 'currentColor'" size="18" />
                CONSTRUTORA
            </button>
        </div>

        <v-form @submit.prevent="handleLogin" class="space-y-8">
            <div class="space-y-3">
                <label class="v-label ml-5">E-MAIL</label>
                <v-text-field 
                    v-model="email" 
                    variant="solo-filled" 
                    flat 
                    rounded="pill" 
                    placeholder="Digite aqui"
                    prepend-inner-icon="mdi-account-outline" 
                    hide-details 
                    class="premium-input-noir"
                />
            </div>

            <div class="space-y-3">
                <label class="v-label ml-5">SENHA</label>
                <v-text-field 
                    v-model="password" 
                    variant="solo-filled" 
                    flat 
                    rounded="pill"
                    :type="showPassword ? 'text' : 'password'" 
                    placeholder="Digite aqui" 
                    prepend-inner-icon="mdi-lock-outline" 
                    hide-details
                    class="premium-input-noir"
                >
                    <template v-slot:append-inner>
                        <v-btn icon variant="text" density="compact" @click="showPassword = !showPassword" class="mr-1">
                            <v-icon :icon="showPassword ? 'mdi-eye-off-outline' : 'mdi-eye-outline'" size="18" color="zinc-700" />
                        </v-btn>
                    </template>
                </v-text-field>
            </div>

            <div class="flex items-center justify-between px-2">
                <v-checkbox 
                    v-model="keepLoggedIn" 
                    label="MANTER LOGADO" 
                    color="emerald-500" 
                    density="compact"
                    hide-details 
                    class="login-checkbox-noir" 
                />
                <button type="button" class="text-[9px] font-[900] uppercase tracking-[0.2em] text-zinc-600 hover:text-white transition-colors">
                    ESQUECI MINHA SENHA
                </button>
            </div>

            <button 
                type="submit" 
                :disabled="!email || !password"
                class="w-full h-14 bg-zinc-950 hover:bg-zinc-900 border border-white/5 disabled:opacity-30 text-white rounded-full font-[900] text-xs uppercase tracking-[0.4em] flex items-center justify-center relative transition-all active:scale-[0.98]"
            >
                ENTRAR
                <div class="absolute right-4 w-9 h-9 bg-zinc-800 rounded-full flex items-center justify-center border border-white/10 group-hover:bg-zinc-700">
                    <v-icon icon="mdi-chevron-right" size="22" color="white" />
                </div>
            </button>
        </v-form>

        <div class="text-center">
            <p class="text-[10px] font-[900] text-zinc-600 uppercase tracking-[0.2em]">
                AINDA NÃO TEM CONTA? 
                <button @click="emit('navigate-signup')" class="text-white underline underline-offset-4 decoration-emerald-500 ml-2 hover:text-emerald-400">
                    CRIAR CONTA
                </button>
            </p>
        </div>
    </div>
</template>

<style scoped>
.premium-input-noir :deep(.v-field__input) {
    font-weight: 700 !important;
    padding-left: 20px !important;
    color: white !important;
    font-size: 14px !important;
}

.login-checkbox-noir :deep(.v-label) {
    font-size: 9px !important;
    font-weight: 900 !important;
    letter-spacing: 0.2em !important;
    color: #52525b !important;
}
</style>