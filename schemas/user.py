from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "String - Nombre del usuario",
                "email": "String - Email del usuario",
                "password": "String - Contraseña del usuario"
            }
        }
    )

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str