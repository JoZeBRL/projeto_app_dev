# 🚀 Como Rodar o Projeto

## ⚡ Quick Start

O projeto é totalmente conteinerizado. O uso de `npm` no host é opcional (apenas para scripts de conveniência).

### Desenvolvimento completo (Docker Compose)
1. Certifique-se de que o Docker está rodando.
2. Crie o arquivo `.env` no diretório `Backend` (você pode copiar o `.env.example`).
3. Execute na raiz do projeto:
```powershell
docker-compose up -d --build --wait
```

- **Frontend:** [http://localhost:5174/](http://localhost:5174/) (Vite)
- **Backend:** [http://localhost:8000/](http://localhost:8000/)
- **Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **pgAdmin:** [http://localhost:5050/](http://localhost:5050/)
- **Backend:** http://localhost:8000/
- **Docs:** http://localhost:8000/docs
- **pgAdmin:** http://localhost:5050/

### Desenvolvimento backend separado (sem Docker)
```powershell
# 1. Sobe só o banco
docker-compose up postgres pgadmin -d

# 2. Backend no venv
cd backend/app
uvicorn main:app --reload
```

### Produção
```powershell
npm run build
npm start
```

### Parar os containers
```powershell
npm run stop          # dev
npm run stop:prod     # prod
```

---

## 🔧 Arquitetura

### Backend (Python FastAPI)
- **Porta:** 8000
- **Health:** http://localhost:8000/ → `{"status": "online", ...}`
- **Docs:** http://localhost:8000/docs
- **Modo:** Controlado pela variável `ENV` no `.env`
  - `ENV=development` → CORS permissivo
  - `ENV=production` → CORS restrito

### Banco de dados (Docker)
- **PostgreSQL:** `localhost:5432`
- **pgAdmin:** http://localhost:5050 (credenciais no `.env`)
- **Bancos:** `corretiza_db` (aplicação) e `corretiza_test` (testes)

### Frontend (Vite + Vue 3)
- **Porta:** 5174
- **Base API:** `/api` (proxy converte para `http://localhost:8000/api/v1`)

### Fluxo de Login
```
Frontend: POST /api/auth/login
    ↓
Proxy Vite: /api → /api/v1
    ↓
Backend: POST /api/v1/auth/login
    ↓
Retorna: {access_token, refresh_token, token_type}
```

---

## 🗂️ Estrutura de Pastas

```
CORRETIZA_APP/
├── backend/
│   ├── alembic/                    ← migrations do banco
│   │   └── versions/
│   ├── app/
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/
│   │   │   ├── database.py
│   │   │   └── crud.py
│   │   ├── middleware/
│   │   │   └── cors_middleware.py
│   │   ├── models/
│   │   │   ├── enums.py
│   │   │   └── models.py
│   │   ├── schemas/
│   │   │   └── schemas.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── properties.py
│   │   │   ├── proposals.py
│   │   │   └── users.py
│   │   └── main.py
│   ├── database/
│   │   └── init-test-db.sql
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_users.py
│   │   ├── test_properties.py
│   │   └── test_proposals.py
│   ├── venv/
│   ├── .env                    ← nunca commitar!
│   ├── .env.example
│   ├── .dockerignore
│   ├── .gitignore
│   ├── alembic.ini
│   ├── Dockerfile
│   ├── requirements.txt
│   └── requirements-dev.txt
├── frontend/
│   ├── Dockerfile              ← produção (Nginx)
│   └── Dockerfile.dev          ← desenvolvimento (Vite)
├── docker-compose.yml          ← base (produção)
├── docker-compose.override.yml ← dev (aplicado automaticamente)
├── package.json                ← scripts de orquestração
├── setup-env.js                ← cria .env automaticamente
└── COMO_RODAR_PROJETO.md
```

---

## ⚙️ Configuração do `.env`

O `setup-env.js` cria o `backend/.env` automaticamente a partir do `backend/.env.example` quando você roda `npm run dev`.

Edite o `backend/.env` com as variáveis corretas antes de subir o projeto.

> ⚠️ Em produção, o `DATABASE_URL` usa `postgres` como host (nome do container) em vez de `localhost`.

---

## 🗄️ Banco de Dados

### Rodar migrations (primeira vez ou após mudanças no modelo)
```powershell
cd backend
alembic upgrade head
```

### Resetar banco (apaga todos os dados)
```powershell
docker-compose down -v
docker-compose up postgres -d
alembic upgrade head
```

---

## 🧪 Testes

```powershell
npm test

ou

cd backend

# Todos os testes
pytest tests/ -v

# Por arquivo
pytest tests/test_auth.py -v
pytest tests/test_users.py -v
pytest tests/test_properties.py -v
pytest tests/test_proposals.py -v
```

> Os testes usam o banco `corretiza_test` e limpam os dados automaticamente após cada teste.

---

## 🔍 Debug

### Logs do backend em tempo real
```powershell
uvicorn main:app --reload --log-level debug
```

### Logs dos containers
```powershell
docker-compose logs backend -f
docker-compose logs postgres -f
```

### Testar backend direto

**Swagger:** http://localhost:8000/docs

**Postman:**
- Method: `POST`
- URL: `http://localhost:8000/api/v1/auth/login`
- Body: `x-www-form-urlencoded`
  - `username`: seu@email.com
  - `password`: suasenha

---

## ❌ Troubleshooting

### Backend em modo PRODUÇÃO quando deveria ser DEV
Confirma que `ENV=development` está no `backend/.env` salvo em UTF-8 sem BOM.

### Erro: `UnicodeDecodeError` ao conectar no banco
Verifica se existe `pgpass.conf` em `C:\Users\<user>\AppData\Roaming\postgresql\` e deleta.

### Erro: `timeout` ou `Connection refused`
```powershell
curl http://localhost:8000/
docker-compose ps
```

### Erro: `CORS policy`
Confirma `ENV=development` no `.env` e reinicia o backend.

### Porta ocupada
```powershell
netstat -ano | findstr :8000
taskkill /PID <número> /F
```

---

## 🌿 Branches

| Branch     | Uso                               |
|------------|-----------------------------------|
| `backend`  | Desenvolvimento do backend        |
| `frontend` | Desenvolvimento do frontend       |
| `dev`      | Integração e testes               |
| `prod`     | Produção — apenas via PR aprovado |