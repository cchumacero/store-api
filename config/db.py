from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Creamos el motor
if os.getenv("ENVIROMENT") == "development":
    engine = create_engine(os.getenv("DATABASE_URL"))
else:
    engine = create_engine(os.getenv("POSTGRES_URL"))
    
# Luego creamos los parametros para las sessiones que se creen de dicho motor
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

# Creamos el mapeador ORM 
Base = declarative_base()

 # Creamos la función para el uso de session de la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()