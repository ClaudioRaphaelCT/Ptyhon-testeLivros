from pydantic import BaseModel

class Livro(BaseModel):
    id: int
    name: str
    box: int