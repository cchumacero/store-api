from fastapi import APIRouter, Depends
from schemas import UserCreate, Token

from controllers.authentications import AuthController
from dependencies.auth import get_auth_controller

router = APIRouter()

@router.post("/register", response_model=Token)
def register(user_data: UserCreate, controller: AuthController = Depends(get_auth_controller)):
    return controller.register(user_data)

@router.post("/login", response_model=Token)
def login(user_data: UserCreate, controller: AuthController = Depends(get_auth_controller)):
    return controller.login(user_data)