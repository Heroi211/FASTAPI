from typing import Annotated
from pydantic.v1 import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
        Configurações gerais.
    """
    
    API_VERSION_V: str = "/api/v1"
    DB_URL:str = "postgresql+asyncpg://hero:280387@localhost:5432/API"
    DBBaseModel: Annotated = declarative_base()
    
    class Config:
        case_sensitive = True
        
settings = Settings()