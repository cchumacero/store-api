from fastapi import Depends
from sqlalchemy.orm import Session
from crud.category import CategoryRepository
from controllers.categories import CategoryController
from config.db import get_db


def get_category_repository(db: Session = Depends(get_db)):
    return CategoryRepository(db)

def get_category_controller(repo: CategoryRepository = Depends(get_category_repository)):
    return CategoryController(repo)
