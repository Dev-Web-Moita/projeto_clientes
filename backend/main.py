# importa as classes e funções necessárias do FastAPI e exceção para erros de HTTP
from fastapi import FastAPI, HTTPException
# importa o middleware de cores para permitir solicitações de diferentes origens
from fastapi.middleware.cors import CORSMiddleware
# importa a classe BaseModel do Pydantic para criar modelos de dados
from pydantic import BaseModel
# importa utilitarios de tipagem de python para definir tipos opcionais e listas
from typing import Optional, List

# inicializa a aplicação FastAPI definindo título e versão
app = FastAPI(title = "API de Clientes", version = "1.0")

# adiciona o middleware CORS na aplicação para evitar bloqueios de segurança no navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5137"],  # permite solicitações de qualquer origem
    allow_credentials = True,  # permite o envio de cookies e credenciais
    allow_methods = ["*"],  # permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers = ["*"]  # permite todos os cabeçalhos HTTP
)

# define o modelo de dados para criar um cliente utilizando o pydantic BaseModel
class ClienteCreate(BaseModel):
    nome: str
    email: str
    telefone: Optional[str] = ""
    empresa: Optional[str] = ""

# define o modelo completo do cliente herdando de ClienteCreate 
# e adicionando os campos id e active
class Cliente(ClienteCreate):
    id: int
    active: bool = True

clientes_db: List[Cliente] = [
    Cliente(id=1, nome="Gustavo", email="gustavo@example.com", 
    telefone="123456789", empresa="FIAP", active=True),
    Cliente(id=2, nome="Moita", email="moita@example.com", 
    telefone="987654321", empresa="FIAP", active=True)
]  # lista para armazenar os clientes cadastrados

#  define a rota HTTP para o GET para o endpoint que retorna a lista de clientes
@app.get("/api/clientes", response_model = List[Cliente], status_code=201)
def buscar_clientes():
    return clientes_db

@app.post("/api/clientes", response_model = Cliente, status_code=201)
def adicionar_cliente(cliente: ClienteCreate):
    novo_id = len(clientes_db) + 1  # gera um novo ID para o cliente
    novo_cliente = Cliente(
        id=novo_id,
        nome=cliente.nome,
        email=cliente.email,
        telefone=cliente.telefone,
        empresa=cliente.empresa,
        active=True 
    )  # cria um novo cliente com os dados fornecidos

    clientes_db.append(novo_cliente)  # adiciona o novo cliente à lista de clientes
    return novo_cliente  # retorna o novo cliente criado