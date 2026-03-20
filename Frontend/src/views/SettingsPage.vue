<script setup>
import { ref, reactive } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import {
    Moon, Sun, Check, Eye, EyeOff, Settings,
    Bell, Lock, Palette, ChevronLeft
} from 'lucide-vue-next';

const props = defineProps({
    userName: { type: String, required: true },
    userType: { type: String, default: 'broker' },
    isDarkMode: { type: Boolean, default: false }
});

const emit = defineEmits(['back', 'logout', 'toggle-dark-mode']);

// Estados para alteração de senha
const showCurrentPassword = ref(false);
const showNewPassword = ref(false);
const showConfirmPassword = ref(false);
const passwordError = ref('');
const passwordSuccess = ref(false);

const passwordForm = reactive({
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
});

// Estados para notificações
const notificationSettings = reactive({
    novosFavoritos: true,
    agendamentosConfirmados: true,
    novosInteressados: true,
    atualizacoesImoveis: true,
    mensagensCorretor: true,
    lembreteVisitas: true,
    alteracoesPreco: false,
    noticiasPlataforma: false
});

const handlePasswordSubmit = () => {
    passwordError.value = '';

    if (!passwordForm.currentPassword || !passwordForm.newPassword || !passwordForm.confirmPassword) {
        passwordError.value = 'Preencha todos os campos';
        return;
    }

    if (passwordForm.newPassword.length < 6) {
        passwordError.value = 'A nova senha deve ter no mínimo 6 caracteres';
        return;
    }

    if (passwordForm.newPassword !== passwordForm.confirmPassword) {
        passwordError.value = 'As senhas não coincidem';
        return;
    }

    // Simulação de sucesso
    passwordSuccess.value = true;
    passwordForm.currentPassword = '';
    passwordForm.newPassword = '';
    passwordForm.confirmPassword = '';

    setTimeout(() => (passwordSuccess.value = false), 3000);
};

const toggleNotification = (key) => {
    notificationSettings[key] = !notificationSettings[key];
};
</script>

