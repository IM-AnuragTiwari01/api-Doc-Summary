import jwt 
from src.users.model import UserModel
from jwt import InvalidTokenError
from fastapi import HTTPException, Request, Depends, status
from sqlalchemy.orm import Session
from src.utils.settings import settings
from src.utils.db import get_db

def is_authenticated(request: Request, db: Session = Depends(get_db)):
    try:
        token = request.headers.get('Authorization')
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UnAUTHORIZED, detail = "User Unauthorized")
        token = token.split(" ")[-1]
        secret_key = settings.SECRET
        algorithm = settings.ALGORITHM
        data = jwt.decode(token, secret_key, algorithm)
        print(data)
        
        user_id = data.get("_id")
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Unauthorized")
        return user
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Unauthorized")
        
        