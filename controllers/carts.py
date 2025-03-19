from fastapi import HTTPException
from crud.cart import CartRepository
from schemas.cart import CartItemSchema

class CartController:
    def __init__(self, repo: CartRepository):
        self.repo = repo
    
    def get_user_cart(self, user_id: str):
        _cart = self.repo.get_cart_id_by_user_id(user_id)
        if _cart is None:
            _new_cart = self.repo.create_cart(user_id)
            return {"cart_id": _new_cart}
        else: return {"cart_id": _cart}
    
    def add_item_to_cart(self, user_id: str, item: CartItemSchema):
        _item = self.repo.add_item_to_cart(user_id, item)
        return _item

    def update_item(self, user_id: str, product_id: str, add_or_substract: int):
        _updated_item = self.repo.update_item_quantity(user_id, product_id, add_or_substract)
        return _updated_item

    def delete_item(self, user_id: str, product_id: str):
        _deleted_item = self.repo.remove_item(user_id, product_id)
        return _deleted_item
    
        