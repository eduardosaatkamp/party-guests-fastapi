from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import List

tags_metadata = [
    {
        "name": "health",
        "description": "Endpoints de verificação de status da API.",
    },
    {
        "name": "guests",
        "description": "Gerenciamento simples de convidados (memória).",
    },
]

app = FastAPI(
    title="Guest List API",
    version="1.0.0",
    description=(
        "API simples para gerenciar uma lista de convidados.\n\n"
        "Endpoints de **GET** e **POST** apenas (por enquanto)."
    ),
    contact={
        "name": "Seu Nome",
        "url": "https://example.com",
        "email": "you@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_url="/openapi.json",   # onde o schema OpenAPI fica
    docs_url="/docs",              # Swagger UI
    redoc_url="/redoc",            # ReDoc
    openapi_tags=tags_metadata,
)

# ----- Schemas -----
class GuestCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Nome do convidado")

class Guest(BaseModel):
    id: int
    name: str

# ----- "Banco" em memória -----
_guests: List[Guest] = []
_next_id = 1

# ----- Endpoints -----
@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}

@app.get("/guests", response_model=List[Guest], tags=["guests"])
def list_guests():
    """Lista todos os convidados atuais."""
    return _guests

@app.post(
    "/guests",
    response_model=Guest,
    status_code=201,
    tags=["guests"],
    summary="Adiciona um convidado",
)
def add_guest(
    payload: GuestCreate = Body(
        ...,
        examples={
            "ex1": {"summary": "Nome simples", "value": {"name": "Midorya"}},
            "ex2": {"summary": "Com espaços", "value": {"name": "  Maria da Silva  "}},
        },
    )
):
    """
    Cria um novo convidado e retorna o objeto criado.
    - **name**: nome do convidado
    """
    global _next_id
    guest = Guest(id=_next_id, name=payload.name.strip())
    _next_id += 1
    _guests.append(guest)
    return guest
