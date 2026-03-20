import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes: Array<RouteRecordRaw> = [
  { path: '/', redirect: '/dashboard' },
  { path: '/login', name: 'Login', component: () => import('@/views/Login.vue'), meta: { requiresAuth: false, layout: 'auth' } },
  { path: '/register', name: 'Register', component: () => import('@/views/Register.vue'), meta: { requiresAuth: false, layout: 'auth' } },
  { path: '/dashboard', name: 'Dashboard', component: () => import('@/views/DashboardPage.vue'), meta: { requiresAuth: true } },
  { path: '/negociacoes', name: 'Negociacoes', component: () => import('@/views/NegociacoesPage.vue'), meta: { requiresAuth: true } },
  { path: '/developments/new', name: 'AddDevelopment', component: () => import('@/views/AddDevelopment.vue'), meta: { requiresAuth: true } },
  { path: '/wallet', name: 'Wallet', component: () => import('@/views/WalletPage.vue'), meta: { requiresAuth: true } },
  { path: '/reservations', name: 'Reservations', component: () => import('@/views/ReservationsPage.vue'), meta: { requiresAuth: true } },
  { path: '/profile', name: 'Profile', component: () => import('@/views/ProfilePage.vue'), meta: { requiresAuth: true } },
  { path: '/agendamentos', name: 'Agendamentos', component: () => import('@/views/AgendamentosPage.vue'), meta: { requiresAuth: true } },
  { path: '/tower/:id', name: 'TowerDetail', component: () => import('@/views/TowerDetail.vue'), meta: { requiresAuth: true } },
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: () => import('@/views/NotFound.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Guard de autenticação tipado
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login')
  } else if ((to.name === 'Login' || to.name === 'Register') && authStore.isAuthenticated) {
    next('/dashboard')
  } else {
    next()
  }
})

export default router
