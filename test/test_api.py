import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.db import get_db, Base
from main import app
from dotenv import load_dotenv
import os
from crud import category

load_dotenv()

DATABASE_URL_TEST = os.getenv("DATABASE_URL_TEST")
engine = create_engine(DATABASE_URL_TEST)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Fixture para manejar la sesión de la base de datos en cada test."""
    Base.metadata.create_all(bind=engine)
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

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
    assert response.status_code == 201
    _category = category.get_category_by_name(db_session, "Test Category")
    assert _category is not None
    assert _category.image == "Test Image"

def test_get_categories(client):
    client.post(
        "/categories", json={"name": "Test Category 1", "image": "Test Image 1"}
    )
    client.post(
        "/categories", json={"name": "Test Category 2", "image": "Test Image 2"}
    )
    
    response = client.get("/categories")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]["name"] == "Test Category 1"
    assert data[0]["image"] == "Test Image 1"
    assert data[1]["name"] == "Test Category 2"
    assert data[1]["image"] == "Test Image 2"
    

def test_update_category(client, db_session):
    post_response = client.post(
        "/categories", json={"name": "Test Category 1", "image": "Test Image 1"}
    )
    assert post_response.status_code == 201
    _category = post_response.json()
    
    put_response = client.put(
        f"/categories/{_category["id"]}", json={"name": "Updated Test Category 1", "image": "Updated Test Image 1"}
    )
    
    assert put_response.status_code == 200
    _updated_category = put_response.json()
    assert _updated_category["name"] == "Updated Test Category 1"
    assert _updated_category["image"] == "Updated Test Image 1"
    
def test_remove_category(client, db_session):
    post_response = client.post(
        "/categories", json={"name": "Test Category 1", "image": "Test Image 1"}
    )
    assert post_response.status_code == 201
    _category = post_response.json()
    
    delete_response = client.delete(
        f"/categories/{_category["id"]}"
    )
    
    assert delete_response.status_code == 200
    _deleted_category = category.get_category_by_id(db_session, _category["id"])
    assert _deleted_category == None
    
    
    
    