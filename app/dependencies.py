from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
from jose import jwt, JWTError
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
ALGORITHM = "HS256"

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        user_id: str = payload.get("user_id")  

        if not email or not user_id:
            raise HTTPException(status_code=401, detail="Token inválido")

        return {"email": email, "id": user_id}  
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
