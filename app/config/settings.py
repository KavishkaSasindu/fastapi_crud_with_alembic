from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    db_username:str
    db_password:str
    db_name:str
    
    def database_url(self):
        encode_pwd = quote_plus(self.db_password)
        database_url = f"mysql+mysqldb://{self.db_username}:{encode_pwd}@localhost:3306/{self.db_name}"
        return database_url
    
    class Config:
        env_file = ".env"
        
settings = Settings()