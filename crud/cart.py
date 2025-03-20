from sqlalchemy.orm import Session
from models.cart import Cart, CartItem
from schemas.cart import CartItemSchema, CartSchema

class CartRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_cart_id_by_user_id(self, user_id: str) -> CartSchema:
        _cart = self.db.query(Cart).filter(Cart.user_id==user_id).first()
        if _cart is None:
            return _cart
        return _cart
    
    def create_cart(self, user_id: str) -> CartSchema:
        _new_cart = Cart(user_id=user_id)
        self.db.add(_new_cart)
        self.db.commit()
        self.db.refresh(_new_cart)
        _cart = self.get_cart_id_by_user_id(user_id=user_id)
        return _cart
    
    def add_item_to_cart(self, user_id: str, item: CartItemSchema):
        _cart = self.get_cart_id_by_user_id(user_id)
        
        _new_item = CartItem(
            cart_id = _cart.id,
            product_id = item.product_id,
            quantity = item.quantity
        )
        self.db.add(_new_item)
        self.db.commit()
        self.db.refresh(_new_item)
        return _new_item
    
    def update_item_quantity(self, user_id: str, product_id: str, add_or_substract: int):
        _cart = self.get_cart_id_by_user_id(user_id)
        _cart_item = self.db.query(CartItem).filter(
            CartItem.cart_id == _cart.id,
            CartItem.product_id == product_id
        ).first()
        
        
        _cart_item.quantity = _cart_item.quantity + add_or_substract
        self.db.commit()
        self.db.refresh(_cart_item)
        return _cart_item
    
    def remove_item(self, user_id: str, product_id: str):
        _cart = self.get_cart_id_by_user_id(user_id)
        _cart_item = self.db.query(CartItem).filter(
            CartItem.cart_id == _cart.id,
            CartItem.product_id == product_id
        ).first()
        
        self.db.delete(_cart_item)
        self.db.commit()
        return _cart_item
        