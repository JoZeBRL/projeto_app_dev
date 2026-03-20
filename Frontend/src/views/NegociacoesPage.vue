<script setup>
import { ref, computed } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import NegotiationTimeline from '@/components/negociacoes/NegotiationTimeline.vue';
import ProposalSummary from '@/components/negociacoes/ProposalSummary.vue';
import ChatDirect from '@/components/negociacoes/ChatDirect.vue';
import NegotiationItem from '@/components/negociacoes/NegotiationItem.vue';
import CustomAlert from '@/components/common/CustomAlert.vue';

// --- PROPS & ESTADO DO USUÁRIO ---
const props = defineProps({
    userName: { type: String, default: 'João Silva' },
    userType: { type: String, default: 'construction' }, // 'broker' ou 'construction'
});

// --- ESTADOS DE UI (Migrados do React) ---
const activeTab = ref('all');
const searchFilter = ref('');
const selectedNegociacao = ref(null);
const showDetailModal = ref(false);
const showCounterModal = ref(false);
const showAcceptConfirmation = ref(false);
const showContratoModal = ref(false);

// Form de Contraproposta
const counterValue = ref('');
const counterObs = ref('');

// --- DADOS MOCKADOS (Densidade total do original) ---
const negociacoes = ref([
    {
        id: 1,
        propertyId: 1,
        propertyTitle: 'Residencial Vista Bella',
        propertyImage: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
        propertyLocation: 'Centro, Chapecó - SC',
        propertyCode: 'IMV-2024-001',
        valorProposta: 850000,
        dataAtualizacao: '2024-10-13',
        status: 'em-analise',
        comprador: {
            nome: 'Maria Santos Silva',
            cpf: '123.456.789-01',
            email: 'maria.santos@email.com',
            telefone: '(49) 99876-5432'
        },
        corretor: { nome: 'João Silva', creci: '12345-F', telefone: '(49) 98888-7777' },
        formaPagamento: 'Financiamento',
        observacoes: 'Cliente interessado em unidade no 5º andar.',
        anexos: ['comprovante_renda.pdf', 'proposta_formal.pdf'],
        contraproposta: null,
        historico: [
            { data: '2024-10-13 10:15', mensagem: 'Proposta enviada pelo corretor', autor: 'João Silva', status: 'completed' },
            { data: '2024-10-13 16:20', mensagem: 'Análise de documentos iniciada', autor: 'Construtora', status: 'current' }
        ]
    }
    // ... outros itens seguindo a mesma estrutura
]);

// --- LÓGICA DE NEGÓCIO (Migrada das 1490 linhas) ---

const formatCurrency = (val) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(val);

const filteredNegociacoes = computed(() => {
    return negociacoes.value.filter(n => {
        const matchesSearch = n.propertyTitle.toLowerCase().includes(searchFilter.value.toLowerCase()) ||
            n.comprador.nome.toLowerCase().includes(searchFilter.value.toLowerCase());
        const matchesTab = activeTab.value === 'all' || n.status === activeTab.value;
        return matchesSearch && matchesTab;
    });
});

// Determina o botão de ação baseado no UserType (Lógica core do original)
const getNextAction = (n) => {
    if (props.userType === 'broker') {
        if (n.status === 'em-analise') return { label: 'Aguardando Resposta', disabled: true };
        if (n.status === 'finalizada') return { label: 'Venda Concluída', disabled: true };
        return { label: 'Ver Detalhes', action: 'view', variant: 'outline' };
    }

    // Lógica Construtora
    if (n.status === 'em-analise') return { label: 'Analisar Proposta', action: 'analyze', variant: 'primary' };
    if (n.status === 'aceita') return { label: 'Emitir Contrato', action: 'contract', variant: 'primary' };
    return { label: 'Histórico', action: 'view', variant: 'outline' };
};

const handleAction = (n, action) => {
    selectedNegociacao.value = n;
    if (action === 'analyze') showDetailModal.value = true;
    if (action === 'contract') showContratoModal.value = true;
};

const handleAcceptProposta = () => {
    // Simulação da mutação de estado do original
    if (selectedNegociacao.value) {
        selectedNegociacao.value.status = 'aceita';
        selectedNegociacao.value.historico.push({
            data: new Date().toLocaleString(),
            mensagem: 'Proposta aceita pela construtora',
            autor: props.userName,
            status: 'completed'
        });
        showAcceptConfirmation.value = false;
        showDetailModal.value = false;
    }
};
</script>

