# Corretiza: Documentação Técnica Backend (Core API)

Esta documentação detalha a arquitetura do Backend do Ecossistema Corretiza, projetada para ser uma API RESTful robusta, escalável e segura, servindo como o motor de dados para o hub de corretores e construtoras.

## 1. Stack Tecnológica

*   **Linguagem:** Python 3.10+
*   **Framework Web:** **FastAPI (v0.104.1)**
    *   Utilizado pela alta performance, suporte nativo a operações assíncronas e documentação automática (Swagger/OpenAPI).
*   **Servidor ASGI:** Uvicorn
*   **Banco de Dados:** **PostgreSQL**
*   **ORM e Camada de Dados:**
    *   **SQLAlchemy (v2.0):** Para mapeamento objeto-relacional com suporte a tipagem moderna.
    *   **Alembic:** Para gerenciamento de migrações de esquema de banco de dados.
*   **Validação e Serialização:** **Pydantic (v2)**
    *   Garante que todos os dados de entrada e saída sigam contratos estritos (schemas).
*   **Segurança e Autenticação:**
    *   **JWT (JSON Web Tokens):** Para sessões seguras e stateless.
    *   **Bcrypt:** Para hashing robusto de senhas.
*   **Ambiente:** `python-dotenv` para gestão de segredos via arquivo `.env`.

---

## 2. Arquitetura e Estrutura de Pastas

O Backend segue uma estrutura modular para separar responsabilidades de configuração, dados e lógica de rotas.

```plaintext
Backend/
├── alembic/                # Histórico de migrações do banco de dados
├── app/
│   ├── main.py             # Ponto de entrada, inicialização FastAPI e middlewares
│   ├── core/               # Configurações globais, segurança e contantes
│   ├── db/                 # Configuração do engine e sessão SQLAlchemy
│   ├── middleware/         # Filtros de requisição (CORS, logging, etc.)
│   ├── models/             # Definição das tabelas (SQLAlchemy Models)
│   ├── routes/             # Definição dos endpoints (API Routers)
│   └── schemas/            # Contratos de dados e validação (Pydantic)
├── tests/                  # Suíte de testes automatizados
└── requirements.txt        # Dependências do projeto
```

---

## 3. Endpoints da API (v1)

A API é versionada sob o prefixo `/api/v1` e está dividida em quatro domínios principais:

### 3.1 Autenticação (`/auth`)
*   `POST /auth/register`: Cadastro de novos usuários (Corretor ou Construtora).
*   `POST /auth/login`: Autenticação e geração de tokens JWT.
*   `POST /auth/refresh`: Renovação de tokens de acesso.

### 3.2 Usuários (`/users`)
*   `GET /users/me`: Recupera o perfil do usuário autenticado.
*   `PATCH /users/me`: Atualiza informações cadastrais e de perfil.

### 3.3 Propriedades (`/properties`)
*   `GET /properties`: Listagem filtrável de imóveis disponíveis.
*   `GET /properties/{id}`: Detalhamento técnico de uma unidade.
*   `POST /properties`: Criação de novos empreendimentos (Acesso restrito a construtoras).

### 3.4 Propostas e Negociações (`/proposals`)
*   `POST /proposals`: Envio de nova proposta de compra/reserva.
*   `GET /proposals`: Lista de negociações ativas (contextual por tipo de usuário).
*   `PATCH /proposals/{id}`: Atualização de status (Aceite, Contraproposta, Recusa).

---

## 4. Segurança e Integridade

1.  **Proteção de Rotas:** Endpoints sensíveis exigem o header `Authorization: Bearer <token>`.
2.  **CORS:** Configurado via middleware para permitir apenas domínios autorizados (Frontend Corretiza).
3.  **Hashing:** Senhas nunca são armazenadas em texto simples; utiliza-se `bcrypt` com salt adaptativo.
4.  **Validação:** Todos os inputs são validados contra Pydantic Schemas antes de atingirem a camada de serviço ou banco de dados.

---

## 5. Fluxo de Desenvolvimento e Deploy

### Migrações de Banco
Sempre que o `app/models/models.py` for alterado, uma nova migração deve ser gerada:
```bash
alembic revision --autogenerate -m "descrição da mudança"
alembic upgrade head
```

### Variáveis de Ambiente Obrigatórias
O backend exige um arquivo `.env` com as seguintes chaves:
*   `DATABASE_URL`: String de conexão PostgreSQL.
*   `SECRET_KEY`: Chave mestre para assinatura de tokens.
*   `ENV`: `development` ou `production`.

---

*Documento atualizado em conformidade com o Core API v1.0.*
