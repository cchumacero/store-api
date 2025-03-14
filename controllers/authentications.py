from fastapi import HTTPException
from schemas.user import UserCreate, UserResponse
from crud.user import UserRepository
from schemas import UserCreate, Token
from config.auth import verify_password, create_access_token, hash_password
from datetime import timedelta

class AuthController:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        
    def register(self, user_data: UserCreate):
        _user = self.repo.get_user_by_email(user_data.email)
        _user = self.repo.get_user_by_username(user_data.username)
        
        if _user:
            raise HTTPException(status_code=400, detail="Email or Username already registered")
        
        user_data.password = hash_password(user_data.password)
        new_user = self.repo.create_user(user_data)

        access_token = create_access_token(data={"sub": new_user.id}, expires_delta=timedelta(minutes=30))
        return {"access_token": access_token, "token_type": "bearer"}

    def login(self, user_data: UserCreate):
        _user = self.repo.get_user_by_email(user_data.email)
        
        if not _user or not verify_password(user_data.password, _user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        access_token = create_access_token(data={"sub": _user.id}, expires_delta=timedelta(minutes=30))
        return {"access_token": access_token, "token_type": "bearer"}