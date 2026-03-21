<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import GlobalHeader from '@/components/navigation/GlobalHeader.vue';
import Sidebar from '@/components/navigation/Sidebar.vue';

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();

const userName = computed(() => authStore.user?.nome || 'Usuário');
const userType = computed(() => authStore.user?.tipo || 'broker');

const isSidebarOpen = ref(window.innerWidth >= 1024);

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};

const handleLogout = () => {
  authStore.logout();
  router.push('/login');
};

const handleResize = () => {
  if (window.innerWidth >= 1024) {
    isSidebarOpen.value = true;
  }
};

onMounted(() => {
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
});
</script>

<template>
  <div class="min-h-screen bg-white dark:bg-[#0A0A0B] transition-colors duration-300">
    <!-- Header Fixo -->
    <GlobalHeader 
      :user-name="userName" 
      :user-type="userType"
      @open-sidebar="toggleSidebar"
      @logout="handleLogout"
    />
    
    <div class="flex pt-20">
      <!-- Sidebar com controle de estado -->
      <Sidebar :is-open="isSidebarOpen" @close="isSidebarOpen = false" />
      
      <!-- Área de Conteúdo Principal -->
      <main 
        :class="[
          'flex-1 transition-all duration-500 ease-in-out min-h-[calc(100vh-80px)]',
          isSidebarOpen ? 'lg:ml-80' : 'ml-0'
        ]"
      >
        <div class="p-6 md:p-10 max-w-7xl mx-auto">
          <router-view v-slot="{ Component }">
            <transition name="page" mode="out-in">
              <component :is="Component" />
            </transition>
          </router-view>
        </div>
      </main>
    </div>
  </div>
</template>

<style scoped>
.page-enter-active, .page-leave-active { 
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); 
}
.page-enter-from { 
  opacity: 0; 
  transform: translateY(12px) scale(0.99); 
}
.page-leave-to { 
  opacity: 0; 
  transform: translateY(-12px) scale(1.01); 
}
</style>
