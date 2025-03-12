from schemas.user import UserCreate, UserResponse
from crud.user import UserRepository

class UserController:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        
    def get_user(self, user_id: str):
        _user = self.repo.get_user_by_id(user_id)
        data = {
            "id": _user.id,
            "username": _user.username,
            "email": _user.email
        }
        return data