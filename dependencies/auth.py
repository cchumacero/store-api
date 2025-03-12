from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.db import get_db
from crud.user import UserRepository
from controllers.authentications import AuthController

def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)

def get_auth_controller(repo: UserRepository = Depends(get_user_repository)):
    return AuthController(repo)
