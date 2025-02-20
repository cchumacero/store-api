from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    name: str
    image: str
    
    class Config:
        json_schema_extra = {
        "example":
            {
                "name": "String - Nombre de la categoría",
                "image": "String - Link de una imagen" 
            }
        
        }
    
    

class Response(BaseModel):
    status: str
    code: int
    message: str