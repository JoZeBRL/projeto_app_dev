<script setup>
import { ref, computed } from 'vue'
import GlobalHeader from '@/components/navigation/GlobalHeader.vue'

// Mock Data
const myProperties = ref([
    {
        id: 1,
        title: 'Residencial Premium Tower',
        location: 'Centro, Chapecó',
        price: 'R$ 850.000',
        type: 'Apartamento',
        status: 'active',
        views: 124,
        favorites: 12,
        reservations: 2,
        image: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&q=80&w=800',
        promotionPlan: 'diamond'
    },
    {
        id: 2,
        title: 'Residencial Aurora - Casa 05',
        location: 'Efapi, Chapecó',
        price: 'R$ 420.000',
        type: 'Casa',
        status: 'reserved',
        views: 89,
        favorites: 5,
        reservations: 1,
        image: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=800',
        promotionPlan: 'silver'
    },
    {
        id: 3,
        title: 'Loteamento Solar - Quadra B',
        location: 'Belvedere, Chapecó',
        price: 'R$ 210.000',
        type: 'Terreno',
        status: 'active',
        views: 56,
        favorites: 3,
        reservations: 0,
        image: 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&q=80&w=800',
    }
])

const mockActivities = [
    { id: 1, type: 'view', user: 'Corretor João Silva', date: 'Hoje às 14:30', message: 'Visualizou os detalhes do imóvel' },
    { id: 2, type: 'favorite', user: 'Imobiliária Central', date: 'Hoje às 11:20', message: 'Adicionou aos favoritos' },
    { id: 3, type: 'reservation', user: 'Corretora Maria Oliveira', date: 'Ontem às 16:45', message: 'Solicitou reserva para visita' },
    { id: 4, type: 'message', user: 'Corretor Pedro Santos', date: 'Ontem às 09:15', message: 'Enviou uma dúvida sobre o valor' },
]

// States
const activeTab = ref('all')
const isActivityOpen = ref(false)
const selectedProperty = ref(null)
const searchQuery = ref('')

// Computed
const filteredProperties = computed(() => {
    return myProperties.value.filter(p => {
        const matchesTab = activeTab.value === 'all' || p.status === activeTab.value
        const matchesSearch = p.title.toLowerCase().includes(searchQuery.value.toLowerCase())
        return matchesTab && matchesSearch
    })
})

// Methods
const getStatusDetails = (status) => {
    const map = {
        active: { label: 'Ativo', color: 'text-green-600 bg-green-50 border-green-100' },
        reserved: { label: 'Reservado', color: 'text-amber-600 bg-amber-50 border-amber-100' },
        sold: { label: 'Vendido', color: 'text-blue-600 bg-blue-50 border-blue-100' }
    }
    return map[status] || { label: status, color: 'text-gray-600 bg-gray-50' }
}

const getPlanStyle = (plan) => {
    switch (plan) {
        case 'diamond': return 'text-indigo-500'
        case 'gold': return 'text-amber-500'
        default: return 'text-gray-400'
    }
}

const openActivity = (property) => {
    selectedProperty.value = property
    isActivityOpen.value = true
}
</script>

