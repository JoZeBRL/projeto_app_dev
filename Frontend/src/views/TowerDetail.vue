<script setup lang="ts">
import { ref, computed } from 'vue'
import GlobalHeader from '@/components/navigation/GlobalHeader.vue'
import AppImage from '@/components/common/UI/AppImage.vue'

interface Props {
  userName: string
  userType: 'broker' | 'construction'
}

const props = defineProps<Props>()
const emit = defineEmits(['back', 'logout', 'navigate'])

// Estado Reativo
const selectedFloorPlan = ref<'2bed' | '3bed'>('2bed')
const currentImageIndex = ref(0)
const isGalleryOpen = ref(false)
const selectedApartmentId = ref<string | null>(null)

// Dados Mockados (Consistentes com o Manifesto Corretiza)
const galleryImages = [
  { url: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1200', caption: 'Fachada do Residencial Premium Tower' },
  { url: 'https://images.unsplash.com/photo-1713832139677-a03a41b602e3?auto=format&fit=crop&w=1200', caption: 'Hall de Entrada Premium' },
  { url: 'https://images.unsplash.com/photo-1768913109710-a8ed50eeb143?auto=format&fit=crop&w=1200', caption: 'Piscina na Cobertura' }
]

const floorPlans = {
  '2bed': {
    title: 'Planta 2 Dormitórios',
    area: '62 m²', bedrooms: 2, bathrooms: 2, parking: 1,
    features: ['Sala integrada', 'Varanda', 'Cozinha americana'],
    imageUrl: 'https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&w=800'
  },
  '3bed': {
    title: 'Planta 3 Dormitórios',
    area: '95 m²', bedrooms: 3, bathrooms: 2, parking: 2,
    features: ['Suíte master', 'Varanda gourmet', 'Closet'],
    imageUrl: 'https://images.unsplash.com/photo-1585128792020-803d29415281?auto=format&fit=crop&w=800'
  }
}

const availableApartments = [
  { title: 'Apto 201 - R$ 375.000', value: '201' },
  { title: 'Apto 701 - R$ 580.000', value: '701' },
  { title: 'Apto 1201 - R$ 645.000', value: '1201' }
]

const amenities = [
  { icon: 'mdi-waves', label: 'Piscina Rooftop' },
  { icon: 'mdi-dumbbell', label: 'Academia' },
  { icon: 'mdi-shield-check-outline', label: 'Segurança 24h' },
  { icon: 'mdi-home-modern', label: 'Salão de Festas' }
]

const currentPlan = computed(() => floorPlans[selectedFloorPlan.value])

const nextImage = () => currentImageIndex.value = (currentImageIndex.value + 1) % galleryImages.length
const prevImage = () => currentImageIndex.value = (currentImageIndex.value - 1 + galleryImages.length) % galleryImages.length

const handleApartmentChange = (id: any) => {
  selectedApartmentId.value = id
  if (id === '201') selectedFloorPlan.value = '2bed'
  else selectedFloorPlan.value = '3bed'
}
</script>

<template>
  <div class="min-h-screen bg-black text-white selection:bg-emerald-500/30">
    <GlobalHeader :user-name="userName" :user-type="userType" @back="emit('back')" />

    <section class="relative h-[75vh] mt-16 overflow-hidden">
      <transition name="fade-scale" mode="out-in">
        <AppImage :key="currentImageIndex" :src="galleryImages[currentImageIndex].url"
          className="w-full h-full opacity-50 scale-105" />
      </transition>

      <div class="absolute inset-0 bg-gradient-to-t from-black via-black/10 to-transparent" />

      <div class="absolute inset-x-12 top-1/2 -translate-y-1/2 flex justify-between pointer-events-none">
        <v-btn icon="mdi-chevron-left" variant="tonal" color="white"
          class="pointer-events-auto !bg-black/20 backdrop-blur-xl border border-white/5" size="large" @click="prevImage" />
        <v-btn icon="mdi-chevron-right" variant="tonal" color="white"
          class="pointer-events-auto !bg-black/20 backdrop-blur-xl border border-white/5" size="large" @click="nextImage" />
      </div>

      <div class="absolute bottom-20 left-20 max-w-3xl">
        <p class="text-emerald-500 font-black uppercase tracking-[0.4em] text-[10px] mb-6 italic">
          Oportunidade Imobiliária B2B
        </p>
        <h1 class="text-8xl font-black tracking-tighter italic uppercase mb-6 leading-[0.85]">
          Residencial<br />Premium Tower
        </h1>
        <p class="flex items-center gap-3 text-zinc-400 font-black uppercase tracking-[0.2em] text-[11px]">
          <v-icon icon="mdi-map-marker" color="emerald-500" size="18" /> Av. Getúlio Vargas, Centro, Chapecó
        </p>
      </div>

      <button @click="isGalleryOpen = true" class="absolute bottom-20 right-20 btn-premium py-5 !text-xs italic">
        VER GALERIA COMPLETA
      </button>
    </section>

    <main class="max-w-[1600px] mx-auto px-20 py-24 grid grid-cols-1 lg:grid-cols-12 gap-20">

      <div class="lg:col-span-8 space-y-24">
        <div class="glass-container p-16">
          <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-16 gap-8">
            <div>
              <h2 class="text-4xl font-black uppercase tracking-tighter italic">Plantas Disponíveis</h2>
              <p class="text-[10px] font-black uppercase tracking-[0.3em] text-zinc-500 mt-2">Design inteligente para seu cliente</p>
            </div>

            <div class="flex bg-black/40 p-1.5 rounded-[40px] border border-white/5">
              <button v-for="(plan, key) in floorPlans" :key="key"
                @click="selectedFloorPlan = key as '2bed' | '3bed'" :class="[
                  'px-10 py-4 rounded-[40px] text-[11px] font-black uppercase tracking-widest transition-all duration-500',
                  selectedFloorPlan === key ? 'bg-white text-black shadow-2xl' : 'text-zinc-500 hover:text-white'
                ]">
                {{ plan.bedrooms }} Qtd - {{ plan.area }}
              </button>
            </div>
          </div>

          <div class="grid grid-cols-1 xl:grid-cols-2 gap-20 items-center">
            <div class="space-y-12">
              <h3 class="text-3xl font-black text-emerald-500 italic uppercase">{{ currentPlan.title }}</h3>

              <div class="grid grid-cols-2 gap-8">
                <div class="p-8 bg-black/40 rounded-[32px] border border-white/5 hover:border-white/10 transition-colors">
                  <v-icon icon="mdi-ruler-square" color="zinc-700" class="mb-3" />
                  <p class="text-[9px] font-black text-zinc-500 uppercase tracking-widest mb-1">Área Privativa</p>
                  <p class="text-2xl font-black italic">{{ currentPlan.area }}</p>
                </div>
                <div class="p-8 bg-black/40 rounded-[32px] border border-white/5 hover:border-white/10 transition-colors">
                  <v-icon icon="mdi-bed-outline" color="zinc-700" class="mb-3" />
                  <p class="text-[9px] font-black text-zinc-500 uppercase tracking-widest mb-1">Dormitórios</p>
                  <p class="text-2xl font-black italic">{{ currentPlan.bedrooms }}</p>
                </div>
              </div>

              <ul class="space-y-5">
                <li v-for="feat in currentPlan.features" :key="feat" class="flex items-center gap-5 group">
                  <div class="w-2.5 h-2.5 rounded-full bg-emerald-500 shadow-[0_0_15px_rgba(16,185,129,0.5)] group-hover:scale-125 transition-transform" />
                  <span class="text-sm font-black uppercase tracking-widest text-zinc-300 group-hover:text-white transition-colors">
                    {{ feat }}
                  </span>
                </li>
              </ul>
            </div>

            <div class="rounded-[40px] overflow-hidden border border-white/10 shadow-3xl bg-zinc-950">
              <AppImage :src="currentPlan.imageUrl" className="w-full aspect-square object-contain p-8" />
            </div>
          </div>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div v-for="item in amenities" :key="item.label"
            class="glass-container !p-10 text-center hover:border-emerald-500/30 transition-all duration-500 group">
            <v-icon :icon="item.icon" class="mb-6 text-zinc-600 group-hover:text-emerald-500 transition-colors" size="40" />
            <p class="font-black text-[10px] uppercase tracking-[0.2em] text-zinc-500 group-hover:text-white">
              {{ item.label }}
            </p>
          </div>
        </div>
      </div>

      <aside class="lg:col-span-4">
        <div class="sticky top-36">
          <div class="glass-container !p-12 border-emerald-500/10 shadow-[0_0_50px_rgba(0,0,0,0.5)] relative overflow-hidden">
            <div class="absolute -top-24 -right-24 w-64 h-64 bg-emerald-500/5 blur-[100px] rounded-full" />

            <div class="relative z-10">
              <p class="text-emerald-400 font-black text-[11px] tracking-[0.4em] uppercase mb-4 italic">Unidades em Aberto</p>
              <h3 class="text-xs text-zinc-500 uppercase font-black tracking-[0.2em] mb-3">A partir de</h3>
              <p class="text-6xl font-black tracking-tighter italic mb-12">R$ 380.000</p>

              <div class="space-y-8">
                <div class="space-y-4">
                  <label class="text-[10px] font-black text-zinc-500 uppercase tracking-[0.3em] ml-6">Lista de Disponibilidade</label>
                  <v-select 
                    placeholder="Escolha a unidade estratégica..." 
                    :items="availableApartments"
                    item-title="title" 
                    item-value="value" 
                    variant="solo-filled" 
                    flat 
                    rounded="pill"
                    bg-color="rgba(0,0,0,0.6)" 
                    hide-details
                    class="premium-select"
                    @update:model-value="handleApartmentChange" 
                  />
                </div>

                <button class="w-full btn-premium py-6 italic text-base">
                  AGENDAR VISITA TÉCNICA
                </button>

                <button class="w-full py-6 rounded-[40px] border-2 border-white/10 font-black text-zinc-400 hover:text-white hover:border-white transition-all italic tracking-widest text-xs uppercase">
                  SOLICITAR PROPOSTA DIRETA
                </button>
              </div>

              <div class="mt-16 pt-12 border-t border-white/5 grid grid-cols-2 gap-10 text-center">
                <div>
                  <p class="text-[9px] font-black text-zinc-500 uppercase tracking-widest mb-2 italic">Comissão Líquida</p>
                  <p class="text-3xl font-black text-emerald-400 italic">4%</p>
                </div>
                <div>
                  <p class="text-[9px] font-black text-zinc-500 uppercase tracking-widest mb-2 italic">Entrega Prevista</p>
                  <p class="text-2xl font-black italic tracking-tighter text-white">DEZ/2026</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </aside>
    </main>

    <v-dialog v-model="isGalleryOpen" fullscreen transition="dialog-bottom-transition">
      <div class="bg-black w-full h-full flex flex-col p-16">
        <div class="flex justify-between items-center mb-12">
          <div class="flex items-center gap-6">
            <h2 class="text-2xl font-black italic uppercase tracking-tighter">Premium Tower</h2>
            <div class="h-4 w-[1px] bg-white/20" />
            <p class="text-xs font-black uppercase tracking-[0.3em] text-zinc-500">
              Imagens <span class="text-white">0{{ currentImageIndex + 1 }} — 0{{ galleryImages.length }}</span>
            </p>
          </div>
          <v-btn icon="mdi-close" variant="tonal" color="white" class="!bg-white/5" @click="isGalleryOpen = false" />
        </div>
        
        <div class="flex-1 flex items-center justify-center relative group">
          <transition name="fade" mode="out-in">
            <img :key="currentImageIndex" :src="galleryImages[currentImageIndex].url"
              class="max-h-[70vh] rounded-[40px] shadow-[0_50px_100px_rgba(0,0,0,1)] border border-white/5 object-cover" />
          </transition>
        </div>

        <div class="py-16 flex items-center justify-center gap-12">
          <v-btn icon="mdi-arrow-left" variant="outlined" color="white" class="border-white/10" @click="prevImage" />
          <h4 class="text-4xl font-black italic tracking-tighter uppercase text-white">{{ galleryImages[currentImageIndex].caption }}</h4>
          <v-btn icon="mdi-arrow-right" variant="outlined" color="white" class="border-white/10" @click="nextImage" />
        </div>
      </div>
    </v-dialog>
  </div>
</template>

<style scoped>
/* Transições de alta performance */
.fade-scale-enter-active, .fade-scale-leave-active {
  transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
.fade-scale-enter-from { opacity: 0; transform: scale(1.15); }
.fade-scale-leave-to { opacity: 0; transform: scale(0.95); }

.premium-select :deep(.v-field) {
  --v-field-padding-start: 24px;
  font-weight: 900 !important;
}
</style>