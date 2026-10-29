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

class ClienteCreate(BaseModel):
    nome: str
    email: str
    telefone: Optional[str] = ""
    empresa: Optional[str] = ""