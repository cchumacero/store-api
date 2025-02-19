from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    name: str
    image: str
    
    

class Response(BaseModel):
    id: str
    name: str
    image: str