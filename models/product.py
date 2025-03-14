from sqlalchemy import Column, Integer, String, Float, ForeignKey, ARRAY, DateTime, func
from config.db import Base
import uuid

class Product(Base):
    __tablename__ = "products"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String)
    price = Column(Float)
    description = Column(String)
    category = Column(String, ForeignKey('categories.id'))
    images = Column(ARRAY(String))
    created_at = Column(DateTime, default=func.now())
    

