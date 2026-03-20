<script setup lang="ts">
defineProps<{
    id: number | string;
    title: string;
    type: string;
    location: string;
    price: string;
    beds: number;
    baths: number;
    parking: number;
    image: string;
}>();
</script>

<template>
    <v-card
        class="!rounded-[40px] overflow-hidden glass-container hover:border-emerald-500/30 transition-all duration-500 group"
        flat>
        <div class="relative overflow-hidden aspect-[4/3]">
            <v-img :src="image" cover class="transition-transform duration-700 group-hover:scale-110">
                <div class="absolute top-4 left-4">
                    <v-chip color="emerald" size="small" class="font-[900] uppercase italic !text-[10px] tracking-widest text-white">
                        {{ type }}
                    </v-chip>
                </div>
            </v-img>
        </div>

        <v-card-text class="pa-6">
            <h3 class="text-xl font-[900] uppercase italic tracking-tight text-[var(--text-color)] mb-1 truncate">
                {{ title }}
            </h3>
            <p class="text-[var(--label-color)] text-[10px] font-[900] uppercase tracking-widest mb-4 flex items-center gap-1">
                <v-icon icon="mdi-map-marker" size="14" class="text-emerald-500" />
                {{ location }}
            </p>

            <div class="flex justify-between items-center pt-4 border-t border-[var(--glass-border)]">
                <div class="flex gap-4">
                    <div class="text-center">
                        <p class="text-[8px] text-[var(--label-color)] font-[900] uppercase tracking-widest">Dorms</p>
                        <p class="text-sm font-[900] text-[var(--text-color)] italic">{{ beds }}</p>
                    </div>
                    <div class="text-center">
                        <p class="text-[8px] text-[var(--label-color)] font-[900] uppercase tracking-widest">Vagas</p>
                        <p class="text-sm font-[900] text-[var(--text-color)] italic">{{ parking }}</p>
                    </div>
                </div>
                <div class="text-right">
                    <p class="text-emerald-500 font-[900] text-xl italic tracking-tighter">{{ price }}</p>
                </div>
            </div>
        </v-card-text>
    </v-card>
</template>