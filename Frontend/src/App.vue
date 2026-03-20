<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// Força a fundação visual Noir no nível mais alto do DOM
onMounted(() => {
  document.documentElement.classList.add('dark')
  document.documentElement.style.backgroundColor = '#000000'
  document.body.className = 'bg-black antialiased overflow-x-hidden'
})
</script>

<template>
  <v-app theme="dark">
    <div class="min-h-screen bg-black text-foreground selection:bg-emerald-500/30">

      <router-view v-slot="{ Component }">
        <transition name="premium-fade" mode="out-in" appear>
          <component :is="Component" :key="route.path" />
        </transition>
      </router-view>

    </div>
  </v-app>
</template>

<style>
/* ESTILOS DE TRANSIÇÃO PREMIUM 
  Focados em suavidade cinematográfica (ease-in-out)
*/
.premium-fade-enter-active,
.premium-fade-leave-active {
  transition: opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1),
    transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.premium-fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.premium-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* OVERRIDE CRÍTICO VUETIFY 4
  Impede que o framework injete fundos cinzas ou elevações indesejadas
*/
.v-application {
  background: transparent !important;
}

.v-application__wrap {
  background-color: #000000 !important;
  min-height: 100vh !important;
  /* Força a tipografia do manifesto em toda a árvore */
  font-family: 'Inter', sans-serif !important;
}

/* Garante que o fundo de modais e menus use o Glassmorphism do manifesto */
.v-overlay__scrim {
  background: rgba(0, 0, 0, 0.8) !important;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}
</style>