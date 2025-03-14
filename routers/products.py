from fastapi import APIRouter, HTTPException, Query
from fastapi import Depends
from schemas import ProductSchema, ProductFilterParams
from typing import Optional

from controllers.products import ProductController
from dependencies.product import get_product_controller

router = APIRouter()

@router.post("/")
async def create_product(request: ProductSchema, controller: ProductController = Depends(get_product_controller)):
    return controller.create_product(request)

@router.get("/")
async def get_products(
    title: Optional[str] = Query(None, description="Filtrar por título"),
    min_price: Optional[float] = Query(
        None, description="Filtrar por precio mínimo"),
    max_price: Optional[float] = Query(
        None, description="Filtrar por precio máximo"),
    category: Optional[str] = Query(None, description="Filtrar por categoría"),
    skip: int = 0,
    limit: int = 100,
    controller: ProductController = Depends(get_product_controller)
):
    filters = ProductFilterParams(
        title=title,
        min_price=min_price,
        max_price=max_price,
        category=category,
        skip=skip,
        limit=limit
    )
    return controller.get_products(filters)

@router.get("/{product_id}")
async def get_product_by_id(product_id: str, controller: ProductController = Depends(get_product_controller)):
    return controller.get_product_by_id(product_id)

@router.put("/{product_id}")
async def update_product(product_id: str, request: ProductSchema, controller: ProductController = Depends(get_product_controller)):
    return controller.update_product(product_id, request)

@router.delete("/{product_id}")
async def remove_product(product_id: str, controller: ProductController = Depends(get_product_controller)):
    return controller.remove_product(product_id)

@router.get("/{category_id}")
async def get_products_by_category(category_id: str, controller: ProductController = Depends(get_product_controller)):
    return controller.get_products_by_category(category_id)
