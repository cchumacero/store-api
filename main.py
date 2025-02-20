from fastapi import FastAPI
import models as model
from routers.categories import router as category_routes



app = FastAPI()
app.include_router(router = category_routes, tags=["Categories"], prefix="/categories")
@app.get("/")
def root():
    return {"message": "Hello World"}

