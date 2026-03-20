import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'

export default createVuetify({
  theme: {
    defaultTheme: 'light', // MUDANÇA CRÍTICA: Deixa o Tailwind governar as cores
    themes: {
      light: {
        colors: {
          primary: '#111827',
          secondary: '#6b7280',
          success: '#10B981',
        },
      },
    },
  },
})
