import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.db import get_db, Base
from main import app
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL_TEST = os.getenv("DATABASE_URL_TEST")
engine = create_engine(DATABASE_URL_TEST)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Fixture para manejar la sesión de la base de datos en cada test."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.rollback()
    session.close()

@pytest.fixture(scope="function")
def client(db_session):
    """Fixture para el cliente de pruebas, con la base de datos de prueba."""

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_category(client, db_session):
    response = client.post(
        "/categories", json={"name": "Test Category", "image": "Test Image"}
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "Test Category"
    assert data["image"] == "Test Image"

    from models import Category
    category = db_session.query(Category).filter_by(name="Test Category").first()
    assert category is not None
    assert category.image == "Test Image"
