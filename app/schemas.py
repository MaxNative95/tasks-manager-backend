from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"
    user_id: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TaskInDB(TaskBase):
    id: str

model_config = {
    "from_attributes": True
}