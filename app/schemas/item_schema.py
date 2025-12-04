from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    item_name: str
    item_desc: str
    item_type: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Items(ItemBase):
    item_id: int

    class Config:
        from_attribute = True

