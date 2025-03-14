from sqlalchemy.orm import Session
from models import Product
from schemas import ProductSchema, ProductFilterParams
import uuid

class ProductRepository:
    
    def __init__(self, db: Session):
        self.db = db

    def get_products(self, filters: ProductFilterParams):
        query = self.db.query(Product)
        
        if filters.title:
            query = query.filter(Product.title.ilike(f"%{filters.title}%"))
            
        if filters.min_price:
            query = query.filter(Product.price >= filters.min_price)
            
        if filters.max_price:
            query = query.filter(Product.price <= filters.max_price)
        
        if filters.category:
            query = query.filter(Product.category == filters.category)
            
        return query.offset(filters.skip).limit(filters.limit).all()
        
    def get_product_by_id(self, product_id:str):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def get_product_by_category(self, category_id:str):
        return self.db.query(Product).filter(Product.category == category_id).all()

    def create_product(self, product:ProductSchema):
        _product = Product(
            title = product.title,
            price = product.price,
            description = product.description,
            category = product.category,
            images = product.images,
        )
        print(_product.images)
        self.db.add(_product)
        self.db.commit()
        self.db.refresh(_product)
        return _product

    def remove_product(self, product_id: str):
        _product = self.get_product_by_id(product_id)
        self.db.delete(_product)
        self.db.commit()
        return _product

    def update_product(self, product_id: str, title: str, price: float, description: str, category: str, images: str):
        _product = self.get_product_by_id(product_id)
        _product.title = title
        _product.price = price
        _product.description = description
        _product.category = category
        _product.images = images
        self.db.commit()
        self.db.refresh(_product)
        return _product