from sqlalchemy.orm import Session
from models import Category
from schemas import CategorySchema
import uuid

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_category(self, skip: int = 0, limit: int = 100):
        return self.db.query(Category).offset(skip).limit(limit).all()

    def get_category_by_id(self, category_id: str):
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_category_by_name(self, category_name: str):
        return self.db.query(Category).filter_by(name=category_name).first()

    def create_category(self, category: CategorySchema):
        _category = Category(
            id=str(uuid.uuid4()),
            name=category.name,
            image=category.image
        )
        self.db.add(_category)
        self.db.commit()
        self.db.refresh(_category)
        return _category

    def remove_category(self, category_id: str):
        _category = self.get_category_by_id(category_id)
        self.db.delete(_category)
        self.db.commit()
        return _category

    def update_category(self, category_id: str, name: str, image: str):
        _category = self.get_category_by_id(category_id)
        _category.name = name
        _category.image = image
        self.db.commit()
        self.db.refresh(_category)
        return _category
