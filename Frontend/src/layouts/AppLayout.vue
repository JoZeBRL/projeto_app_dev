<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import Sidebar from '@/components/navigation/Sidebar.vue';

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();

const userName = computed(() => authStore.user?.nome || 'Usuário');
const userType = computed(() => authStore.user?.tipo || 'broker');
const activeRouteName = computed(() => String(route.name || '').toLowerCase());

const isSidebarOpen = ref(false);

const handleLogout = () => {
  authStore.logout();
  router.push('/login');
};

const handleNavigate = (routeName: string) => {
  router.push({ name: routeName });
  isSidebarOpen.value = false;
};
</script>

<template>
  <div class="min-h-screen bg-[#f9fafb] font-sans flex flex-col">
    
    <Sidebar 
      :isOpen="isSidebarOpen" 
      :currentPage="activeRouteName"
      :userName="userName"
      :userType="userType"
      @close="isSidebarOpen = false"
      @navigate="handleNavigate"
      @logout="handleLogout"
    />

    <GlobalHeader 
      :userName="userName" 
      :userType="userType"
      :currentPage="activeRouteName"
      @open-sidebar="isSidebarOpen = true"
      @navigate="handleNavigate"
      @logout="handleLogout"
    />

    <main class="flex-1 w-full h-full">
      <slot />
    </main>

  </div>
</template>
