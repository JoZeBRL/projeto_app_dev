# Corretiza - Manifesto Técnico & Business Rules (v2.0)

## 🎯 Conceito B2B (Business-to-Business)
A Corretiza é um ecossistema fechado para corretores de imóveis e construtoras.
- **Usuários:** Corretores (CRECI) e Gestores de Construtoras.
- **Proibição:** Acesso externo de compradores finais é estritamente vedado.
- **Linguagem:** Técnica, ágil e focada em fechamento de negócios.

---

## 🎨 Identidade Visual "Premium Black" (Rigor Figma)

### 1. Sistema de Cores (Tailwind v4 tokens)
- **Background Principal:** `bg-black` (Profundidade máxima).
- **Cards & Containers:** `bg-zinc-900/50` com `backdrop-blur-xl`.
- **Ações Positivas:** `text-emerald-500` / `bg-emerald-600`.
- **Erros/Alertas:** `text-red-500`.
- **Bordas:** `border-white/10` (Efeito de fio de luz).

### 2. Geometria & Sombras
- **Raio de Borda (Pill):** `rounded-[40px]` para botões e containers principais.
- **Raio de Borda (Cards):** `rounded-3xl` (24px).
- **Sombras:** `shadow-[0_20px_50px_rgba(0,0,0,0.5)]`.

### 3. Tipografia (Font Rigor)
- **Títulos/Labels:** `font-black` (Peso 900).
- **Estilo:** `uppercase` e `tracking-[0.2em]` para labels de sistema (Ex: "BEM-VINDO").
- **Cor:** Branco puro para títulos, `text-gray-400` para descrições.

---

## 🛠️ Diretrizes de Desenvolvimento (Vue 3 / Vuetify 4)

### 1. Arquitetura de Componentes
- **Views:** Apenas orquestram dados e layout de página. Local: `src/views/`.
- **Components:** Lógica de domínio atômica. Local: `src/components/[modulo]/`.
- **Script Setup:** Obrigatório o uso de `<script setup lang="ts">`.

### 2. Vuetify 4 Premium Integration
- Utilizar `v-menu`, `v-dialog` e `v-navigation-drawer` para componentes de overlay.
- Estilizar via classes Tailwind dentro dos componentes Vuetify usando `:class` ou `class`.

### 3. Tailwind v4 First
- Evitar CSS arbitrário em blocos `<style>`.
- Usar utilitários de opacidade (`/10`, `/50`) para criar o efeito Glassmorphism.

---

## 📋 Regras de Negócio (Business Logic)
1. **Reservas:** Devem possuir data de expiração automática.
2. **Comissões:** Sempre destacadas em Emerald Green.
3. **Busca:** Exclusiva para o perfil `broker`.
4. **Privacidade:** Dados de clientes do corretor são visíveis apenas para o corretor proprietário da conta.

---

## 📂 Estrutura de Arquivos & Dependências

Abaixo a relação completa de arquivos e quais componentes cada uno orquestra ou consome.

### 1. Views (Páginas principais)
- **AddDevelopment.vue**: Passo a passo de cadastro de empreendimentos. 
  - [Usa]: `StepGeneralInfo`, `StepFloorPlans`, `StepUnits`.
- **AddProperty.vue**: Cadastro de imóveis individuais.
  - [Usa]: `GlobalHeader`, `Sidebar`, `StepPropertyBasicInfo`, `StepPropertyDetails`, `StepPropertyPhotos`.
- **DashboardPage.vue**: Visão geral do Corretor.
  - [Usa]: `GlobalHeader`, `Sidebar`, `DashboardCard`.
- **NegociacoesPage.vue**: Gestão de propostas e vendas. 
  - [Usa]: `GlobalHeader`, `NegotiationTimeline`, `ProposalSummary`, `ChatDirect`, `NegotiationItem`, `CustomAlert`.
- **AgendamentosPage.vue**: Calendário e visitas.
  - [Usa]: `GlobalHeader`, `Sidebar`, `AgendamentoCard`, `HistoryDrawer`.
- **MyProperties.vue**: Gestão da carteira de imóveis.
  - [Usa]: `GlobalHeader`.
- **PropertyDetail.vue**: Detalhamento técnico do imóvel.
  - [Usa]: `ReserveModal`.
- **PropertySearch.vue**: Motor de busca de oportunidades.
  - [Usa]: `PropertyCard`, `PartnerCarousel`.
- **ProposalPage.vue**: Layout de envio de propostas.
  - [Usa]: `ProposalFormInfo`, `ProposalFormPayment`.
- **FavoritesPage.vue**: Imóveis salvos.
  - [Usa]: `GlobalHeader`, `FavoriteCard`.
- **Login.vue / Register.vue**: Fluxos de acesso.
  - [Usa]: `LoginForm`, `SignupForm`.
- **Outras Views**: `ProfilePage`, `WalletPage`, `NotificationsPage`, `ConstructionDashboard`, `ReservationsPage`, `TowerDetail`, `SettingsPage`.
  - [Usa]: Geralmente `GlobalHeader` e `Sidebar`.

### 2. Componentes (Blocos Funcionais)
- **Navigation**: 
  - `GlobalHeader.vue`: Barra superior premium. Orquestra `Logo`, `SearchBar` e `UserMenu`.
  - `Sidebar.vue`: Menu lateral de navegação rápida.
- **Auth**:
  - `LoginForm.vue`: Gestão de acesso com abas (Broker/Construction).
  - `SignupForm.vue`: Cadastro de novos membros.
- **Negociações**:
  - `NegotiationItem.vue`: Linha resumida de negociação (usada na lista principal).
  - `NegotiationTimeline.vue`: Histórico visual de eventos da proposta.
  - `ChatDirect.vue`: Interface de comunicação direta.
- **Common/UI**: 
  - `ConfirmModal.vue`, `CustomAlert.vue`, `PartnerCarousel.vue`, `DashboardCard.vue`, `FavoriteCard.vue`.

---

## 📊 Tabela de Migração & Status

| Módulo | Arquivos Migrados | Status |
| :--- | :--- | :--- |
| **Documentação** | `ProjectManifesto (Guidelines)` | ✅ 100% |
| **Busca / Filtros** | `SearchBar.vue`, `PropertyCard.vue` | ✅ 100% |
| **Global/Navigation** | `Header, Sidebar, UserMenu, Logo` | ✅ 100% |
| **Empreendimentos** | `AddDevelopment, TowerDetail, Steps...` | ✅ 100% |
| **Imóveis** | `AddProperty, Details, Photos, Search` | ✅ 100% |
| **Autenticação** | `LoginForm, SignupForm` | ✅ 100% |
| **Dashboards** | `DashboardPage, Construction...` | ✅ 100% |
| **Perfil/Carteira** | `Profile, Wallet, Favorites, MyProperties` | ✅ 100% |
| **Agendamentos** | `AgendamentosPage, Card, History, Modais` | ✅ 100% |
| **Negociações** | `Timeline, Summary, Chat, Item` | ✅ 100% |
| **Propostas** | `ProposalPage, FormInfo, FormPayment` | ✅ 100% |