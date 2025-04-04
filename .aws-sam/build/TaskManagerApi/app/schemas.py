from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    status: str

class TaskInDB(TaskBase):
    id: str

model_config = {
    "from_attributes": True
}