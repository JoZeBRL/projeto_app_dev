<script setup lang="ts">
// Removidos Lucide e Vuetify imports manuais. 
// O auto-import resolve os componentes v-xxx.

const props = defineProps<{
    modelValue: any
}>();

const categorias = ['Residencial', 'Comercial', 'Loteamento', 'Industrial'];
const diferenciaisDisponiveis = ['Piscina', 'Academia', 'Rooftop', 'Portaria 24h', 'Coworking', 'Pet Friendly'];

const toggleFeature = (feature: string) => {
    const index = props.modelValue.features.indexOf(feature);
    if (index === -1) props.modelValue.features.push(feature);
    else props.modelValue.features.splice(index, 1);
};
</script>

<template>
    <div class="space-y-8 animate-in fade-in duration-500">
        <section>
            <h3 class="text-lg font-black text-white mb-6 flex items-center gap-2 uppercase italic tracking-tighter">
                <v-icon icon="mdi-office-building-marker-outline" color="emerald-500" /> Identificação do Projeto
            </h3>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <v-text-field v-model="modelValue.name" label="NOME DO EMPREENDIMENTO" variant="solo-filled" flat bg-color="rgba(255,255,255,0.05)"
                    placeholder="Ex: Reserva Du Parc" persistent-placeholder class="rounded-xl font-bold" />

                <v-select v-model="modelValue.category" :items="categorias" label="CATEGORIA" variant="solo-filled" flat bg-color="rgba(255,255,255,0.05)"
                    class="rounded-xl font-bold" />
            </div>
        </section>

        <section>
            <h3 class="text-lg font-black text-white mb-6 flex items-center gap-2 uppercase italic tracking-tighter">
                <v-icon icon="mdi-map-marker-radius-outline" color="emerald-500" /> Localização Estratégica
            </h3>
            <v-text-field v-model="modelValue.location" label="ENDEREÇO COMPLETO" variant="solo-filled" flat bg-color="rgba(255,255,255,0.05)"
                prepend-inner-icon="mdi-map-marker" placeholder="Rua, Bairro, Cidade - UF" class="rounded-xl font-bold" />
        </section>

        <section>
            <h3 class="text-lg font-black text-white mb-6 flex items-center gap-2 uppercase italic tracking-tighter">
                <v-icon icon="mdi-text-box-search-outline" color="emerald-500" /> Descrição e Conceito
            </h3>
            <v-textarea v-model="modelValue.description" label="MEMORIAL DESCRITIVO" variant="solo-filled" flat bg-color="rgba(255,255,255,0.05)"
                prepend-inner-icon="mdi-file-document-outline" rows="4" placeholder="Descreva o conceito, acabamentos e diferenciais..."
                class="rounded-xl font-bold" />

            <div class="mt-6">
                <p class="text-[10px] font-black uppercase text-zinc-500 mb-4 tracking-[0.3em]">Diferenciais Exclusivos</p>
                <div class="flex flex-wrap gap-2">
                    <button v-for="feature in diferenciaisDisponiveis" :key="feature" @click="toggleFeature(feature)"
                        :class="[
                            'px-5 py-2.5 rounded-full border-2 text-[10px] font-black uppercase tracking-widest transition-all flex items-center gap-2',
                            modelValue.features.includes(feature)
                                ? 'bg-white border-white text-black shadow-lg shadow-white/10'
                                : 'bg-black/40 border-white/5 text-zinc-500 hover:border-white/20'
                        ]">
                        <v-icon v-if="modelValue.features.includes(feature)" icon="mdi-check-circle" size="14" />
                        {{ feature }}
                    </button>
                </div>
            </div>
        </section>
    </div>
</template>