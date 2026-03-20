<script setup>
defineProps({
    property: Object
})
</script>

<template>
    <v-card
        class="!rounded-[40px] overflow-hidden bg-[#14161C] border border-white/5 hover:border-emerald-500/30 transition-all duration-500 group"
        flat>
        <div class="relative overflow-hidden aspect-[4/3]">
            <v-img :src="property.image" cover class="transition-transform duration-700 group-hover:scale-110">
                <div class="absolute top-4 left-4">
                    <v-chip color="emerald" size="small" class="font-black uppercase italic">{{ property.type
                        }}</v-chip>
                </div>
            </v-img>
        </div>

        <v-card-text class="pa-6">
            <h3 class="text-xl font-black uppercase italic tracking-tight text-white mb-1 truncate">
                {{ property.title }}
            </h3>
            <p class="text-gray-500 text-xs mb-4 flex items-center gap-1">
                <v-icon icon="mdi-map-marker" size="14"></v-icon> {{ property.address }}
            </p>

            <div class="flex justify-between items-center pt-4 border-t border-white/5">
                <div class="flex gap-4">
                    <div class="text-center">
                        <p class="text-[10px] text-gray-500 font-black uppercase">Área</p>
                        <p class="text-sm font-bold">{{ property.area }}</p>
                    </div>
                    <div class="text-center">
                        <p class="text-[10px] text-gray-500 font-black uppercase">Dorms</p>
                        <p class="text-sm font-bold">{{ property.beds }}</p>
                    </div>
                </div>
                <div class="text-right">
                    <p class="text-emerald-400 font-black text-lg">{{ property.price }}</p>
                </div>
            </div>
        </v-card-text>
    </v-card>
</template>