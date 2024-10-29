from fastapi import APIRouter
from models.livros import Livro
from controllers.livros import get_all
from typing import List

api_router = APIRouter()

@api_router.get("/livros", response_model=List[Livro])
def read_livros():
    return get_all()