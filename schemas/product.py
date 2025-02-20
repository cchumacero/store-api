from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, Field
from datetime import datetime

class ProductSchema(BaseModel):
    title: str
    price: float
    description: str
    category: str
    images: list[str]
    
    class Config:
        json_schema_extra = {
        "example":
            {
                "title": "String - Nombre del producto",
                "price": "Float - Precio del producto",
                "description": "String - Descripción del producto",
                "category": "String - Id de una categoría existente",
                "image": "String - Link de una imagen" 
            }
        
        }
    