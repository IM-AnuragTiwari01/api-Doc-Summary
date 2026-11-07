from fastapi import APIRouter, Depends, status
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.users import controller
from src.users.dto import UserSchema, UserResponseSchema, LoginSchema


user_route = APIRouter(prefix="/user")

@user_route.post("/register-user", response_model=UserResponseSchema)
def register(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)

@user_route.post("/login-user", status_code=status.HTTP_200_OK)
def login_user(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)