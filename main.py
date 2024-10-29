from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views.livros import api_router

app = FastAPI()

# Configuração de CORS
origins = [
    "http://localhost:5173",  # Adicione aqui o domínio do seu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
