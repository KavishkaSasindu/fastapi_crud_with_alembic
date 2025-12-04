from fastapi.params import Depends
from app.db.session import get_db
from app.models.person import Person
from sqlalchemy.orm import Session
from app.schemas.person_schema import PersonCreate

def person_create(data: PersonCreate, db: Session = Depends(get_db))->Person:
    person_data = Person(**data.model_dump())
    db.add(person_data)
    db.commit()
    db.refresh(person_data)
    return person_data

