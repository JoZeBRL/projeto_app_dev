# Projeto Corretiza App

## Visão Geral
O Corretiza App é uma plataforma (hub) para corretores e construtoras. O projeto é estruturado de forma full-stack, separado em um Backend construído com Python (FastAPI) e um Frontend construído com Vue.js 3 + Vite. O banco de dados utilizado é PostgreSQL rodando via Docker.

## Arquitetura
- **Backend**: API RESTFUL usando FastAPI, exposta localmente na porta 8000.
- **Frontend**: SPA construída em Vue 3, rodando localmente na porta 5174.
- **Banco de Dados**: PostgreSQL containerizado via Docker Compose (Porta 5432).

## Estrutura de Diretórios
- `/Backend/`: Contém todo o código-fonte da API Python.
- `/Frontend/`: Contém todo o código-fonte da interface de usuário em Javascript/Vue.
- `docker-compose.yml`: Orquestração de containers do banco de dados (postgres e gerenciador pgadmin).
- `COMO_RODAR_PROJETO.md`: Instruções detalhadas para execução do projeto e testes locais de sanidade ("Health Check").
- `/docs/`: Documentação detalhada dos componentes específicos do projeto.

Para detalhes específicos de cada camada, confira a documentação abaixo:
- [Documentação do Backend](./backend.md)
- [Documentação do Frontend](./frontend.md)
