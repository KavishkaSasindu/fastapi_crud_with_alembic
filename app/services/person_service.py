from typing import List

from fastapi.params import Depends
from app.db.session import get_db
from app.models.person import Person
from sqlalchemy.orm import Session
import app.schemas.person_schema as person_schema

def person_create(data: person_schema.PersonCreate, db: Session = Depends(get_db))->Person:
    person_data = Person(**data.model_dump())
    db.add(person_data)
    db.commit()
    db.refresh(person_data)
    return person_data

def get_all_persons(db: Session = Depends(get_db))->List[type[Person]]:
    return db.query(Person).offset(0).all()