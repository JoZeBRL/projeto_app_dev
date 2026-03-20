<script setup>
defineProps({
    property: Object,
    isGrid: Boolean
});
const emit = defineEmits(['remove']);
</script>

<template>
    <div :class="[
        'group relative bg-[#111111] border border-white/5 hover:border-white/20 transition-all duration-500 overflow-hidden',
        isGrid ? 'rounded-[40px] flex flex-col' : 'rounded-[30px] flex flex-row h-64'
    ]">
        <div :class="['relative overflow-hidden', isGrid ? 'aspect-[4/3]' : 'w-80 h-full']">
            <img :src="property.image"
                class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-60">
            </div>

            <div class="absolute top-6 left-6 flex gap-2">
                <span
                    class="bg-white text-black px-4 py-1.5 rounded-full text-[10px] font-black uppercase tracking-widest">
                    {{ property.type }}
                </span>
            </div>

            <button @click.stop="emit('remove', property.id)"
                class="absolute top-6 right-6 w-12 h-12 bg-black/40 backdrop-blur-md rounded-full flex items-center justify-center border border-white/20 hover:bg-red-500 transition-colors">
                <v-icon icon="mdi-heart" color="white" size="20"></v-icon>
            </button>
        </div>

        <div :class="['p-8 flex flex-col justify-between', isGrid ? 'flex-1' : 'flex-1']">
            <div>
                <div class="flex justify-between items-start mb-4">
                    <h3
                        class="text-xl font-black leading-tight tracking-tight text-white group-hover:text-emerald-400 transition-colors">
                        {{ property.title }}
                    </h3>
                </div>
                <p class="flex items-center text-gray-500 text-sm font-medium mb-6">
                    <v-icon icon="mdi-map-marker-outline" size="16" class="mr-1"></v-icon>
                    {{ property.location }}
                </p>
            </div>

            <div class="flex items-end justify-between border-t border-white/5 pt-6">
                <div>
                    <p class="text-[10px] font-black text-emerald-500 uppercase tracking-widest mb-1">Valor de Venda</p>
                    <p class="text-2xl font-black text-white">{{ property.price }}</p>
                </div>
                <v-btn color="white" rounded="pill" size="large" class="!font-black !text-black !capitalize" flat>
                    Ver Unidade
                </v-btn>
            </div>
        </div>
    </div>
</template>