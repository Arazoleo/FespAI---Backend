from fastapi import FastAPI, HTTPException
from app import models, database
from app.routes import auth
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitindo requisições de qualquer origem. Para produção, é bom especificar as origens.
    allow_credentials=True,
    allow_methods=["*"],  # Permite qualquer método (GET, POST, etc.)
    allow_headers=["*"],  # Permite qualquer cabeçalho
)

app.include_router(auth.router, prefix="/auth")

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}