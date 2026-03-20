# Corretiza: Documentação Técnica Frontend (Fase Premium Black)

Esta documentação detalha a arquitetura frontend do Ecossistema Corretiza, consolidada após a migração para a **Fase Premium Black**. O foco principal é a entrega de uma experiência B2B de alto luxo, com rigor tipográfico e performance otimizada.

## 1. Stack Tecnológica

*   **Framework:** Vue.js 3 (Composition API)
*   **UI Framework:** **Vuetify 4 (Alpha/Experimental)**
    *   *Nota:* O auto-import via Vite é obrigatório. Proibida a importação manual de componentes no `<script setup>`.
*   **CSS Engine:** **Tailwind CSS v4**
    *   Uso de variáveis de tema nativas e camadas (`@layer`) para overrides de rigor.
*   **Gerenciamento de Estado:** Pinia
*   **Ícones:** **Material Design Icons (MDI)** exclusivo.
    *   Remoção total da biblioteca Lucide para garantir consistência e performance.
*   **Tipografia:** Inter (font-black, italic e tracking-tighter para títulos).

---

## 2. Padrões de Design e UX

### 2.1 Rigor Visual B2B
O design é orientado pelo **Manifesto Corretiza V2.0**, focado no "Rigor Noir":
*   **Fundo:** Preto absoluto (`#000000`).
*   **Containers:** Uso obrigatório da classe `.glass-container` (zinc-900/50 com backdrop-blur).
*   **Geometria:** Arredondamento padrão de **40px** (`rounded-[40px]`) para containers e botões principais.
*   **Botões:** Ações críticas devem utilizar a classe `.btn-premium`.

### 2.2 Tratamento de Mídia
Toda e qualquer exibição de imagem no sistema deve utilizar o componente `AppImage.vue`. Ele garante:
*   Fallbacks automáticos para imagens quebradas.
*   Skeleton loading durante o carregamento.
*   Ajuste de aspect-ratio consistente com o design de luxo.

---

## 3. Hierarquia de Arquivos

A estrutura do projeto segue uma separação estrita de domínios para facilitar a manutenção e integração:

```plaintext
src/
├── assets/styles/main.css  # CSS Global Tailwind v4 + Overrides Vuetify 4
├── components/
│   ├── navigation/         # GlobalHeader.vue, Sidebar.vue, UserMenu.vue, Logo.vue
│   ├── auth/               # LoginForm.vue, SignupForm.vue
│   ├── search/             # SearchBar.vue, PropertyCard.vue
│   ├── negociacoes/        # NegotiationItem.vue, NegotiationTimeline.vue, ChatDirect.vue, ProposalSummary.vue, StepDocumentUpload.vue
│   ├── proposal/           # ProposalFormInfo.vue
│   ├── add-development/    # StepGeneralInfo.vue, StepFloorPlans.vue, StepUnits.vue
│   ├── add-property/       # StepPropertyBasicInfo.vue, StepPropertyDetails.vue, StepPropertyPhotos.vue
│   ├── property/           # ReserveModal.vue
│   ├── common/             # ConfirmModal.vue, CustomAlert.vue, PartnerCarousel.vue, PromoteModal.vue
│   └── common/UI/          # AppImage.vue (Tratamento de mídia global)
├── views/                  # Orquestradores de Página (DashboardPage, WalletPage, ReservationsPage, etc.)
├── stores/                 # Pinia: auth.ts e gerenciamento de estados globais
├── api/                    # Serviços Axios para comunicação com o Backend
└── guidelines/             # ProjectManifesto.md (Referência de Design B2B)
```

---

## 4. Integração e Fluxo de Dados

### 4.1 Arquitetura de Consumo
As **Views** atuam como orquestradores de alto nível, sendo responsáveis por:
1.  Consumir estados globais das **Stores (Pinia)**.
2.  Despachar ações para as Stores dispararem chamadas para a camada de **API (Axios)**.
3.  Distribuir os dados tipados para os componentes de domínio (Props).

### 4.2 Integridade B2B
Todos os contratos de dados trocados entre Frontend e Backend **devem ser tipados em TypeScript**. Isso garante que falhas de esquema não cheguem à camada visual, essencial para um ambiente de negociação imobiliária de alto valor.

---

## 5. Regras de Ouro (Instruções de Desenvolvimento)

Para manter o "Rigor Premium Black", os desenvolvedores devem seguir estas diretrizes:

*   **Regra 01:** Nunca utilize cores hexadecimais genéricas diretamente no HTML/Vue. Utilize sempre as variáveis de tema definidas no `main.css` ou classes utilitárias do Tailwind.
*   **Regra 02:** Todo botão de ação principal (CTA) deve usar a classe `.btn-premium`.
*   **Regra 03:** Todo container de conteúdo ou card de destaque deve utilizar a classe `.glass-container`.
*   **Regra 04:** É proibida a importação manual de componentes Vuetify no `<script setup>`. O auto-import via Vite está configurado e é obrigatório para evitar erros de tipagem TS2305.
*   **Regra 05:** Ícones devem ser chamados exclusivamente via `<v-icon icon="mdi-xxx" />`.

---

*Documento atualizado em conformidade com o Manifesto Corretiza V2.0.*
