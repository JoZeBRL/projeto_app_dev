<script setup lang="ts">
import { ref, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import GlobalHeader from '@/components/navigation/GlobalHeader.vue'
import Sidebar from '@/components/navigation/Sidebar.vue'
import AppImage from '@/components/common/UI/AppImage.vue'

// Nota: Removidos imports explícitos de Lucide e Vuetify.
// O auto-import resolve os componentes v-xxx automaticamente.
// Ícones migrados para o padrão MDI nativo do Vuetify.

interface TimelineStep {
    id: number
    title: string
    description: string
    date: string
    status: 'completed' | 'current' | 'pending'
}

interface Reservation {
    id: number
    title: string
    price: string
    location: string
    type: string
    image: string
    expirationDate: string
    clientName: string
    status: 'ativa' | 'expirada' | 'vendida'
}

const authStore = useAuthStore()
const userName = computed(() => authStore.user?.nome || 'Corretor Parceiro')
const userType = computed(() => authStore.user?.tipo || 'broker')

const reservations = ref<Reservation[]>([
    {
        id: 1,
        title: 'Casa em Condomínio no Efapi',
        price: 'R$ 850.000',
        location: 'Efapi, Chapecó - SC',
        type: 'CASA',
        image: 'https://images.unsplash.com/photo-1684778522663-be47e3cbbb2f?auto=format&fit=crop&q=80&w=1080',
        expirationDate: '22/12/2024',
        clientName: 'Ana Silva',
        status: 'ativa',
    }
])

const histories: Record<number, TimelineStep[]> = {
    1: [
        { id: 1, title: 'Reserva Criada', description: 'Reserva iniciada para Ana Silva', date: '15/12/2024', status: 'completed' },
        { id: 2, title: 'Visita Realizada', description: 'Concluída com sucesso', date: '18/12/2024', status: 'current' },
    ]
}

const selectedStatus = ref('todas')
const isGridView = ref(true)
const isHistoryOpen = ref(false)
const selectedId = ref<number | null>(null)

const statusOptions = [
    { value: 'todas', label: 'TODAS' },
    { value: 'ativa', label: 'ATIVAS' },
    { value: 'expirada', label: 'EXPIRADAS' },
    { value: 'vendida', label: 'VENDIDAS' }
]

const filteredReservations = computed(() => {
    if (selectedStatus.value === 'todas') return reservations.value
    return reservations.value.filter(r => r.status === selectedStatus.value)
})

const selectedReservation = computed(() =>
    reservations.value.find(r => r.id === selectedId.value)
)

const openHistory = (id: number) => {
    selectedId.value = id
    isHistoryOpen.value = true
}

const getStatusColor = (status: string) => {
    switch (status) {
        case 'ativa': return '#10B981';
        case 'expirada': return '#EF4444';
        case 'vendida': return '#3B82F6';
        default: return '#71717A';
    }
}
</script>

<template>
    <div class="min-h-screen bg-black text-white font-sans selection:bg-emerald-500/30">
        <GlobalHeader :userName="userName" :userType="userType" />

        <div class="max-w-[1600px] mx-auto flex">
            <Sidebar active-id="reservations" :userName="userName" :userType="userType" />

            <main class="flex-1 pt-32 pb-20 px-8">
                <div class="mb-12 flex flex-col md:flex-row md:items-end justify-between gap-8">
                    <div class="space-y-4">
                        <button @click="$router.back()"
                            class="group flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.3em] text-zinc-500 hover:text-white transition-all">
                            <v-icon icon="mdi-arrow-left" size="18" class="group-hover:-translate-x-1 transition-transform" />
                            Voltar
                        </button>
                        <div>
                            <h1 class="text-6xl font-black uppercase tracking-tighter italic leading-none">
                                Reservas <span class="text-zinc-700">Ativas</span>
                            </h1>
                            <p class="text-[10px] font-black uppercase tracking-[0.4em] text-emerald-500 mt-4">
                                Controle de exclusividade e prazos sob sua gestão
                            </p>
                        </div>
                    </div>

                    <div class="flex items-center gap-4">
                        <div class="flex glass-container !p-1 !rounded-2xl border-white/5">
                            <button @click="isGridView = true"
                                :class="['p-3 rounded-xl transition-all', isGridView ? 'bg-white text-black shadow-lg' : 'text-zinc-500']">
                                <v-icon icon="mdi-view-grid-outline" size="20" />
                            </button>
                            <button @click="isGridView = false"
                                :class="['p-3 rounded-xl transition-all', !isGridView ? 'bg-white text-black shadow-lg' : 'text-zinc-500']">
                                <v-icon icon="mdi-format-list-bulleted" size="20" />
                            </button>
                        </div>
                    </div>
                </div>

                <div class="flex flex-wrap gap-3 mb-12">
                    <button v-for="opt in statusOptions" :key="opt.value" @click="selectedStatus = opt.value" :class="[
                        'px-8 py-3 rounded-[40px] font-black text-[10px] tracking-[0.2em] border transition-all duration-300',
                        selectedStatus === opt.value ? 'bg-white text-black border-white' : 'bg-transparent text-zinc-500 border-white/10 hover:border-white/30'
                    ]">
                        {{ opt.label }}
                    </button>
                </div>

                <div
                    :class="[isGridView ? 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8' : 'flex flex-col gap-6']">
                    <div v-for="item in filteredReservations" :key="item.id"
                        class="group glass-container !p-0 transition-all duration-700 hover:border-emerald-500/30 overflow-hidden"
                        :class="{ 'flex flex-col md:flex-row': !isGridView }">

                        <div :class="[isGridView ? 'h-72 w-full' : 'h-72 md:w-[450px]']"
                            class="relative overflow-hidden">
                            <AppImage :src="item.image" :alt="item.title"
                                className="group-hover:scale-105 transition-transform duration-1000" />

                            <div class="absolute top-6 left-6">
                                <div
                                    class="backdrop-blur-xl bg-black/60 border border-white/10 px-4 py-1.5 rounded-full">
                                    <span class="text-[9px] font-black uppercase tracking-widest text-white">{{
                                        item.type }}</span>
                                </div>
                            </div>

                            <div class="absolute top-6 right-6">
                                <div
                                    class="backdrop-blur-xl bg-black/60 border border-white/10 px-4 py-1.5 rounded-full flex items-center gap-2">
                                    <div class="w-1.5 h-1.5 rounded-full animate-pulse"
                                        :style="{ backgroundColor: getStatusColor(item.status) }"></div>
                                    <span class="text-[9px] font-black uppercase tracking-widest">{{ item.status
                                        }}</span>
                                </div>
                            </div>
                        </div>

                        <div class="p-10 flex flex-col flex-1 justify-between">
                            <div>
                                <h3 class="text-2xl font-black uppercase tracking-tighter mb-2 italic line-clamp-1">
                                    {{ item.title }}
                                </h3>
                                <div class="text-4xl font-black tracking-tighter italic text-white mb-6">
                                    <span class="text-sm not-italic opacity-30 font-bold mr-1">R$</span>
                                    {{ item.price.replace('R$', '').trim() }}
                                </div>

                                <div class="space-y-6 mb-10">
                                    <div class="flex items-center gap-3 text-zinc-400">
                                        <v-icon icon="mdi-map-marker-outline" size="18" color="emerald-500" />
                                        <span class="text-[10px] font-black uppercase tracking-widest">{{ item.location
                                            }}</span>
                                    </div>

                                    <div class="bg-white/[0.02] rounded-[24px] p-6 border border-white/5 space-y-4">
                                        <div class="flex justify-between items-center">
                                            <span
                                                class="text-[9px] text-zinc-500 font-black uppercase tracking-widest">Proponente</span>
                                            <span class="text-xs font-black uppercase tracking-tighter">{{
                                                item.clientName }}</span>
                                        </div>
                                        <div class="flex justify-between items-center">
                                            <span
                                                class="text-[9px] text-zinc-500 font-black uppercase tracking-widest">Expiração</span>
                                            <span
                                                class="text-xs font-black uppercase tracking-tighter text-orange-500">{{
                                                item.expirationDate }}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="flex flex-col gap-4">
                                <button class="btn-premium w-full !text-[10px] italic">
                                    GERENCIAR EXCLUSIVIDADE
                                </button>
                                <button @click="openHistory(item.id)"
                                    class="w-full py-4 rounded-[40px] border border-white/10 font-black text-zinc-400 hover:text-white hover:border-white transition-all text-[10px] tracking-widest uppercase italic">
                                    VER LINHA DO TEMPO
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>

        <v-navigation-drawer v-model="isHistoryOpen" location="right" temporary width="500"
            class="!bg-black !border-l !border-white/10 !text-white !p-0">
            <div class="p-12 h-full flex flex-col bg-black">
                <div class="mb-16 flex justify-between items-center">
                    <div>
                        <h2 class="text-3xl font-black italic tracking-tighter uppercase leading-none">Status da</h2>
                        <h2 class="text-3xl font-black italic tracking-tighter uppercase text-zinc-700 leading-none">
                            Reserva</h2>
                    </div>
                    <v-btn @click="isHistoryOpen = false" icon variant="tonal"
                        class="!bg-zinc-900 !text-white rounded-xl">
                        <v-icon icon="mdi-close" size="24" />
                    </v-btn>
                </div>

                <div v-if="selectedReservation" class="flex-1 overflow-y-auto space-y-12 pr-4 custom-scrollbar">
                    <div v-for="step in histories[selectedId || 0]" :key="step.id"
                        class="relative pl-12 border-l-2 border-zinc-900 ml-2">

                        <div class="absolute -left-[9px] top-0 w-4 h-4 rounded-full border-4 border-black transition-all"
                            :class="[
                                step.status === 'completed' ? 'bg-emerald-500 shadow-[0_0_15px_rgba(16,185,129,0.5)]' :
                                    step.status === 'current' ? 'bg-white shadow-[0_0_15px_rgba(255,255,255,0.5)]' : 'bg-zinc-800'
                            ]">
                        </div>

                        <div class="space-y-2">
                            <span class="text-[9px] font-black text-zinc-600 uppercase tracking-[0.3em] italic">{{
                                step.date }}</span>
                            <h4 class="text-lg font-black uppercase italic tracking-tight"
                                :class="step.status === 'pending' ? 'text-zinc-700' : 'text-white'">
                                {{ step.title }}
                            </h4>
                            <p class="text-zinc-500 text-sm leading-relaxed font-medium">
                                {{ step.description }}
                            </p>
                        </div>
                    </div>
                </div>

                <div class="mt-12 pt-10 border-t border-white/5">
                    <button class="w-full btn-premium !bg-zinc-800 !text-white py-5 italic text-[10px]">
                        SOLICITAR EXTENSÃO DE PRAZO
                    </button>
                </div>
            </div>
        </v-navigation-drawer>
    </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
    width: 4px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: transparent;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background: #27272a;
    border-radius: 10px;
}

:deep(.v-navigation-drawer__content) {
    background-color: black !important;
    scrollbar-width: none;
}
</style>