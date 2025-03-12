from fastapi import HTTPException, Path, Query
from schemas import ProductSchema, ProductFilterParams
from crud.product import ProductRepository

class ProductController:
    def __init__(self, repo: ProductRepository):
        self.repo = repo
    
    def create_product(self, request: ProductSchema):
      _product = self.repo.create_product(request)
      return _product
    
    def get_products(self, filters: ProductFilterParams):
        _products = self.repo.get_products(filters=filters)
        return _products

    def get_product_by_id(self, product_id: str):
        _product = self.repo.get_product_by_id(product_id)
        if _product is None:
            raise HTTPException(status_code=404, detail="Product Not Found")
        return _product

    def update_product(self, product_id: str, request: ProductSchema):
        try:
            _product = self.repo.update_product(
                product_id, request.title, request.price, request.description, request.category, request.images)
            return _product
        except Exception as e:
            # return Response(status="bad", code=304, message="the updated gone wrong")
            raise HTTPException(
                status_code=404, detail="the updated gone wrong, not modified")

    def remove_product(self, product_id: str):
        try:
            _product = self.repo.remove_product(product_id)
            return _product
        except Exception as e:
            # return Response(status="bad", code=304, message="the updated gone wrong")
            raise HTTPException(
                status_code=404, detail="the deleted gone wrong, not deleted")