/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

// O Vuetify 4 injeta suas próprias tipagens globais via plugin.
// Não declare componentes manualmente aqui para evitar erros TS2305.