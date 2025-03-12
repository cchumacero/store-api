from fastapi import Depends
from sqlalchemy.orm import Session
from config.db import get_db
from crud.user import UserRepository
from controllers.users import UserController

def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)

def get_user_controller(repo: UserRepository = Depends(get_user_repository)):
    return UserController(repo)