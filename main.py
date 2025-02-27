from fastapi import FastAPI
import models as model
from routers.categories import router as category_routes
from routers.products import router as product_routes
from routers.auth import router as auth_routes
from routers.users import router as user_routes


app = FastAPI()
app.include_router(router = category_routes, tags=["Categories"], prefix="/categories")
app.include_router(router = product_routes, tags=["Products"], prefix="/products")
app.include_router(router = auth_routes, tags=["Authentication"], prefix="/auth")
app.include_router(router = user_routes, tags=["Users"], prefix="/users")

@app.get("/")
def root():
    return {"message": "Hello World"}