<template>
    <div class="min-h-screen bg-gray-50 dark:bg-black transition-colors duration-300">
        <GlobalHeader :user-name="userName" :user-type="userType" :is-dark-mode="isDarkMode"
            @toggle-dark-mode="emit('toggle-dark-mode')" @logout="emit('logout')" />

        <main class="max-w-4xl mx-auto px-6 py-12 pt-32">
            <div class="space-y-8">
                <div>
                    <div class="flex items-center gap-4 mb-4">
                        <button @click="emit('back')"
                            class="flex items-center gap-2 px-4 py-2 rounded-full hover:bg-gray-200 dark:hover:bg-zinc-800 transition-all group">
                            <ChevronLeft class="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
                            <span class="text-sm font-black uppercase tracking-wider">Voltar</span>
                        </button>

                        <div class="flex items-center gap-3">
                            <Settings class="w-8 h-8 text-black dark:text-white" />
                            <h1 class="text-4xl font-black text-black dark:text-white tracking-tight">Configurações</h1>
                        </div>
                    </div>
                    <p class="text-gray-500 font-medium ml-1">Personalize sua experiência na plataforma Corretiza.</p>
                </div>

                <section
                    class="bg-white dark:bg-zinc-900 rounded-[40px] p-8 shadow-sm border border-gray-100 dark:border-zinc-800">
                    <div class="flex items-center gap-4 mb-8 border-b border-gray-100 dark:border-zinc-800 pb-6">
                        <div class="p-3 bg-gray-100 dark:bg-zinc-800 rounded-2xl">
                            <Palette class="w-6 h-6" />
                        </div>
                        <div>
                            <h3 class="text-xl font-black">Aparência</h3>
                            <p class="text-sm text-gray-500">Escolha o tema visual da interface</p>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <button @click="isDarkMode && emit('toggle-dark-mode')" :class="[
                            'p-6 rounded-[32px] border-2 transition-all text-left flex flex-col gap-4',
                            !isDarkMode ? 'border-black bg-gray-50' : 'border-gray-200 dark:border-zinc-800'
                        ]">
                            <div class="flex justify-between items-start">
                                <Sun :class="!isDarkMode ? 'text-orange-500' : 'text-gray-400'" />
                                <div v-if="!isDarkMode" class="bg-black rounded-full p-1">
                                    <Check class="w-3 h-3 text-white" />
                                </div>
                            </div>
                            <div>
                                <span class="font-black block">Light Mode</span>
                                <span class="text-xs text-gray-500">Ideal para ambientes iluminados</span>
                            </div>
                        </button>

                        <button @click="!isDarkMode && emit('toggle-dark-mode')" :class="[
                            'p-6 rounded-[32px] border-2 transition-all text-left flex flex-col gap-4',
                            isDarkMode ? 'border-white bg-zinc-800' : 'border-gray-200'
                        ]">
                            <div class="flex justify-between items-start">
                                <Moon :class="isDarkMode ? 'text-blue-400' : 'text-gray-400'" />
                                <div v-if="isDarkMode" class="bg-white rounded-full p-1">
                                    <Check class="w-3 h-3 text-black" />
                                </div>
                            </div>
                            <div>
                                <span class="font-black block text-black dark:text-white">Dark Mode</span>
                                <span class="text-xs text-gray-500">Conforto visual e elegância Premium</span>
                            </div>
                        </button>
                    </div>
                </section>

                <section
                    class="bg-white dark:bg-zinc-900 rounded-[40px] p-8 shadow-sm border border-gray-100 dark:border-zinc-800">
                    <div class="flex items-center gap-4 mb-8 border-b border-gray-100 dark:border-zinc-800 pb-6">
                        <div class="p-3 bg-gray-100 dark:bg-zinc-800 rounded-2xl">
                            <Lock class="w-6 h-6" />
                        </div>
                        <div>
                            <h3 class="text-xl font-black">Segurança</h3>
                            <p class="text-sm text-gray-500">Mantenha sua conta protegida</p>
                        </div>
                    </div>

                    <v-alert v-if="passwordSuccess" type="success" variant="tonal" class="mb-6 rounded-2xl font-bold">
                        Senha alterada com sucesso!
                    </v-alert>

                    <v-alert v-if="passwordError" type="error" variant="tonal" class="mb-6 rounded-2xl font-bold">
                        {{ passwordError }}
                    </v-alert>

                    <form @submit.prevent="handlePasswordSubmit" class="space-y-4">
                        <div class="grid grid-cols-1 gap-4">
                            <v-text-field v-model="passwordForm.currentPassword" label="Senha Atual"
                                :type="showCurrentPassword ? 'text' : 'password'" variant="outlined" rounded="pill"
                                color="black" @click:append-inner="showCurrentPassword = !showCurrentPassword">
                                <template #append-inner>
                                    <component :is="showCurrentPassword ? EyeOff : Eye" class="cursor-pointer w-5" />
                                </template>
                            </v-text-field>

                            <v-text-field v-model="passwordForm.newPassword" label="Nova Senha"
                                :type="showNewPassword ? 'text' : 'password'" variant="outlined" rounded="pill"
                                color="black" @click:append-inner="showNewPassword = !showNewPassword">
                                <template #append-inner>
                                    <component :is="showNewPassword ? EyeOff : Eye" class="cursor-pointer w-5" />
                                </template>
                            </v-text-field>

                            <v-text-field v-model="passwordForm.confirmPassword" label="Confirmar Nova Senha"
                                :type="showConfirmPassword ? 'text' : 'password'" variant="outlined" rounded="pill"
                                color="black" @click:append-inner="showConfirmPassword = !showConfirmPassword">
                                <template #append-inner>
                                    <component :is="showConfirmPassword ? EyeOff : Eye" class="cursor-pointer w-5" />
                                </template>
                            </v-text-field>
                        </div>

                        <button type="submit"
                            class="w-full py-4 bg-black dark:bg-white text-white dark:text-black rounded-full font-black text-lg hover:scale-[1.01] active:scale-95 transition-all shadow-lg">
                            ATUALIZAR SENHA
                        </button>
                    </form>
                </section>

                <section
                    class="bg-white dark:bg-zinc-900 rounded-[40px] p-8 shadow-sm border border-gray-100 dark:border-zinc-800">
                    <div class="flex items-center gap-4 mb-8 border-b border-gray-100 dark:border-zinc-800 pb-6">
                        <div class="p-3 bg-gray-100 dark:bg-zinc-800 rounded-2xl">
                            <Bell class="w-6 h-6" />
                        </div>
                        <div>
                            <h3 class="text-xl font-black">Notificações</h3>
                            <p class="text-sm text-gray-500">Gerencie seus alertas e avisos</p>
                        </div>
                    </div>

                    <div class="space-y-4">
                        <div v-for="(value, key) in notificationSettings" :key="key"
                            class="flex items-center justify-between p-5 rounded-[24px] border border-gray-100 dark:border-zinc-800 hover:bg-gray-50 dark:hover:bg-zinc-800/50 transition-colors">
                            <div>
                                <p class="font-black capitalize">{{ key.replace(/([A-Z])/g, ' $1') }}</p>
                                <p class="text-xs text-gray-500">Receba alertas em tempo real para esta atividade.</p>
                            </div>
                            <v-switch :model-value="value" @update:model-value="toggleNotification(key)" color="success"
                                inset hide-details></v-switch>
                        </div>
                    </div>
                </section>
            </div>
        </main>
    </div>
</template>

<style scoped>
:deep(.v-field__outline) {
    --v-field-border-width: 2px !important;
    color: #e5e7eb !important;
}

:deep(.v-field--focused .v-field__outline) {
    color: #000 !important;
}

.dark :deep(.v-field--focused .v-field__outline) {
    color: #fff !important;
}
</style>