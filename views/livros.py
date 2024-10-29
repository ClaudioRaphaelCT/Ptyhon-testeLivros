from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.livros import Livro
from controllers.livros import get_all
from typing import List
from fastapi import APIRouter

# Criação da aplicação FastAPI
app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:5173",  # Permite acesso do seu frontend (Vue.js)
    "https://ptyhon-testelivros.onrender.com",  # Permite acesso da API em produção, se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Criação do APIRouter
api_router = APIRouter()

@api_router.get("/livros", response_model=List[Livro])
def read_livros():
    return get_all()

# Inclui o router na aplicação
app.include_router(api_router)
