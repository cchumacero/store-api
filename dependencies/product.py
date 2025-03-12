from fastapi import Depends
from sqlalchemy.orm import Session
from crud.product import ProductRepository
from controllers.products import ProductController
from config.db import get_db


def get_product_repository(db: Session = Depends(get_db)):
    return ProductRepository(db)

def get_product_controller(repo: ProductRepository = Depends(get_product_repository)):
    return ProductController(repo)
