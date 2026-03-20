<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import AuthLayout from '@/layouts/AuthLayout.vue';
import AppLayout from '@/layouts/AppLayout.vue';

const route = useRoute();

// Define dinamicamente o layout baseado na rota. Padrão: AppLayout (Interno)
const layout = computed(() => {
  return route.meta.layout === 'auth' ? AuthLayout : AppLayout;
});
</script>

<template>
  <v-app class="!bg-transparent">
    <transition name="premium-fade" mode="out-in" appear>
      <component :is="layout">
        <router-view v-slot="{ Component }">
          <transition name="premium-fade" mode="out-in">
            <component :is="Component" :key="route.path" />
          </transition>
        </router-view>
      </component>
    </transition>
  </v-app>
</template>

<style>
body {
  margin: 0;
  overflow-x: hidden;
}

.premium-fade-enter-active,
.premium-fade-leave-active {
  transition: opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1), transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.premium-fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.premium-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.v-application {
  background: transparent !important;
}
.v-application__wrap {
  min-height: 100vh !important;
  font-family: 'Inter', system-ui, sans-serif !important;
}
</style>