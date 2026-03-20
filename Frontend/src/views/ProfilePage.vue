<script setup lang="ts">
import { ref, reactive } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import Sidebar from '@/components/navigation/Sidebar.vue';

// Nota: Removidos imports explícitos de Vuetify e Lucide.
// O sistema Vite + unplugin-vue-components resolve o Vuetify.
// Ícones migrados para MDI (Material Design Icons).

const isEditing = ref(false);
const showSuccess = ref(false);
const isDarkMode = ref(true);

const formData = reactive({
    nome: 'Bruno - Black Sistemas',
    email: 'bruno@blacksi.com.br',
    telefone: '(49) 99999-9999',
    creci: 'CRECI-SC 12345',
    imobiliaria: 'Black Sistemas Imobiliários',
    endereco: 'Av. Getúlio Vargas, 100, Centro, Chapecó - SC'
});

const handleSave = () => {
    isEditing.value = false;
    showSuccess.value = true;
    setTimeout(() => (showSuccess.value = false), 3000);
};

const handleCancel = () => {
    isEditing.value = false;
};
</script>

<template>
    <div class="min-h-screen bg-black text-white selection:bg-emerald-500/30">
        <GlobalHeader :user-name="formData.nome" user-type="broker" />

        <div class="max-w-[1600px] mx-auto flex">
            <Sidebar active-id="profile" />

            <main class="flex-1 pt-32 pb-20 px-8">
                <div class="mb-12 space-y-4 max-w-5xl">
                    <button @click="$router.back()"
                        class="group flex items-center gap-2 text-zinc-500 hover:text-white transition-all">
                        <v-icon icon="mdi-arrow-left" size="18" class="group-hover:-translate-x-1 transition-transform" />
                        <span class="text-[10px] font-black uppercase tracking-[0.3em]">Voltar</span>
                    </button>

                    <div class="flex items-center gap-6">
                        <h1 class="text-6xl font-black uppercase tracking-tighter italic leading-none">
                            Meu <span class="text-zinc-700">Perfil</span>
                        </h1>
                        <div
                            class="h-[2px] flex-1 bg-gradient-to-r from-emerald-500/50 to-transparent hidden md:block mt-4">
                        </div>
                    </div>
                    <p class="text-[10px] font-black uppercase tracking-[0.4em] text-zinc-500">
                        Gestão de Identidade e Credenciais CRECI
                    </p>
                </div>

                <v-expand-transition>
                    <div v-if="showSuccess"
                        class="max-w-5xl mb-8 p-5 bg-emerald-500/10 border border-emerald-500/20 rounded-[20px] flex items-center justify-center gap-3 text-emerald-500">
                        <v-icon icon="mdi-check-circle" size="18" />
                        <span class="font-black uppercase text-[11px] tracking-widest">Alterações salvas com
                            sucesso</span>
                    </div>
                </v-expand-transition>

                <section class="max-w-5xl glass-container p-12 mb-8">
                    <div class="flex flex-col md:flex-row items-center gap-10 pb-12 border-b border-white/5 mb-12">
                        <div class="relative group">
                            <v-avatar size="144" class="bg-zinc-950 rounded-[40px] border-2 border-white/10 shadow-2xl group-hover:border-emerald-500/50 transition-all duration-500">
                                <span class="text-5xl font-black text-white italic opacity-20">BK</span>
                            </v-avatar>
                            <v-btn icon="mdi-camera" density="comfortable" position="absolute" location="bottom end" size="small" color="white" class="!text-black shadow-2xl hover:scale-110 transition-all" />
                        </div>

                        <div class="flex-1 text-center md:text-left">
                            <h2 class="text-4xl font-black uppercase tracking-tighter italic mb-3">{{ formData.nome }}
                            </h2>
                            <div class="flex flex-wrap justify-center md:justify-start gap-3">
                                <div
                                    class="px-5 py-2 bg-emerald-500/10 border border-emerald-500/20 rounded-full flex items-center gap-2">
                                    <div class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></div>
                                    <span class="text-[10px] font-black uppercase tracking-widest text-emerald-500">{{
                                        formData.creci }}</span>
                                </div>
                                <div class="px-5 py-2 bg-white/5 border border-white/5 rounded-full">
                                    <span class="text-[10px] font-black uppercase tracking-widest text-zinc-400">{{
                                        formData.imobiliaria }}</span>
                                </div>
                            </div>
                        </div>

                        <button v-if="!isEditing" @click="isEditing = true"
                            class="px-10 py-4 rounded-full border border-white/10 font-black text-[10px] uppercase tracking-[0.2em] hover:bg-white hover:text-black transition-all">
                            Editar Dados
                        </button>
                    </div>

                    <v-form @submit.prevent="handleSave" class="space-y-10">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-10 gap-y-8">
                            <div class="space-y-2">
                                <label class="text-[9px] font-black text-zinc-500 uppercase tracking-[0.3em] ml-4">Nome
                                    Completo</label>
                                <v-text-field v-model="formData.nome" :readonly="!isEditing" prepend-inner-icon="mdi-account-outline" variant="solo-filled" flat
                                    rounded="pill" bg-color="rgba(0,0,0,0.4)" class="premium-field" hide-details />
                            </div>

                            <div class="space-y-2">
                                <label
                                    class="text-[9px] font-black text-zinc-500 uppercase tracking-[0.3em] ml-4">E-mail
                                    Profissional</label>
                                <v-text-field v-model="formData.email" :readonly="!isEditing" type="email" prepend-inner-icon="mdi-email-outline"
                                    variant="solo-filled" flat rounded="pill" bg-color="rgba(0,0,0,0.4)"
                                    class="premium-field" hide-details />
                            </div>

                            <div class="space-y-2">
                                <label
                                    class="text-[9px] font-black text-zinc-500 uppercase tracking-[0.3em] ml-4">Número
                                    do CRECI</label>
                                <v-text-field v-model="formData.creci" :readonly="!isEditing" prepend-inner-icon="mdi-card-account-details-outline" variant="solo-filled" flat
                                    rounded="pill" bg-color="rgba(0,0,0,0.4)" class="premium-field" hide-details />
                            </div>

                            <div class="space-y-2">
                                <label
                                    class="text-[9px] font-black text-zinc-500 uppercase tracking-[0.3em] ml-4">WhatsApp
                                    / Celular</label>
                                <v-text-field v-model="formData.telefone" :readonly="!isEditing" prepend-inner-icon="mdi-whatsapp" variant="solo-filled"
                                    flat rounded="pill" bg-color="rgba(0,0,0,0.4)" class="premium-field" hide-details />
                            </div>

                            <div class="space-y-2 md:col-span-2">
                                <label
                                    class="text-[9px] font-black text-zinc-500 uppercase tracking-[0.3em] ml-4">Endereço
                                    de Atuação</label>
                                <v-text-field v-model="formData.endereco" :readonly="!isEditing" prepend-inner-icon="mdi-map-marker-outline" variant="solo-filled"
                                    flat rounded="pill" bg-color="rgba(0,0,0,0.4)" class="premium-field" hide-details />
                            </div>
                        </div>

                        <v-expand-transition>
                            <div v-if="isEditing" class="flex gap-4 pt-6 border-t border-white/5">
                                <button type="submit" class="btn-premium flex-1 py-5 !text-[11px] italic flex items-center justify-center gap-2">
                                    <v-icon icon="mdi-content-save" size="18" />
                                    SALVAR ALTERAÇÕES
                                </button>
                                <button @click="handleCancel" type="button"
                                    class="px-12 py-5 rounded-[40px] bg-zinc-800 font-black text-[10px] uppercase tracking-widest hover:bg-zinc-700 transition-all italic">
                                    CANCELAR
                                </button>
                            </div>
                        </v-expand-transition>
                    </v-form>
                </section>

                <div class="max-w-5xl grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="glass-container !p-10 space-y-8">
                        <div>
                            <h3 class="text-lg font-black uppercase italic tracking-tighter">Aparência</h3>
                            <p class="text-[9px] font-black text-zinc-500 uppercase tracking-widest mt-1">Configurações
                                de interface</p>
                        </div>
                        <div class="flex gap-4">
                            <v-btn @click="isDarkMode = false" :variant="!isDarkMode ? 'flat' : 'tonal'" :color="!isDarkMode ? 'white' : 'zinc-800'" 
                                class="flex-1 !h-24 !rounded-[30px] !text-black flex flex-col items-center gap-3">
                                <div class="flex flex-col items-center gap-1">
                                    <v-icon icon="mdi-white-balance-sunny" size="24" />
                                    <span class="text-[9px] font-black uppercase tracking-widest">Light</span>
                                </div>
                            </v-btn>
                            <v-btn @click="isDarkMode = true" :variant="isDarkMode ? 'flat' : 'tonal'" :color="isDarkMode ? 'white' : 'zinc-800'"
                                class="flex-1 !h-24 !rounded-[30px] !text-black flex flex-col items-center gap-3">
                                <div class="flex flex-col items-center gap-1">
                                    <v-icon icon="mdi-moon-waning-crescent" size="24" />
                                    <span class="text-[9px] font-black uppercase tracking-widest">Dark</span>
                                </div>
                            </v-btn>
                        </div>
                    </div>

                    <div class="glass-container !p-10 flex flex-col justify-between gap-6">
                        <div>
                            <h3 class="text-lg font-black uppercase italic tracking-tighter">Segurança</h3>
                            <p class="text-[9px] font-black text-zinc-500 uppercase tracking-widest mt-1">Proteção de
                                acesso</p>
                        </div>
                        <div class="space-y-3">
                            <button
                                class="w-full h-14 px-8 rounded-full border border-white/5 bg-white/[0.02] flex items-center justify-between group hover:border-white/20 transition-all">
                                <div class="flex items-center gap-4 text-zinc-400 group-hover:text-white">
                                    <v-icon icon="mdi-shield-lock-outline" size="18" />
                                    <span class="text-[10px] font-black uppercase tracking-widest">Alterar Senha</span>
                                </div>
                                <v-icon icon="mdi-chevron-right" size="16" class="text-zinc-700" />
                            </button>
                            <button
                                class="w-full h-14 px-8 rounded-full border border-red-500/10 bg-red-500/5 flex items-center justify-center gap-4 text-red-500 hover:bg-red-500 hover:text-white transition-all">
                                <v-icon icon="mdi-close-circle-outline" size="18" />
                                <span class="text-[10px] font-black uppercase tracking-widest">Desativar Conta</span>
                            </button>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </div>
</template>

<style scoped>
.premium-field :deep(.v-field__input) {
    font-weight: 700 !important;
    letter-spacing: -0.01em;
    color: white !important;
    padding-left: 24px !important;
}

.premium-field :deep(.v-field--variant-solo-filled) {
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: border-color 0.3s ease;
}

.premium-field :deep(.v-field--focused) {
    border-color: rgba(16, 185, 129, 0.5) !important;
}
</style>