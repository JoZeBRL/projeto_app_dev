<script setup>
import { ref } from 'vue'

const uploadedDocuments = ref([])
const cartorioStatus = ref('pendente') // 'pendente' | 'concluido'
const isDragging = ref(false)

const handleFileUpload = (event) => {
    const files = Array.from(event.target.files || event.dataTransfer.files)

    files.forEach(file => {
        if (file.size <= 10 * 1024 * 1024) { // 10MB
            uploadedDocuments.value.push({
                name: file.name,
                size: (file.size / 1024 / 1024).toFixed(2) + 'MB',
                type: file.type
            })
        } else {
            // Aqui integraria com o CustomAlert futuramente
            alert(`O arquivo ${file.name} excede 10MB`)
        }
    })
}

const handleConfirmCartorio = () => {
    // Simulação de processamento
    cartorioStatus.value = 'concluido'
}

const removeFile = (index) => {
    uploadedDocuments.value.splice(index, 1)
}
</script>

<template>
    <div class="space-y-6">
        <div class="flex items-center gap-2 mb-4">
            <v-icon icon="mdi-file-document-outline" color="black"></v-icon>
            <span class="font-black text-lg text-black">Documentos para Cartório</span>
        </div>

        <div v-if="cartorioStatus === 'pendente'" @dragover.prevent="isDragging = true"
            @dragleave.prevent="isDragging = false" @drop.prevent="handleFileUpload; isDragging = false"
            :class="[isDragging ? 'border-black bg-gray-50' : 'border-gray-200']"
            class="border-2 border-dashed rounded-[32px] p-10 transition-all text-center relative">
            <input type="file" multiple accept=".jpg,.png,.pdf,.doc,.docx"
                class="absolute inset-0 w-full h-full opacity-0 cursor-pointer" @change="handleFileUpload" />

            <v-icon icon="mdi-cloud-upload" size="48" color="gray-lighten-1" class="mb-4"></v-icon>
            <p class="text-black font-black text-lg">Arraste seus documentos aqui</p>
            <p class="text-sm text-gray-400 mt-2 font-medium">
                Tire fotos ou selecione arquivos (JPG, PNG, PDF ou DOC - máx. 10MB cada)
            </p>
        </div>

        <div v-if="uploadedDocuments.length > 0" class="space-y-3">
            <div v-for="(file, index) in uploadedDocuments" :key="index"
                class="flex items-center justify-between p-4 bg-gray-50 rounded-2xl border border-gray-100">
                <div class="flex items-center gap-3">
                    <v-icon icon="mdi-file-check" color="emerald"></v-icon>
                    <div class="flex flex-col">
                        <span class="text-sm font-bold text-black truncate max-w-[200px]">{{ file.name }}</span>
                        <span class="text-[10px] text-gray-400 font-black uppercase">{{ file.size }}</span>
                    </div>
                </div>
                <button @click="removeFile(index)" class="p-2 hover:bg-red-50 rounded-full transition-colors group">
                    <v-icon icon="mdi-close" size="small" class="group-hover:text-red-500"></v-icon>
                </button>
            </div>
        </div>

        <v-btn v-if="uploadedDocuments.length > 0 && cartorioStatus === 'pendente'" block color="black" height="56"
            class="!rounded-full font-black text-white shadow-xl hover:scale-[1.02] transition-transform"
            prepend-icon="mdi-check-circle" @click="handleConfirmCartorio">
            Confirmar envio e concluir
        </v-btn>

        <div v-if="cartorioStatus === 'concluido'"
            class="bg-emerald-50 border border-emerald-100 rounded-[24px] p-6 flex items-center gap-4">
            <div
                class="w-12 h-12 bg-emerald-500 rounded-full flex items-center justify-center shadow-lg shadow-emerald-200">
                <v-icon icon="mdi-check-bold" color="white"></v-icon>
            </div>
            <div>
                <h4 class="font-black text-emerald-900 text-lg">Documentação Enviada</h4>
                <p class="text-emerald-700 text-sm font-medium">Todos os arquivos foram processados e a etapa foi
                    concluída com sucesso.</p>
            </div>
        </div>
    </div>
</template>