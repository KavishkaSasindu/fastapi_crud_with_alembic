from sqlalchemy import Column,Integer,String
from app.db.session import Base

class Person(Base):
    __tablename__ = "persons"
    
    person_id = Column(Integer,primary_key = True,index = True)
    username = Column(String(30),index = True)
    email = Column(String(30),index = True)
