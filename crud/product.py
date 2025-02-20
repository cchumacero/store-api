from sqlalchemy.orm import Session
from models import Product
from schemas import ProductSchema
import uuid

def get_products(db:Session, skip:int=0, limit:int=100):
    return db.query(Product).offset(skip).limit(limit).all()

def get_product_by_id(db:Session, product_id:str):
    return db.query(Product).filter(Product.id == product_id).first()

def get_product_by_category(db:Session, category_id:str):
    return db.query(Product).filter(Product.category == category_id).all()

def create_product(db:Session, product:ProductSchema):
    _product = Product(
        id = str(uuid.uuid4()),
        title = product.title,
        price = product.price,
        description = product.description,
        category = product.category,
        images = product.images,
    )
    print(_product.images)
    db.add(_product)
    db.commit()
    db.refresh(_product)
    return _product

def remove_product(db:Session, product_id: str):
    _product = get_product_by_id(db, product_id)
    db.delete(_product)
    db.commit()
    return _product

def update_product(db:Session, product_id: str, title: str, price: float, description: str, category: str, images: str):
    _product = get_product_by_id(db, product_id)
    _product.title = title
    _product.price = price
    _product.description = description
    _product.category = category
    _product.images = images
    db.commit()
    db.refresh(_product)
    return _product