<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
// Removidos Lucide e Vuetify imports manuais. 
// O auto-import resolve os componentes v-xxx.

interface Props {
    searchQuery: string;
    location: string;
    propertyType: string;
    priceRange: string;
    bedrooms: string;
    parkingSpots: string;
    bathrooms: string;
    isHeaderScrolled?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
    isHeaderScrolled: false
});

const emit = defineEmits([
    'update:searchQuery',
    'update:location',
    'update:propertyType',
    'update:priceRange',
    'update:bedrooms',
    'update:parkingSpots',
    'update:bathrooms',
    'search'
]);

const isFilterOpen = ref(false);
const filterRef = ref<HTMLElement | null>(null);

// Opções de Filtro (Mantidas e expandidas conforme a lógica de negócio)
const locationOptions = [
    { value: "centro", label: "Centro" },
    { value: "efapi", label: "Efapi" },
    { value: "jardim-america", label: "Jardim América" },
    { value: "sao-cristovao", label: "São Cristóvão" }
];

const propertyOptions = [
    { value: "apartamento", label: "Apartamento" },
    { value: "casa", label: "Casa" },
    { value: "terreno", label: "Terreno" }
];

const priceRangeOptions = [
    { value: "0-500000", label: "Até R$ 500 mil" },
    { value: "500000-1500000", label: "R$ 500 mil - 1.5Mi" },
    { value: "1500000-99999999", label: "Luxo (+1.5Mi)" }
];

const activeFiltersCount = computed(() => {
    return [
        props.location,
        props.propertyType,
        props.priceRange,
        props.bedrooms,
        props.parkingSpots,
        props.bathrooms
    ].filter(Boolean).length;
});

const toggleFilter = () => { isFilterOpen.value = !isFilterOpen.value; };

const clearFilters = () => {
    emit('update:location', '');
    emit('update:propertyType', '');
    emit('update:priceRange', '');
    emit('update:bedrooms', '');
    emit('update:parkingSpots', '');
    emit('update:bathrooms', '');
};

const handleSearch = () => {
    isFilterOpen.value = false;
    emit('search');
};

const handleClickOutside = (event: MouseEvent) => {
    if (filterRef.value && !filterRef.value.contains(event.target as Node)) {
        isFilterOpen.value = false;
    }
};

onMounted(() => document.addEventListener('mousedown', handleClickOutside));
onUnmounted(() => document.removeEventListener('mousedown', handleClickOutside));
</script>

<template>
    <div ref="filterRef" class="relative w-full max-w-5xl mx-auto">
        <div
            class="flex items-center bg-zinc-900/40 backdrop-blur-xl border border-white/10 p-1.5 rounded-[40px] shadow-2xl transition-all duration-300 focus-within:border-emerald-500/50">
            <div class="flex-[2] min-w-[200px]">
                <v-text-field :model-value="searchQuery" @update:model-value="$emit('update:searchQuery', $event)"
                    placeholder="Buscar imóveis ou bairros..." variant="solo" flat hide-details bg-color="transparent"
                    class="custom-search-input" @keydown.enter="handleSearch">
                    <template v-slot:prepend-inner>
                        <v-icon icon="mdi-magnify" class="text-zinc-500 ml-2" />
                    </template>
                </v-text-field>
            </div>

            <div class="hidden md:block h-8 w-[1px] bg-white/10 mx-1"></div>

            <div class="flex-1 hidden md:block">
                <v-select :model-value="location" @update:model-value="$emit('update:location', $event)"
                    :items="locationOptions" item-title="label" item-value="value" placeholder="Localização"
                    variant="solo" flat hide-details bg-color="transparent" class="custom-select-minimal" />
            </div>

            <div class="hidden lg:block h-8 w-[1px] bg-white/10 mx-1"></div>

            <div class="flex-1 hidden lg:block">
                <v-select :model-value="propertyType" @update:model-value="$emit('update:propertyType', $event)"
                    :items="propertyOptions" item-title="label" item-value="value" placeholder="Tipo" variant="solo"
                    flat hide-details bg-color="transparent" class="custom-select-minimal" />
            </div>

            <div class="flex items-center gap-2 pr-1">
                <button @click="toggleFilter"
                    class="relative p-3 rounded-full hover:bg-white/10 transition-all text-gray-400 hover:text-white"
                    :class="{ 'text-emerald-500 bg-emerald-500/10': isFilterOpen }">
                    <v-icon icon="mdi-tune-variant" />
                    <span v-if="activeFiltersCount > 0"
                        class="absolute top-1 right-1 w-4 h-4 bg-emerald-500 text-black text-[10px] rounded-full flex items-center justify-center font-black">
                        {{ activeFiltersCount }}
                    </span>
                </button>

                <v-btn color="white" icon class="!text-black hover:scale-105 transition-transform" elevation="4"
                    size="48" rounded="circle" @click="handleSearch">
                    <v-icon icon="mdi-magnify" size="24" />
                </v-btn>
            </div>
        </div>

        <Transition name="fade-slide">
            <div v-if="isFilterOpen"
                class="absolute left-0 right-0 mt-4 p-8 bg-zinc-900 border border-white/10 rounded-[40px] shadow-[0_25px_50px_-12px_rgba(0,0,0,0.8)] z-50 overflow-hidden">
                <div class="flex items-center justify-between mb-8">
                    <div>
                        <h3 class="text-xl font-black text-white uppercase tracking-tighter italic">Filtros Avançados
                        </h3>
                        <p class="text-[10px] font-black text-gray-500 uppercase tracking-widest">Refine sua busca B2B
                        </p>
                    </div>
                    <button v-if="activeFiltersCount > 0" @click="clearFilters"
                        class="text-xs font-black uppercase tracking-widest text-emerald-500 hover:text-emerald-400 transition-colors">
                        Resetar
                    </button>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div class="space-y-3">
                        <label class="text-[10px] uppercase font-black tracking-[0.2em] text-gray-500">Faixa de
                            Preço</label>
                        <v-select :model-value="priceRange" @update:model-value="$emit('update:priceRange', $event)"
                            :items="priceRangeOptions" item-title="label" item-value="value" variant="solo" flat
                            rounded="pill" bg-color="rgba(255,255,255,0.05)" placeholder="Qualquer valor" hide-details
                            class="custom-expanded-select"></v-select>
                    </div>

                </div>

                <v-btn block color="emerald-500" height="56" rounded="pill"
                    class="mt-10 !text-black !font-black text-lg" @click="handleSearch">
                    Aplicar Filtros
                </v-btn>
            </div>
        </Transition>
    </div>
</template>

<style scoped>
/* Reset de estilos Vuetify para manter o visual Premium Black */
:deep(.v-field) {
    --v-field-padding-start: 16px;
    font-weight: 900 !important;
    color: white !important;
}

:deep(.v-field__input) {
    font-size: 0.9rem !important;
}

.custom-select-minimal :deep(.v-field__append-inner) {
    display: none;
    /* Estilo minimalista do Browser.tsx */
}

.custom-search-input :deep(.v-field) {
    font-family: 'Objectivity', sans-serif !important;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.fade-slide-enter-from,
.fade-slide-leave-to {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
}
</style>