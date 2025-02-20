from sqlalchemy.orm import Session
from models import Category
from schemas import CategorySchema
import uuid

def get_category(db:Session, skip:int=0, limit:int=100):
    return db.query(Category).offset(skip).limit(limit).all()

def get_category_by_id(db:Session, category_id:int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db:Session, category:CategorySchema):
    _category = Category(
        id = str(uuid.uuid4()),
        name = category.name,
        image = category.image
    )
    db.add(_category)
    db.commit()
    db.refresh(_category)
    return _category

def remove_category(db:Session, category_id: str):
    _category = get_category_by_id(db, category_id)
    db.delete(_category)
    db.commit()
    return _category

def update_category(db:Session, category_id: str, name: str, image: str):
    _category = get_category_by_id(db, category_id)
    _category.name = name
    _category.image = image
    db.commit()
    db.refresh(_category)
    return _category