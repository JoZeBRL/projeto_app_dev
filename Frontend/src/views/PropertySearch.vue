<script setup lang="ts">
import { ref, computed } from 'vue';
import { Ruler, Bath, Bed, Car, Handshake, Copy, Heart, Calendar as CalendarIcon } from 'lucide-vue-next';

// --- Estado e Dados ---
const favorites = ref<Set<number>>(new Set());
const email = ref('');
const isReserveModalOpen = ref(false);
const selectedProperty = ref<any>(null);

const properties = [
  { id: 1, title: 'Apartamento de Luxo no Centro', address: 'Rua Nereu Ramos, Centro, Chapecó', price: 'R$ 3.200/mês', area: '85 m²', bedrooms: 3, bathrooms: 2, parking: 1, image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80', badge: 'Aluguel', type: 'Apartamento', isReserved: true, commission: '50%' },
  { id: 2, title: 'Casa Moderna no Efapi', address: 'Rua das Flores, Efapi, Chapecó', price: 'R$ 680.000', area: '120 m²', bedrooms: 3, bathrooms: 2, parking: 2, image: 'https://images.unsplash.com/photo-1627141234469-24711efb373c?w=800&q=80', badge: 'Venda', type: 'Casa', commission: '6%' },
  { id: 3, title: 'Sobrado Familiar no Jardim América', address: 'Av. Porto Alegre, Jardim América, Chapecó', price: 'R$ 850.000', area: '180 m²', bedrooms: 4, bathrooms: 3, parking: 2, image: 'https://images.unsplash.com/photo-1592928302636-c83cf1e1c887?w=800&q=80', badge: 'Venda', type: 'Sobrado', commission: '5%' },
  { id: 4, title: 'Residencial Premium Tower - 15 Andares', address: 'Av. Getúlio Vargas, Centro, Chapecó', price: 'A partir de R$ 380.000', area: '62 m² a 95 m²', bedrooms: 2, bathrooms: 2, parking: 2, image: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&q=80', badge: 'Venda', type: 'Residencial', commission: '4%' },
  { id: 5, title: 'Apartamento Bela Vista', address: 'Rua Marechal Bormann, Bela Vista, Chapecó', price: 'R$ 450.000', area: '75 m²', bedrooms: 2, bathrooms: 1, parking: 1, image: 'https://images.unsplash.com/photo-1603072388139-565853396b38?w=800&q=80', badge: 'Venda', type: 'Apartamento', commission: '5%' },
  { id: 6, title: 'Casa Premium no São Cristóvão', address: 'Rua dos Pioneiros, São Cristóvão, Chapecó', price: 'R$ 1.200.000', area: '250 m²', bedrooms: 4, bathrooms: 4, parking: 3, image: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80', badge: 'Venda', type: 'Casa', commission: '6%' },
  { id: 7, title: 'Terreno Comercial Eldorado', address: 'BR-282, Eldorado, Chapecó', price: 'R$ 320.000', area: '500 m²', bedrooms: 0, bathrooms: 0, parking: 0, image: 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=800&q=80', badge: 'Venda', type: 'Terreno', hasDiscount: true, discountPercentage: '25%', commission: '5%' },
  { id: 8, title: 'Chácara no Palmital', address: 'Linha Palmital, Chapecó', price: 'R$ 4.500/mês', area: '2.000 m²', bedrooms: 3, bathrooms: 2, parking: 4, image: 'https://images.unsplash.com/photo-1560185007-cde436f6a4d0?w=800&q=80', badge: 'Temporada', type: 'Chácara', commission: '10%' },
  { id: 9, title: 'Apartamento Duplex no Centro', address: 'Rua Benjamin Constant, Centro, Chapecó', price: 'R$ 720.000', area: '140 m²', bedrooms: 3, bathrooms: 3, parking: 2, image: 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&q=80', badge: 'Venda', type: 'Apartamento', commission: '6%' },
  { id: 10, title: 'Cobertura Premium Jardim Itália', address: 'Rua Itália, Jardim Itália, Chapecó', price: 'R$ 980.000', area: '200 m²', bedrooms: 3, bathrooms: 3, parking: 3, image: 'https://images.unsplash.com/photo-1600607686527-6fb886090705?w=800&q=80', badge: 'Venda', type: 'Cobertura' },
  { id: 11, title: 'Sala Comercial Beira-Rio', address: 'Av. Fernando Machado, Beira-Rio, Chapecó', price: 'R$ 3.200/mês', area: '80 m²', bedrooms: 0, bathrooms: 2, parking: 2, image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80', badge: 'Aluguel', type: 'Sala Comercial' },
  { id: 12, title: 'Casa Condomínio Fechado', address: 'Rua das Palmeiras, Maria Goretti, Chapecó', price: 'R$ 890.000', area: '160 m²', bedrooms: 3, bathrooms: 3, parking: 2, image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=80', badge: 'Venda', type: 'Casa' },
];

// --- Métodos ---
const toggleFavorite = (id: number) => {
  if (favorites.value.has(id)) {
    favorites.value.delete(id);
  } else {
    favorites.value.add(id);
  }
};

const handleCopyCode = (code: string) => {
  navigator.clipboard.writeText(code);
  alert('Código copiado!');
};

const handleSubscribe = () => {
  console.log('Newsletter subscription:', email.value);
  email.value = '';
  alert('Obrigado por se inscrever em nossa newsletter!');
};

const openReserveModal = (property: any) => {
  if (!property.isReserved) {
    selectedProperty.value = property;
    isReserveModalOpen.value = true;
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 flex flex-col w-full">
    
    <div class="relative w-full h-[350px] bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1600&q=80');">
      <div class="absolute inset-0 bg-black/60"></div>
      <section class="absolute inset-0 flex items-center justify-center px-6">
        <div class="max-w-6xl mx-auto text-center space-y-4">
          <h1 class="text-white text-4xl md:text-5xl font-bold tracking-tight">
            Qual imóvel vamos<br class="md:hidden" /> vender hoje?
          </h1>
          <p class="text-white/90 max-w-2xl mx-auto text-lg">
            Descubra as melhores oportunidades em Chapecó e região. Encontre imóveis ideais para apresentar e negociar com seus clientes.
          </p>
        </div>
      </section>
    </div>

    <section class="py-12 px-6 bg-gray-50 relative z-10 w-full">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          
          <template v-for="(property, index) in properties" :key="property.id">
            
            <div 
              @click="$router.push(`/property/${property.id}`)"
              class="rounded-2xl overflow-hidden hover:-translate-y-1 transition-all duration-300 group cursor-pointer flex flex-col bg-white border border-gray-100 shadow-sm"
            >
              <div class="relative h-48 flex-shrink-0 overflow-hidden bg-gray-200">
                <img :src="property.image" :alt="property.title" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
                
                <div class="absolute top-3 left-3 flex flex-col items-start space-y-1.5">
                  <span :class="['px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider', property.badge === 'Aluguel' ? 'bg-white text-gray-900' : 'bg-gray-900 text-white']">
                    {{ property.badge }}
                  </span>
                  
                  <div class="relative group/tooltip">
                    <span class="px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-[#10B981] text-white flex items-center gap-1 shadow-sm">
                      Comissão: {{ property.commission || (property.badge === 'Aluguel' ? '50%' : '6%') }}
                    </span>
                    <div class="absolute left-0 top-full mt-2 w-64 p-4 rounded-xl border border-gray-100 bg-white text-gray-900 shadow-xl opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-50">
                      <div class="flex items-center gap-2 text-[#10B981] mb-2">
                        <Handshake class="h-4 w-4" />
                        <h4 class="font-bold text-sm text-gray-900">Sobre a Comissão</h4>
                      </div>
                      <p class="text-xs text-gray-600 leading-relaxed mb-2">Este é o percentual de ganho garantido para você, corretor parceiro.</p>
                      <p class="text-[10px] text-gray-400 italic border-t border-gray-50 pt-2">* Valores baseados na política da imobiliária.</p>
                    </div>
                  </div>
                </div>

                <button 
                  @click.stop="toggleFavorite(property.id)"
                  class="absolute top-3 right-3 p-2 rounded-full bg-white/90 hover:bg-white transition-all shadow-sm z-10"
                >
                  <Heart :class="['w-4 h-4 transition-colors', favorites.has(property.id) ? 'fill-red-500 text-red-500' : 'text-gray-400']" />
                </button>
              </div>

              <div class="p-4 flex flex-col flex-1">
                <div class="flex items-center justify-between mb-2">
                  <h3 class="text-gray-500 text-xs font-semibold uppercase tracking-wider">{{ property.type }}</h3>
                  <button @click.stop="handleCopyCode(`${property.type.substring(0, 2).toUpperCase()}${8000 + property.id}`)" class="flex items-center gap-1.5 px-2 py-1 rounded-md bg-gray-50 border border-gray-100 hover:bg-gray-100 transition-colors">
                    <Copy class="h-3 w-3 text-gray-400" />
                    <span class="text-[10px] font-bold text-gray-600">{{ property.type.substring(0, 2).toUpperCase() }}{{ 8000 + property.id }}</span>
                  </button>
                </div>

                <div class="mb-3">
                  <p class="font-black text-gray-900 text-lg tracking-tight">{{ property.price }}</p>
                  <p class="text-gray-500 text-xs line-clamp-2 h-8 mt-1">{{ property.address }}</p>
                </div>

                <div class="flex items-center gap-4 text-xs text-gray-500 font-medium mb-4">
                  <span class="flex items-center gap-1"><Ruler class="h-3.5 w-3.5 text-gray-400" /> {{ property.area }}</span>
                  <span class="flex items-center gap-1"><Bath class="h-3.5 w-3.5 text-gray-400" /> {{ property.bathrooms }}</span>
                  <span class="flex items-center gap-1"><Car class="h-3.5 w-3.5 text-gray-400" /> {{ property.parking }}</span>
                </div>

                <div class="mt-auto pt-4 border-t border-gray-100">
                  <button 
                    @click.stop="openReserveModal(property)"
                    :disabled="property.isReserved"
                    :class="['w-full flex items-center justify-center gap-2 py-2.5 text-sm font-semibold transition-all rounded-[24px]', property.isReserved ? 'bg-gray-50 text-gray-400 cursor-not-allowed' : 'bg-black text-white hover:bg-gray-800']"
                  >
                    <span v-if="property.isReserved">Em Negociação</span>
                    <span v-else>Agendar Visita</span>
                  </button>
                </div>
              </div>
            </div>

            <div v-if="index === 7" class="col-span-1 sm:col-span-2 md:col-span-3 lg:col-span-4 my-4">
              <div class="relative rounded-3xl overflow-hidden min-h-[300px] md:min-h-[400px]">
                <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1600&q=80" alt="Lançamento" class="absolute inset-0 w-full h-full object-cover" />
                <div class="absolute inset-0 bg-gradient-to-r from-black/90 via-black/60 to-transparent"></div>
                <div class="relative z-10 p-8 md:p-12 flex flex-col justify-center h-full max-w-xl">
                  <span class="px-3 py-1 bg-white rounded-full text-xs font-bold text-black uppercase tracking-widest w-fit mb-4">Lançamento Exclusivo</span>
                  <h2 class="text-white text-3xl md:text-5xl font-black mb-3">Residencial Vista Bella</h2>
                  <p class="text-white/80 text-sm md:text-base mb-6 leading-relaxed">Novo empreendimento no coração de Chapecó. Apartamentos de 2 e 3 dormitórios com infraestrutura de lazer completa.</p>
                  <div class="flex gap-6 text-white/90 text-sm font-medium mb-8">
                    <span class="flex items-center gap-2"><Ruler class="h-4 w-4" /> Centro, Chapecó</span>
                    <span class="flex items-center gap-2"><CalendarIcon class="h-4 w-4" /> Entrega em 2026</span>
                  </div>
                  <button class="bg-white text-black font-bold px-8 py-3 rounded-full hover:bg-gray-100 transition-all w-fit">Saiba Mais</button>
                </div>
              </div>
            </div>
            
          </template>
        </div>
      </div>
    </section>

    <section class="py-20 px-6 bg-white border-t border-gray-100 w-full">
      <div class="max-w-4xl mx-auto text-center space-y-8">
        <div class="space-y-3">
          <h2 class="text-gray-900 text-3xl md:text-4xl font-black tracking-tight">Fique por dentro do<br />mercado imobiliário</h2>
          <p class="text-gray-500 text-lg">Receba alertas de novos imóveis e oportunidades B2B exclusivas.</p>
        </div>
        <form @submit.prevent="handleSubscribe" class="flex flex-col sm:flex-row gap-4 max-w-md mx-auto">
          <input 
            type="email" 
            placeholder="Digite seu e-mail" 
            v-model="email" 
            class="flex-1 px-6 py-3 rounded-full border border-gray-300 bg-gray-50 text-gray-900 focus:ring-2 focus:ring-black outline-none transition-all" 
            required 
          />
          <button type="submit" class="bg-black text-white font-bold px-8 py-3 rounded-full hover:bg-gray-800 transition-colors">Inscrever-se</button>
        </form>
      </div>
    </section>

  </div>
</template>