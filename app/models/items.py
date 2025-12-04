from sqlalchemy import Column, Integer, String, Text
from app.db.session import Base

class Items(Base):
    __tablename__ = "items"

    item_id = Column(Integer,primary_key=True,index=True)
    item_name = Column(String(30),nullable=False)
    item_desc = Column(Text(),nullable=False)
    item_type = Column(String(30),nullable=True)
