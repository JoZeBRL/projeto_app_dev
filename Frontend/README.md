# Corretiza Frontend

**Stack:** Vite + Vue 3 + UnoCSS + Pinia

## Rodar Projeto

```bash
npm install
npm run dev
```

Acesse: http://localhost:5174

## Build Produção

```bash
npm run build
```

## Estrutura

```
src/
├── pages/       # Login, Dashboard, Properties, etc
├── components/  # Componentes reutilizáveis  
├── stores/      # Pinia (auth, properties)
├── api/         # Cliente HTTP + interceptors
└── router/      # Rotas + guards
```