<template>
    <div class="min-h-screen bg-gray-50">
        <GlobalHeader />

        <main class="max-w-7xl mx-auto px-6 pt-32 pb-12">
            <div class="flex flex-col md:flex-row justify-between items-start gap-6 mb-12">
                <div>
                    <h1 class="text-4xl font-black text-black mb-2 tracking-tight">Meus Imóveis</h1>
                    <p class="text-gray-500 font-medium">Gerencie sua carteira e acompanhe o interesse da rede B2B.</p>
                </div>
                <v-btn color="black" size="x-large" prepend-icon="mdi-plus" class="!rounded-full font-bold shadow-xl">
                    Cadastrar Imóvel
                </v-btn>
            </div>

            <div class="flex flex-col md:flex-row justify-between gap-6 mb-10">
                <div class="flex p-1 bg-gray-200/50 rounded-full w-fit">
                    <button @click="activeTab = 'all'"
                        :class="[activeTab === 'all' ? 'bg-white shadow-sm text-black' : 'text-gray-500']"
                        class="px-8 py-2.5 rounded-full text-sm font-bold transition-all">
                        Todos
                    </button>
                    <button @click="activeTab = 'active'"
                        :class="[activeTab === 'active' ? 'bg-white shadow-sm text-black' : 'text-gray-500']"
                        class="px-8 py-2.5 rounded-full text-sm font-bold transition-all">
                        Ativos
                    </button>
                </div>

                <div class="relative w-full md:w-96">
                    <v-text-field v-model="searchQuery" placeholder="Buscar imóveis..." prepend-inner-icon="mdi-magnify"
                        variant="solo" flat density="comfortable"
                        class="!rounded-full overflow-hidden border border-gray-100" rounded="pill" />
                </div>
            </div>

            <div v-if="filteredProperties.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div v-for="item in filteredProperties" :key="item.id"
                    class="bg-white rounded-[40px] overflow-hidden border border-gray-100 hover:shadow-2xl transition-all group">
                    <div class="relative h-64 overflow-hidden">
                        <v-img :src="item.image" cover
                            class="h-full w-full transition-transform duration-700 group-hover:scale-110" />
                        <div :class="getStatusDetails(item.status).color"
                            class="absolute top-6 right-6 px-4 py-1.5 rounded-full text-[10px] font-black uppercase border">
                            {{ getStatusDetails(item.status).label }}
                        </div>
                    </div>

                    <div class="p-8">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="text-xl font-black text-black leading-tight">{{ item.title }}</h3>
                            <v-icon :class="getPlanStyle(item.promotionPlan)" icon="mdi-sparkles" size="small" />
                        </div>
                        <p class="text-gray-400 text-sm mb-6">{{ item.location }}</p>

                        <div class="flex items-center justify-between mb-8 pb-6 border-b border-gray-50">
                            <span class="text-2xl font-black text-emerald-500">{{ item.price }}</span>
                            <span
                                class="text-[10px] font-black bg-gray-50 px-3 py-1 rounded-full uppercase text-gray-400">
                                {{ item.type }}
                            </span>
                        </div>

                        <div class="grid grid-cols-3 gap-2 mb-8">
                            <div class="text-center">
                                <div class="text-lg font-black text-black">{{ item.views }}</div>
                                <div class="text-[9px] font-bold text-gray-400 uppercase tracking-widest">Views</div>
                            </div>
                            <div class="text-center">
                                <div class="text-lg font-black text-black">{{ item.favorites }}</div>
                                <div class="text-[9px] font-bold text-gray-400 uppercase tracking-widest">Favoritos
                                </div>
                            </div>
                            <div class="text-center">
                                <div class="text-lg font-black text-black">{{ item.reservations }}</div>
                                <div class="text-[9px] font-bold text-gray-400 uppercase tracking-widest">Reservas</div>
                            </div>
                        </div>

                        <div class="space-y-3">
                            <v-btn block color="black" height="56" class="!rounded-full font-black text-sm"
                                @click="openActivity(item)">
                                Ver Atividades
                            </v-btn>
                            <div class="flex gap-3">
                                <v-btn variant="outlined" block class="flex-1 !rounded-full font-bold text-xs"
                                    height="48">Editar</v-btn>
                                <v-btn color="emerald-lighten-4" flat block
                                    class="flex-1 !rounded-full font-bold text-xs text-emerald-darken-2"
                                    height="48">Promover</v-btn>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <v-navigation-drawer v-model="isActivityOpen" location="right" temporary width="400"
            class="!rounded-l-[40px] p-6">
            <div class="flex flex-col h-full">
                <div class="mb-8">
                    <h2 class="text-2xl font-black text-black mb-1">Atividade B2B</h2>
                    <p class="text-sm text-gray-500">Histórico de interações da rede.</p>
                </div>

                <div class="space-y-4 overflow-y-auto">
                    <div v-for="act in mockActivities" :key="act.id" class="p-4 rounded-[24px] bg-gray-50 flex gap-4">
                        <div
                            class="w-10 h-10 rounded-xl bg-white flex items-center justify-center border border-gray-100 shadow-sm">
                            <v-icon size="small" color="emerald">mdi-eye</v-icon>
                        </div>
                        <div class="flex-1">
                            <div class="flex justify-between items-center mb-1">
                                <span class="font-bold text-sm text-black">{{ act.user }}</span>
                                <span class="text-[10px] text-gray-400">{{ act.date }}</span>
                            </div>
                            <p class="text-xs text-gray-500">{{ act.message }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </v-navigation-drawer>
    </div>
</template>

<style scoped>
/* Vuetify overrides para Premium Black */
:deep(.v-btn) {
    text-transform: none;
    letter-spacing: 0;
}

:deep(.v-navigation-drawer__content) {
    padding: 32px !important;
}
</style>