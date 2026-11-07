from sqlalchemy.orm import Session
from src.users.dto import UserSchema, LoginSchema
from src.users.model import UserModel
from src.users.security_config import get_password, verify_password
import jwt
from src.utils.settings import settings
from fastapi import HTTPException, status
from datetime import datetime, timedelta

def register(body: UserSchema, db: Session):
    """
    we will check if the ussername or email are individually unique 
    then only we will create/ register the user
    """
    
    is_user_username = db.query(UserModel).filter(UserModel.username == body.username).first()
    is_user_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    
    if is_user_username:
        raise HTTPException(400, detail="Username already exists...")
    if is_user_email:
        raise HTTPException(400, detail="email already exists...")
    
    hash_password = get_password(body.password)
    
    data = body.model_dump()
    new_user: UserModel = UserModel()
    new_user.name = data['name']
    new_user.username = data['username']
    new_user.email = data['email']
    new_user.hashed_password = hash_password
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def login_user(body: LoginSchema, db: Session):
    user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with email: {body.email} does not extist")
    
    if not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    
    
    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    payload = {
        "_id": str(user.id),
        "exp":exp_time.timestamp()
    }
    secret_key = settings.SECRET
    algorithm = settings.ALGORITHM
    token = jwt.encode(payload, secret_key, algorithm)
    
    return {
        "token": token 
    }