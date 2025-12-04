from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import app.services.item_service as item_service
import app.schemas.item_schema as item_schema
from app.db.session import get_db

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=item_schema.ItemCreate, status_code=status.HTTP_201_CREATED)
def item_create(item_req: item_schema.ItemCreate, db: Session = Depends(get_db)):
    try:
        return item_service.item_create(item_req, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.get("/",response_model=List[item_schema.GetItems], status_code=status.HTTP_200_OK)
def get_items(db: Session = Depends(get_db)):
    try:
        all_items = item_service.get_all_items(db)
        if len(all_items) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return all_items
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))