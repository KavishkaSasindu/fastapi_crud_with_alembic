from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from app.config.settings import settings

DB_URL = settings.database_url()

engine = create_engine(
    DB_URL,
    echo = True
)

LocalSession = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush = False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()    
    