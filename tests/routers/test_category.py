import pytest
import json
from crud import category

class Category:
    def __init__(self, name: str, image: str):
        self.name = name
        self.image = image

    def to_dict(self):
        return {"name": self.name, "image": self.image}

class CategoryBuilder:
    def __init__(self):
        self._name = "Test Category 1"
        self._image = "Test Image 1"
    
    def build(self):
        return Category(self._name, self._image)

category_a = Category("Test Category 1", "Test Image 1")
category_a_json = category_a.to_dict()

category_b = Category("Test Category 2", "Test Image 2")
category_b_json = category_b.to_dict()

category_update = Category("Updated Test Category 1", "Updated Test Image 1")
category_update_json = category_update.to_dict()

def test_create_category(client, db_session):
    response = client.post(
        "/categories", json=category_a_json
    )
    assert response.status_code == 201
    _category = category.get_category_by_name(db_session, category_a.name)
    assert _category is not None
    assert _category.image == category_a.image

def test_get_categories(client):
    client.post(
        "/categories", json=category_a_json
    )
    client.post(
        "/categories", json=category_b_json
    )
    
    response = client.get("/categories")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]["name"] == category_a.name
    assert data[0]["image"] == category_a.image
    assert data[1]["name"] == category_b.name
    assert data[1]["image"] == category_b.image
    

def test_update_category(client, db_session):
    post_response = client.post(
        "/categories", json=category_a_json
    )
    assert post_response.status_code == 201
    _category = post_response.json()
    
    put_response = client.put(
        f"/categories/{_category["id"]}", json=category_update_json
    )
    
    assert put_response.status_code == 200
    _updated_category = put_response.json()
    assert _updated_category["name"] == category_update.name
    assert _updated_category["image"] == category_update.image
    
def test_remove_category(client, db_session):
    post_response = client.post(
        "/categories", json=category_a_json
    )
    assert post_response.status_code == 201
    _category = post_response.json()
    
    delete_response = client.delete(
        f"/categories/{_category["id"]}"
    )
    
    assert delete_response.status_code == 200
    _deleted_category = category.get_category_by_id(db_session, _category["id"])
    assert _deleted_category == None
    
    
    
    