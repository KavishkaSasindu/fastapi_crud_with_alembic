from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.person_service import person_create
from app.schemas.person_schema import PersonCreate

router = APIRouter(prefix="/person", tags=["person"])

@router.post("/",response_model=PersonCreate,status_code=status.HTTP_201_CREATED)
def create_person(person_req: PersonCreate, db: Session = Depends(get_db)):
    try:
        return person_create(person_req, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))