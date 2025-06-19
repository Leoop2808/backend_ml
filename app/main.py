from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(
    title="API de Predicción de Hipertensión",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Permite todos los dominios
    allow_credentials=False,    # Evita error con "*"
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
