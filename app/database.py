import os
from pymongo.errors import ConnectionFailure
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)

db = client["taskdb"]  # Base de datos
tasks_collection = db["tasks"]  # Colección de tareas
users_collection = db["users"]  # Colección de usuarios
