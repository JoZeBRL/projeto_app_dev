<script setup lang="ts">
import { computed } from 'vue';
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

const handleLogout = () => {
    authStore.logout();
    router.push('/login');
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 text-gray-900 font-sans transition-colors duration-300 antialiased">
    <GlobalHeader 
      :userName="userName" 
      :userType="userType" 
      @logout="handleLogout"
      @navigate="(name) => router.push({ name })"
    />
    
    <div class="max-w-7xl mx-auto flex">
      <Sidebar 
        :activeId="activeRouteName" 
        :userType="userType"
        @navigate="(name) => router.push({ name })"
        @logout="handleLogout"
      />
      
      <main class="flex-1 pt-32 pb-12 px-6 lg:px-8">
        <slot />
      </main>
    </div>
  </div>
</template>
