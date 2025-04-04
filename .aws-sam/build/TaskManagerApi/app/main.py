# backend/app/main.py
from fastapi import FastAPI
from app.routes import router
from app.auth import auth_router
from mangum import Mangum

app = FastAPI(title="Task Manager API")

# Incluir las rutas definidas en routes.py
app.include_router(auth_router)
app.include_router(router)

handler = Mangum(app)

@app.get("/")
def home():
    return {"message": "API Running!"}