from fastapi import FastAPI
import models as model
from routers.categories import router as category_routes
from routers.products import router as product_routes



app = FastAPI()
app.include_router(router = category_routes, tags=["Categories"], prefix="/categories")
app.include_router(router = product_routes, tags=["Products"], prefix="/products")
@app.get("/")
def root():
    return {"message": "Hello World"}

