from pydantic import BaseModel, EmailStr
from typing import Optional

class Task(BaseModel):
    title: str
    description: str
    status: str = "To Do"

class User(BaseModel):
    username: str
    password: str

class UserIn(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str