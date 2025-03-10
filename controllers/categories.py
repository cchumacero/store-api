from fastapi import APIRouter, HTTPException, Path, status
from schemas import CategorySchema, Response
from crud.category import CategoryRepository


class CategoryController:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def create_category(self, new_category: CategorySchema):
        _category = self.repo.create_category(new_category)
        return _category

    def get_categories(self):
        _categories = self.repo.get_category()
        return _categories

    def update_category(self, category_id: str, request: CategorySchema):
        try:
            _category = self.repo.update_category(
                category_id, request.name, request.image)
            return _category
        except Exception as e:
            raise HTTPException(
                status_code=404, detail="the updated gone wrong, not modified")

    def remove_category(self, category_id: str):
        try:
            _category = self.repo.remove_category(category_id)
            return _category
        except Exception as e:
            raise HTTPException(
                status_code=404, detail="the deleted gone wrong, not deleted")