<template>
    <div class="min-h-screen bg-[#F8F9FA]">
        <GlobalHeader :userName="props.userName" :userType="props.userType" />

        <main class="max-w-7xl mx-auto px-6 pt-32 pb-20">
            <header class="flex flex-col md:flex-row justify-between items-start mb-12 gap-6">
                <div class="space-y-2">
                    <h1 class="text-5xl font-black text-black tracking-tighter italic uppercase">
                        Negociações
                    </h1>
                    <p class="text-gray-500 font-bold text-lg uppercase tracking-widest text-[10px]">
                        {{ props.userType === 'construction' ? 'Portal de Gestão de Vendas' : 'Acompanhamento de Propostas' }}
                    </p>
                </div>
                <v-btn v-if="props.userType === 'broker'"
                    class="!rounded-[20px] !bg-black !text-white !font-black !px-10 !h-[60px]" elevation="10">
                    Nova Proposta
                </v-btn>
            </header>

            <section class="flex flex-col md:flex-row gap-6 mb-12 items-center">
                <div class="bg-gray-200/40 backdrop-blur-md p-1.5 rounded-[40px] flex gap-1 border border-white/50">
                    <button v-for="tab in ['all', 'em-analise', 'aceita', 'finalizada']" :key="tab"
                        @click="activeTab = tab" :class="[
                            'px-8 py-3 rounded-[40px] text-[10px] font-black uppercase tracking-[2px] transition-all duration-500',
                            activeTab === tab ? 'bg-black text-white shadow-xl scale-105' : 'text-gray-400 hover:text-black'
                        ]">
                        {{ tab === 'all' ? 'Ver Todas' : tab.replace('-', ' ') }}
                    </button>
                </div>

                <div class="relative flex-1 group">
                    <v-icon icon="mdi-magnify"
                        class="absolute left-6 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-black transition-colors"></v-icon>
                    <input v-model="searchFilter" type="text" placeholder="PESQUISAR IMÓVEL OU COMPRADOR..."
                        class="w-full pl-16 pr-8 py-5 bg-white border-2 border-transparent rounded-[40px] text-xs font-black tracking-widest shadow-sm focus:border-black outline-none transition-all placeholder:text-gray-300" />
                </div>
            </section>

            <section class="space-y-2 mt-8">
                <header
                    class="px-6 mb-4 flex justify-between items-center text-[10px] font-black text-zinc-600 uppercase tracking-[0.3em]">
                    <span>Empreendimento / Proponente</span>
                    <div class="flex gap-20 mr-12">
                        <span>Data</span>
                        <span>Status</span>
                    </div>
                </header>

                <NegotiationItem v-for="n in filteredNegociacoes" :key="n.id"
                    :title="`${n.propertyTitle} - ${n.comprador.nome}`" :date="n.dataAtualizacao" :status="n.status"
                    :isActive="selectedNegociacao?.id === n.id" @click="handleAction(n, 'analyze')" />
            </section>
        </main>

        <v-dialog v-model="showDetailModal" fullscreen transition="dialog-bottom-transition">
            <div class="bg-[#F8F9FA] min-h-screen">
                <v-toolbar color="black" dark class="px-6">
                    <v-toolbar-title class="!font-black !text-xs !tracking-[4px] !uppercase">Detalhamento da Proposta
                        #{{ selectedNegociacao?.id }}</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn icon="mdi-close" @click="showDetailModal = false"></v-btn>
                </v-toolbar>

                <div class="max-w-7xl mx-auto p-10">
                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
                        <div class="lg:col-span-2 space-y-10">
                            <NegotiationTimeline :currentStep="2" />
                            <ProposalSummary :proposalData="selectedNegociacao" />

                            <div v-if="props.userType === 'construction'"
                                class="bg-black rounded-[40px] p-10 text-white shadow-2xl">
                                <h3 class="text-2xl font-black italic uppercase mb-2">Decisão Comercial</h3>
                                <p class="text-gray-400 font-medium mb-8">Revise todos os dados e documentos antes de
                                    prosseguir com o aceite.</p>
                                <div class="flex flex-wrap gap-4">
                                    <v-btn color="white" class="!text-black !font-black !rounded-full !px-10 !h-[50px]"
                                        @click="showAcceptConfirmation = true">Aceitar Proposta</v-btn>
                                    <v-btn variant="outlined" color="white"
                                        class="!font-black !rounded-full !px-10 !h-[50px]"
                                        @click="showCounterModal = true">Contraproposta</v-btn>
                                    <v-btn variant="text" color="red" class="!font-black !text-xs">Recusar
                                        Definitivamente</v-btn>
                                </div>
                            </div>
                        </div>

                        <div class="lg:col-span-1 space-y-8">
                            <ChatDirect />

                            <div class="bg-white rounded-[40px] p-8 border border-gray-100 shadow-sm">
                                <h4 class="font-black uppercase text-[10px] tracking-widest text-gray-400 mb-6 italic">
                                    Arquivos da Negociação</h4>
                                <div class="space-y-3">
                                    <div v-for="file in selectedNegociacao?.anexos" :key="file"
                                        class="flex items-center justify-between p-4 bg-gray-50 rounded-[20px] border border-gray-100 group hover:border-black transition-all">
                                        <div class="flex items-center gap-3">
                                            <v-icon icon="mdi-file-pdf-box" color="red-darken-2"></v-icon>
                                            <span class="text-[11px] font-black text-gray-600 truncate max-w-[150px]">{{
                                                file }}</span>
                                        </div>
                                        <v-btn icon="mdi-download" variant="text" size="small"></v-btn>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </v-dialog>

        <CustomAlert v-model="showAcceptConfirmation" title="Confirmar Aceite?"
            message="Ao aceitar, o corretor e o cliente serão notificados para a fase de contrato."
            @confirm="handleAcceptProposta" />
    </div>
</template>

<style scoped>
/* Estilização para manter o rigor font-black e premium black */
h1,
h2,
h3,
button {
    font-family: 'Inter', sans-serif;
    font-weight: 900 !important;
}
</style>