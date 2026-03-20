<script setup lang="ts">
import { ref } from 'vue';
// Removidos Lucide e Vuetify imports manuais. 
// O auto-import resolve os componentes v-xxx.

const props = defineProps<{
    modelValue: any
}>();

const config = ref({
    floors: 10,
    unitsPerFloor: 4
});

// Gera a matriz de unidades baseada nos inputs do utilizador
const generateMatrix = () => {
    const newUnits = [];
    for (let f = 1; f <= config.value.floors; f++) {
        for (let u = 1; u <= config.value.unitsPerFloor; u++) {
            const unitNumber = `${f}${u.toString().padStart(2, '0')}`;
            newUnits.push({
                id: crypto.randomUUID(),
                floor: f,
                number: unitNumber,
                modelId: props.modelValue.plans[0]?.id || '',
                price: props.modelValue.plans[0]?.basePrice || '',
                status: 'disponivel',
                view: 'Frente'
            });
        }
    }
    props.modelValue.units = newUnits;
};

const getStatusColor = (status: string) => {
    switch (status) {
        case 'disponivel': return 'text-emerald-500 bg-emerald-500/10 border border-emerald-500/20';
        case 'reservado': return 'text-amber-500 bg-amber-500/10 border border-amber-500/20';
        case 'vendido': return 'text-red-500 bg-red-500/10 border border-red-500/20';
        default: return 'text-zinc-500 bg-zinc-500/10 border border-zinc-500/20';
    }
};
</script>

<template>
    <div class="space-y-8 animate-in fade-in slide-in-from-right-4 duration-500">
        <section class="glass-container !p-10">
            <div class="flex items-center gap-4 mb-8">
                <v-icon icon="mdi-auto-fix" color="emerald-500" />
                <h3 class="text-xs font-black uppercase tracking-[0.3em] text-white italic">Motor de Geração de Matriz</h3>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-end">
                <v-text-field v-model.number="config.floors" label="TOTAL DE ANDARES" variant="solo-filled" flat bg-color="rgba(255,255,255,0.05)" type="number"
                    prepend-inner-icon="mdi-layers-outline" class="font-black" />

                <v-text-field v-model.number="config.unitsPerFloor" label="UNIDADES POR ANDAR" variant="solo-filled" flat bg-color="rgba(255,255,255,0.05)"
                    prepend-inner-icon="mdi-format-list-numbered" type="number" class="font-black" />

                <button class="btn-premium h-[56px] w-full mb-[22px] !text-[11px] italic" @click="generateMatrix">
                    GERAR TABELA ESTRATÉGICA
                </button>
            </div>
        </section>

        <div v-if="modelValue.units.length > 0"
            class="overflow-x-auto rounded-[40px] border border-white/5 bg-black/40">
            <table class="w-full text-left border-collapse">
                <thead class="bg-zinc-900/80">
                    <tr>
                        <th class="p-6 text-[10px] font-black uppercase tracking-[0.2em] text-zinc-500 italic">Unidade</th>
                        <th class="p-6 text-[10px] font-black uppercase tracking-[0.2em] text-zinc-500 italic">Planta / Modelo</th>
                        <th class="p-6 text-[10px] font-black uppercase tracking-[0.2em] text-zinc-500 italic">Valor de Tabela (R$)</th>
                        <th class="p-6 text-[10px] font-black uppercase tracking-[0.2em] text-zinc-500 italic text-center">Status B2B</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-white/5">
                    <tr v-for="unit in modelValue.units" :key="unit.id"
                        class="hover:bg-white/5 transition-colors group">
                        <td class="p-6">
                            <span class="font-black text-xl italic text-white">{{ unit.number }}</span>
                            <p class="text-[9px] text-zinc-600 uppercase font-black tracking-widest">{{ unit.floor }}º ANDAR</p>
                        </td>
                        <td class="p-6">
                            <select v-model="unit.modelId"
                                class="w-full p-3 bg-black/40 border-b-2 border-white/5 text-xs font-black uppercase tracking-widest text-white focus:border-emerald-500 outline-none rounded-t-lg transition-all">
                                <option v-for="plan in modelValue.plans" :key="plan.id" :value="plan.id">
                                    {{ plan.name || 'Modelo Padrão' }}
                                </option>
                            </select>
                        </td>
                        <td class="p-6">
                            <input type="text" v-model="unit.price"
                                class="w-full p-3 bg-black/40 border-b-2 border-white/5 text-xs font-black tracking-widest text-emerald-400 focus:border-emerald-500 outline-none rounded-t-lg transition-all" />
                        </td>
                        <td class="p-6 text-center">
                            <span
                                :class="['px-5 py-2 rounded-full text-[9px] font-black uppercase tracking-[0.2em]', getStatusColor(unit.status)]">
                                {{ unit.status }}
                            </span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div v-else
            class="py-32 text-center border-2 border-dashed border-white/5 rounded-[40px] bg-black/20">
            <v-icon icon="mdi-table-large" size="64" class="text-zinc-800 mb-6" />
            <p class="font-black text-zinc-500 uppercase tracking-[0.2em] text-xs">Aguardando geração da matriz de unidades...</p>
        </div>
    </div>
</template>
e>