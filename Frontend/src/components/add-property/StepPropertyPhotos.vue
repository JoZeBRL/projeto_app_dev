<script setup lang="ts">
import { ref } from 'vue';
import { Upload, X, ImageIcon, CheckCircle2 } from 'lucide-vue-next';

const props = defineProps<{ modelValue: any }>();
const previews = ref<string[]>([]);

const handleFileChange = (e: any) => {
    const files = Array.from(e.target.files) as File[];
    files.forEach(file => {
        props.modelValue.images.push(file);
        previews.value.push(URL.createObjectURL(file));
    });
};

const removeImage = (index: number) => {
    props.modelValue.images.splice(index, 1);
    previews.value.splice(index, 1);
};
</script>

<template>
    <div class="bg-gray-50 dark:bg-white/5 p-8 md:p-12 rounded-[40px] space-y-8">
        <div class="flex items-center gap-3">
            <div class="w-2 h-8 bg-green-600 rounded-full"></div>
            <h2 class="text-2xl font-black uppercase tracking-tighter">Mídia e Fotos</h2>
        </div>

        <label class="relative group cursor-pointer block">
            <input type="file" multiple accept="image/*" class="hidden" @change="handleFileChange" />
            <div
                class="border-2 border-dashed border-gray-300 dark:border-white/10 rounded-[40px] p-16 text-center group-hover:border-green-600 transition-all bg-white dark:bg-black/20">
                <div
                    class="w-20 h-20 bg-gray-100 dark:bg-white/5 rounded-3xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform">
                    <Upload class="w-10 h-10 text-gray-400 group-hover:text-green-600" />
                </div>
                <p class="text-lg font-black uppercase tracking-tighter">Arraste as fotos aqui</p>
                <p class="text-sm text-gray-500 font-bold uppercase tracking-widest mt-1">ou clique para selecionar
                    arquivos</p>
            </div>
        </label>

        <div v-if="previews.length > 0" class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4">
            <div v-for="(img, idx) in previews" :key="idx"
                class="relative aspect-square group overflow-hidden rounded-[32px]">
                <img :src="img"
                    class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
                <div
                    class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                    <button @click="removeImage(idx)"
                        class="p-3 bg-red-600 text-white rounded-full hover:scale-110 transition-transform">
                        <X class="w-5 h-5" />
                    </button>
                </div>
                <div v-if="idx === 0"
                    class="absolute top-4 left-4 bg-green-600 text-white text-[10px] font-black uppercase px-3 py-1 rounded-full flex items-center gap-1">
                    <CheckCircle2 class="w-3 h-3" /> Capa
                </div>
            </div>
        </div>
    </div>
</template>