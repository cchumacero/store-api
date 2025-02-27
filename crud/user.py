from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from config.auth import hash_password
import uuid


def get_user_by_id(db:Session, user_id:str):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db:Session, username:str):
    return db.query(User).filter_by(username=username).first()

def get_user_by_email(db:Session, email:str):
    return db.query(User).filter_by(email=email).first()

def create_user(db:Session, user:UserCreate):
    _user = User(
        id = str(uuid.uuid4()),
        username = user.username,
        email =  user.email,
        hashed_password = hash_password(user.password)
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user