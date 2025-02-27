from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from schemas import UserCreate, Token
from config.auth import verify_password, create_access_token
from datetime import timedelta
from crud import user

router = APIRouter()

@router.post("/register", response_model=Token)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    _user = user.get_user_by_email(db, user_data.email)
    _user = user.get_user_by_username(db, user_data.username)
    
    if _user:
        raise HTTPException(status_code=400, detail="Email or Username already registered")
    
    new_user = user.create_user(db, user_data)

    access_token = create_access_token(data={"sub": new_user.id}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(user_data: UserCreate, db: Session = Depends(get_db)):
    _user = user.get_user_by_email(db, user_data.email)
    
    if not _user or not verify_password(user_data.password, _user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": _user.id}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}
