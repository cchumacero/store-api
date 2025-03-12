from fastapi import APIRouter, Depends, HTTPException, status
from config.auth import get_current_user
from controllers.users import UserController
from dependencies.user import get_user_controller

router = APIRouter()

@router.get("/profile")
def get_user_profile(user_id: str = Depends(get_current_user), controller: UserController = Depends(get_user_controller) ):
    return controller.get_user(user_id)
