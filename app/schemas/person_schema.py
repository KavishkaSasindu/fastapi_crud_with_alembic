from pydantic import BaseModel,EmailStr

class PersonBase(BaseModel):
    username : str
    email : EmailStr

class PersonCreate(PersonBase):
    pass

class PersonGetOne(PersonBase):
    person_id: int

    class Config:
        from_attribute = True


