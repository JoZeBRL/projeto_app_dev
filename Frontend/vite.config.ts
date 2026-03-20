import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import tailwindcss from '@tailwindcss/vite'
import vuetify from 'vite-plugin-vuetify'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    vue(),
    // OBRIGATÓRIO: Habilita o auto-import e resolve erros de TypeScript (TS2305)
    vuetify({ autoImport: true }), 
    tailwindcss(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'Corretiza B2B',
        short_name: 'Corretiza',
        theme_color: '#000000',       // Sincronizado: Premium Black
        background_color: '#000000',  // Sincronizado: Premium Black (Splash Screen)
        icons: [
          { src: 'pwa-192x192.png', sizes: '192x192', type: 'image/png' },
          { src: 'pwa-512x512.png', sizes: '512x512', type: 'image/png' }
        ]
      }
    })
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@views': path.resolve(__dirname, './src/views'),
      '@layouts': path.resolve(__dirname, './src/layouts'), // Restaurado
      '@stores': path.resolve(__dirname, './src/stores'),
      '@api': path.resolve(__dirname, './src/api'),
      '@utils': path.resolve(__dirname, './src/utils'),     // Restaurado
      '@assets': path.resolve(__dirname, './src/assets'),
      '@plugins': path.resolve(__dirname, './src/plugins'), // Restaurado
    }
  },
  server: {
    port: 5174,
    strictPort: true,
    proxy: {
      '/api': {
        target: 'http://backend:8000', // Comunica com o container Docker do Backend
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '/api/v1'),
      }
    }
  }
})
