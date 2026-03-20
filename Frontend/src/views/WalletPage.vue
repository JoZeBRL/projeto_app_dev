<script setup lang="ts">
import { ref, computed } from 'vue';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import Sidebar from '@/components/navigation/Sidebar.vue';
import AppImage from '@/components/common/UI/AppImage.vue';

// Nota: Removidos imports explícitos de Vuetify para evitar conflitos de TS. 
// O Vite auto-importa os componentes v-xxx nativamente.

interface Property {
  id: number;
  title: string;
  address: string;
  price: string;
  area: string;
  bedrooms: number;
  bathrooms: number;
  parking: number;
  image: string;
  status: 'Ativo' | 'Reservado' | 'Vendido';
  views: number;
  favorites: number;
  reservations: number;
}

const props = defineProps<{
  userName: string;
  userType?: 'broker' | 'construction';
}>();

const isGridView = ref(true);

const myProperties = ref<Property[]>([
  {
    id: 1,
    title: 'Apartamento Moderno no Centro',
    address: 'Centro, Chapecó - SC',
    price: 'R$ 450.000',
    area: '95m²',
    bedrooms: 3,
    bathrooms: 2,
    parking: 2,
    image: 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?q=80&w=1080',
    status: 'Ativo',
    views: 245,
    favorites: 18,
    reservations: 3
  },
  {
    id: 2,
    title: 'Casa com Piscina - Bairro Efapi',
    address: 'Efapi, Chapecó - SC',
    price: 'R$ 850.000',
    area: '280m²',
    bedrooms: 4,
    bathrooms: 3,
    parking: 4,
    image: 'https://images.unsplash.com/photo-1613977257363-707ba9348227?q=80&w=1080',
    status: 'Reservado',
    views: 389,
    favorites: 32,
    reservations: 7
  }
]);

const getStatusTheme = (status: string) => {
  switch (status) {
    case 'Ativo': return { color: '#10B981', icon: 'mdi-check-circle-outline' };
    case 'Reservado': return { color: '#F59E0B', icon: 'mdi-clock-outline' };
    case 'Vendido': return { color: '#6B7280', icon: 'mdi-lock-outline' };
    default: return { color: '#FFF', icon: 'mdi-help' };
  }
};
</script>

<template>
  <div class="min-h-screen bg-black text-white selection:bg-emerald-500/30">
    <GlobalHeader :userName="userName" :userType="userType" />

    <div class="max-w-[1600px] mx-auto flex">
      <Sidebar active-id="wallet" />

      <main class="flex-1 pt-32 pb-20 px-8">
        <div class="mb-12 flex flex-col md:flex-row md:items-end justify-between gap-8">
          <div class="space-y-4">
            <button @click="$router.back()"
              class="flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.2em] text-zinc-500 hover:text-white transition-all group">
              <v-icon icon="mdi-arrow-left" size="14" class="group-hover:-translate-x-1 transition-transform" />
              Voltar
            </button>
            <div>
              <h1 class="text-6xl font-black uppercase tracking-tighter italic leading-none">
                Minha <span class="text-zinc-700">Carteira</span>
              </h1>
              <p class="text-[10px] font-black uppercase tracking-[0.4em] text-emerald-500 mt-4">
                {{ myProperties.length }} Unidades sob sua gestão profissional
              </p>
            </div>
          </div>

          <div class="flex items-center gap-4">
            <div class="flex glass-container !p-1 !rounded-2xl border-white/5">
              <button @click="isGridView = true"
                :class="['p-3 rounded-xl transition-all', isGridView ? 'bg-white text-black' : 'text-zinc-500']">
                <v-icon icon="mdi-view-grid" size="18" />
              </button>
              <button @click="isGridView = false"
                :class="['p-3 rounded-xl transition-all', !isGridView ? 'bg-white text-black' : 'text-zinc-500']">
                <v-icon icon="mdi-view-list" size="18" />
              </button>
            </div>

            <button class="btn-premium flex items-center gap-3">
              <v-icon icon="mdi-plus" size="20" />
              NOVO IMÓVEL
            </button>
          </div>
        </div>

        <v-row v-if="isGridView" class="gy-8">
          <v-col v-for="property in myProperties" :key="property.id" cols="12" md="6" lg="4">
            <div class="group glass-container !p-0 transition-all duration-700 hover:border-emerald-500/30">
              <div class="relative h-72 rounded-t-[40px] overflow-hidden">
                <AppImage :src="property.image" :alt="property.title"
                  className="group-hover:scale-105 transition-transform duration-1000" />
                
                <div class="absolute top-6 left-6">
                  <div class="backdrop-blur-xl bg-black/60 border border-white/10 px-4 py-1.5 rounded-full flex items-center gap-2">
                    <div class="w-1.5 h-1.5 rounded-full" :style="{ backgroundColor: getStatusTheme(property.status).color }"></div>
                    <span class="text-[9px] font-black uppercase tracking-widest">{{ property.status }}</span>
                  </div>
                </div>
              </div>

              <div class="p-8 space-y-6">
                <div>
                  <h3 class="text-xl font-black uppercase tracking-tighter mb-1 line-clamp-1 group-hover:text-emerald-400 transition-colors">
                    {{ property.title }}
                  </h3>
                  <p class="text-[9px] font-black text-zinc-500 uppercase tracking-widest flex items-center gap-1 italic">
                    <v-icon icon="mdi-map-marker" size="12" class="text-emerald-500" /> {{ property.address }}
                  </p>
                </div>

                <div class="text-4xl font-black tracking-tighter italic text-white flex items-baseline gap-1">
                  <span class="text-sm not-italic opacity-30 font-bold">R$</span>
                  {{ property.price.replace('R$', '').trim() }}
                </div>

                <div class="grid grid-cols-3 py-6 border-y border-white/5 bg-white/[0.02] rounded-3xl">
                  <div class="text-center border-r border-white/5">
                    <p class="text-xl font-black text-white">{{ property.views }}</p>
                    <p class="text-[8px] font-black text-zinc-500 uppercase tracking-widest">Views</p>
                  </div>
                  <div class="text-center border-r border-white/5">
                    <p class="text-xl font-black text-white">{{ property.favorites }}</p>
                    <p class="text-[8px] font-black text-zinc-500 uppercase tracking-widest">Favs</p>
                  </div>
                  <div class="text-center">
                    <p class="text-xl font-black text-white text-emerald-500">{{ property.reservations }}</p>
                    <p class="text-[8px] font-black text-zinc-500 uppercase tracking-widest">Reservas</p>
                  </div>
                </div>

                <div class="flex items-center justify-between">
                  <div class="flex gap-4 text-zinc-600">
                    <v-tooltip text="Área Total" location="bottom">
                      <template v-slot:activator="{ props }">
                        <v-icon v-bind="props" icon="mdi-ruler-square" size="18" />
                      </template>
                    </v-tooltip>
                    <v-icon icon="mdi-bed-outline" size="18" />
                    <v-icon icon="mdi-car-outline" size="18" />
                  </div>
                  
                  <button class="text-[10px] font-black uppercase tracking-widest text-white hover:text-emerald-400 transition-colors">
                    Gerenciar Unidade
                  </button>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </main>
    </div>
  </div>
</template>

<style scoped>
/* Rigor específico para o arredondamento superior da imagem no card */
:deep(.v-img) {
  border-top-left-radius: 40px !important;
  border-top-right-radius: 40px !important;
}

.line-clamp-1 {
  display: -webkit-box;
  -webkit-line-clamp: 1;
  line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>