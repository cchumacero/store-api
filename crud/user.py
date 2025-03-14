from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id:str):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username:str):
        return self.db.query(User).filter_by(username=username).first()

    def get_user_by_email(self, email:str):
        return self.db.query(User).filter_by(email=email).first()

    def create_user(self, user:UserCreate):
        _user = User(
            username = user.username,
            email =  user.email,
            hashed_password = user.password
        )
        self.db.add(_user)
        self.db.commit()
        self.db.refresh(_user)
        return _user

    def update_username(self, user_id: str, username: str):
        _user = self.get_user_by_id(user_id)
        _user.username = username
        self.db.commit()
        self.db.refresh(_user)
        return _user

    