from sqlalchemy.orm import Session
from models import Product
from schemas import ProductSchema, ProductFilterParams
import uuid

def get_products(db:Session, filters: ProductFilterParams):
    query = db.query(Product)
    
    if filters.title:
        query = query.filter(Product.title.ilike(f"%{filters.title}%"))
        
    if filters.min_price:
        query = query.filter(Product.price >= filters.min_price)
        
    if filters.max_price:
        query = query.filter(Product.price <= filters.max_price)
    
    if filters.category:
        query = query.filter(Product.category == filters.category)
        
    return query.offset(filters.skip).limit(filters.limit).all()
    
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