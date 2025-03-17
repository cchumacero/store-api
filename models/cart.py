from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import uuid

class Cart(Base):
    __tablename__ = "carts"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), unique=True, index=True)
    
    items = relationship("CartItem", back_populates="cart")
    
class CartItem(Base):
    __tablename__ = "cart_items"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    cart_id = Column(String, ForeignKey("carts.id"), unique=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), unique=True, index=True)
    quantity = Column(Integer)
    
    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")
    
