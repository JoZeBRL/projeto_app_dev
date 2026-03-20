<script setup>
import { ref, onMounted, nextTick } from 'vue'

const newMessage = ref('')
const chatContainer = ref(null)

const messages = ref([
    { id: 1, sender: 'Construtora Black', text: 'Recebemos os documentos. O RG está um pouco ilegível, poderia reenviar?', time: '10:30', isMe: false },
    { id: 2, sender: 'Eu', text: 'Com certeza! Vou tirar uma foto com melhor iluminação agora mesmo.', time: '10:32', isMe: true },
    { id: 3, sender: 'Eu', text: 'Acabei de fazer o upload no campo acima.', time: '10:35', isMe: true },
    { id: 4, sender: 'Construtora Black', text: 'Perfeito, agora sim. Vamos encaminhar para o jurídico.', time: '11:00', isMe: false }
])

const scrollToBottom = async () => {
    await nextTick()
    if (chatContainer.value) {
        chatContainer.value.scrollTop = chatContainer.value.scrollHeight
    }
}

const sendMessage = () => {
    if (!newMessage.value.trim()) return

    messages.value.push({
        id: Date.now(),
        sender: 'Eu',
        text: newMessage.value,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        isMe: true
    })

    newMessage.value = ''
    scrollToBottom()
}

onMounted(scrollToBottom)
</script>

<template>
    <div class="flex flex-col h-[500px] bg-white rounded-[40px] border border-gray-100 overflow-hidden shadow-sm">
        <div class="p-6 border-b border-gray-50 flex items-center justify-between bg-gray-50/50">
            <div class="flex items-center gap-3">
                <div
                    class="w-10 h-10 bg-black rounded-full flex items-center justify-center text-white font-black text-xs">
                    CB
                </div>
                <div>
                    <h4 class="text-sm font-black text-black leading-none">Construtora Black</h4>
                    <span class="text-[10px] text-emerald-500 font-bold uppercase tracking-widest">Online agora</span>
                </div>
            </div>
            <v-btn icon="mdi-dots-vertical" variant="text" size="small" color="gray"></v-btn>
        </div>

        <div ref="chatContainer" class="flex-1 overflow-y-auto p-6 space-y-4 scroll-smooth">
            <div v-for="msg in messages" :key="msg.id"
                :class="['flex flex-col', msg.isMe ? 'items-end' : 'items-start']">
                <div :class="[
                    'max-w-[80%] p-4 text-sm font-medium leading-relaxed',
                    msg.isMe
                        ? 'bg-black text-white rounded-t-[20px] rounded-l-[20px] shadow-lg shadow-black/10'
                        : 'bg-gray-100 text-gray-800 rounded-t-[20px] rounded-r-[20px]'
                ]">
                    {{ msg.text }}
                </div>
                <span class="text-[9px] font-black text-gray-400 mt-1 uppercase tracking-tighter">
                    {{ msg.time }}
                </span>
            </div>
        </div>

        <div class="p-6 bg-white border-t border-gray-50">
            <div class="relative flex items-center gap-2">
                <input v-model="newMessage" type="text" placeholder="Escreva sua mensagem..."
                    class="w-full bg-gray-50 border-none rounded-full px-6 py-4 text-sm font-medium focus:ring-2 focus:ring-black transition-all outline-none"
                    @keyup.enter="sendMessage" />
                <v-btn icon="mdi-send" color="black" elevation="4" size="large" class="!rounded-full"
                    @click="sendMessage"></v-btn>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Custom Scrollbar para manter o visual Premium */
::-webkit-scrollbar {
    width: 4px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: #f1f1f1;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #e5e5e5;
}
</style>