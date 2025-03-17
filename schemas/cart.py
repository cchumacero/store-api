from typing import List,Optional,Generic, TypeVar
from pydantic import BaseModel, ConfigDict

class CartItemSchema(BaseModel):
    product_id: str
    quantity: int


class CartSchema(BaseModel):
    cart_id: str
    user_id: str
    products: CartItemSchema
    
