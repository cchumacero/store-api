from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.db import SessionLocal, get_db
from sqlalchemy.orm import Session
from schemas import CategorySchema, Response
from crud import category

router = APIRouter()

@router.post("/")
async def create_category(request: CategorySchema, db: Session = Depends(get_db)):
    _category = category.create_category(db, request)
    return _category

@router.get("/")
async def get_categories(db: Session = Depends(get_db)):
    _categories = category.get_category(db)
    return _categories

@router.put("/{category_id}")
async def update_category(category_id: str, request: CategorySchema, db:Session = Depends(get_db)):
    try:
        _category = category.update_category(db, category_id, request.name, request.image)
        return _category
    except Exception as e:
        # return Response(status="bad", code=304, message="the updated gone wrong")
        raise HTTPException(status_code= 404, detail="the updated gone wrong, not modified")

@router.delete("/{category_id}")
async def remove_category(category_id: str, db:Session = Depends(get_db)):
    try:
        _category = category.remove_category(db, category_id)
        return _category
    except Exception as e:
        # return Response(status="bad", code=304, message="the updated gone wrong")
        raise HTTPException(status_code= 404, detail="the deleted gone wrong, not deleted")

