# /main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.auth import auth_router
from mangum import Mangum

app = FastAPI(title="Task Manager API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, usa ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Incluir las rutas definidas en routes.py
app.include_router(auth_router)
app.include_router(router)

handler = Mangum(app)

@app.get("/")
def home():
    return {"message": "API Running!"}