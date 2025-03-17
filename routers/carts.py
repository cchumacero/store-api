from fastapi import APIRouter, status
from fastapi import Depends
from controllers.carts import CartController
from dependencies.cart import get_cart_controller
from schemas.cart import CartItemSchema

router = APIRouter()

@router.get("/{user_id}")
async def get_cart(user_id: str, controller: CartController = Depends(get_cart_controller)):
    return controller.get_user_cart(user_id)

@router.post("/{user_id}/item")
async def add_item(user_id: str, request: CartItemSchema, controller: CartController = Depends(get_cart_controller)):
    return controller.add_item_to_cart(user_id, request)

@router.put("/{user_id}/item/{product_id}/add")
async def add_one(user_id: str, product_id: str, controller: CartController = Depends(get_cart_controller)):
    return controller.update_item(user_id, product_id, 1)

@router.put("/{user_id}/item/{product_id}/substract")
async def remove_one(user_id: str, product_id: str, controller: CartController = Depends(get_cart_controller)):
    return controller.update_item(user_id, product_id, -1)

@router.delete("/{user_id}/item/{product_id}")
async def delete_item(user_id: str, product_id: str, controller: CartController = Depends(get_cart_controller)):
    return controller.delete_item(user_id, product_id)