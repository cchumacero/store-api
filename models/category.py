from sqlalchemy import Column, Integer, String
from config.db import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    


    

    