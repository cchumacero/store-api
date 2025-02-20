from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.db import SessionLocal, get_db
from sqlalchemy.orm import Session
from schemas import ProductSchema, Response
from crud import product

router = APIRouter()

@router.post("/")
async def create_product(request: ProductSchema, db: Session = Depends(get_db)):
    _product = product.create_product(db, request)
    return _product

@router.get("/")
async def get_products(offset: int | None = None, limit: int | None = None, db: Session = Depends(get_db)):
    _products = product.get_products(db, offset, limit)
    return _products

@router.get("/{product_id}")
async def get_product_by_id(product_id: str, db: Session = Depends(get_db)):
    _product = product.get_product_by_id(db, product_id)
    if _product is None:
        raise HTTPException(status_code= 404, detail="Product Not Found")
    return _product
        

@router.put("/{product_id}")
async def update_product(product_id: str, request: ProductSchema, db:Session = Depends(get_db)):
    try:
        _product = product.update_product(db, product_id, request.title, request.price, request.description, request.category, request.images)
        return _product
    except Exception as e:
        # return Response(status="bad", code=304, message="the updated gone wrong")
        raise HTTPException(status_code= 404, detail="the updated gone wrong, not modified")

@router.delete("/{product_id}")
async def remove_product(product_id: str, db:Session = Depends(get_db)):
    try:
        _product = product.remove_product(db, product_id)
        return _product
    except Exception as e:
        # return Response(status="bad", code=304, message="the updated gone wrong")
        raise HTTPException(status_code= 404, detail="the deleted gone wrong, not deleted")

