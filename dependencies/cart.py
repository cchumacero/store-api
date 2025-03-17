from fastapi import Depends
from sqlalchemy.orm import Session
from crud.cart import CartRepository
from controllers.carts import CartController
from config.db import get_db

def get_cart_repository(db: Session = Depends(get_db)):
    return CartRepository(db)

def get_cart_controller(repo: CartRepository = Depends(get_cart_repository)):
    return CartController(repo)