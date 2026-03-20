// src/plugins/vuetify.ts
import '@mdi/font/css/materialdesignicons.css' // Essencial para os ícones baseados em string funcionarem
import 'vuetify/styles'
import { createVuetify } from 'vuetify'

// O Vite cuidará do auto-import dos componentes, não precisamos declarar aqui.
export default createVuetify({
  theme: {
    defaultTheme: 'dark',
    themes: {
      dark: {
        dark: true,
        colors: {
          background: '#000000',
          surface: '#0a0a0a',
          primary: '#ffffff',
          secondary: '#1a1a1a',
          error: '#EF4444',
          info: '#3B82F6',
          success: '#10B981', // Nosso Emerald Premium
          warning: '#F59E0B',
        },
      },
    },
  },
  // O Vuetify já usa o MDI como padrão quando a fonte CSS está presente
})
