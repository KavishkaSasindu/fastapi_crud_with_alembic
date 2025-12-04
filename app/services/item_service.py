from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.items import Items
import app.schemas.item_schema as item_schema

def item_create(data: item_schema.ItemCreate, db: Session = Depends(get_db))->Items:
    item_data = Items(**data.model_dump())
    db.add(item_data)
    db.commit()
    db.refresh(item_data)
    return item_data
