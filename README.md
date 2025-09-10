# Party Guests (FastAPI)

API simples para gerenciar uma lista de convidados (em memória) usando FastAPI.

## Tecnologias
- FastAPI: framework web assíncrono em Python
- Pydantic: validação de dados (modelos de entrada/saída)
- Uvicorn: servidor ASGI para executar a API

## Como rodar
1) Ambiente e dependências (opção rápida):
- `python3 setup_and_open.py guests_main.py`

2) Manualmente:
- `python3 -m venv .venv && source .venv/bin/activate`
- `pip install fastapi uvicorn[standard]`
- `uvicorn guests_main:app --reload`

Docs interativas: `http://127.0.0.1:8000/docs` (Swagger) e `http://127.0.0.1:8000/redoc`.

## Endpoints
- GET `/` : healthcheck da API
- GET `/guests` : lista convidados
- POST `/guests` : cria convidado — body `{ "name": "Alice" }`
