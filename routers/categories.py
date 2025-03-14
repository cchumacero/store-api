from fastapi import APIRouter, status
from fastapi import Depends
from schemas import CategorySchema
from controllers.categories import CategoryController
from dependencies.category import get_category_controller

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(request: CategorySchema, controller: CategoryController = Depends(get_category_controller)):
    return controller.create_category(request)

@router.get("/")
async def get_categories(controller: CategoryController = Depends(get_category_controller)):
    return controller.get_categories()

@router.put("/{category_id}")
async def update_category(category_id: str, request: CategorySchema, controller: CategoryController = Depends(get_category_controller)):
    return controller.update_category(category_id, request)

@router.delete("/{category_id}")
async def remove_category(category_id: str, controller: CategoryController = Depends(get_category_controller)):
    return controller.remove_category(category_id)

'''
@router.get("/{category_id}/products")
async def get_categories(category_id: str, db: Session = Depends(get_db)):
    _products = product.get_product_by_category(db, category_id)
    return _products
'''