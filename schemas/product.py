from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductSchema(BaseModel):
    title: str
    price: float
    description: str
    category: str
    images: list[str]
    
    model_config = ConfigDict(
        json_schema_extra = {
        "example": {
                "title": "String - Nombre del producto",
                "price": "Float - Precio del producto",
                "description": "String - Descripción del producto",
                "category": "String - Id de una categoría existente",
                "image": "String - Link de una imagen" 
            }
        
        }
    )

class ProductFilterParams(BaseModel):
    title: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    category: Optional[str] = None
    skip: int = 0
    limit: int = 100