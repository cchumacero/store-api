from sqlalchemy import Column, Integer, String
from config.db import Base
import uuid

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    image = Column(String)
    


    

    