import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pydantic_core import BaseSettings

env_path = Path(".")/".env"
load_dotenv(dotenv_path= env_path)


class Settings(BaseSettings):
    DB_USER:str = os.getenv("MYSQL_USER")
    DB_PASSWORD:str = os.getenv("MYQL_USER_PASSWORD")
    DB_NAME:str = os.getenv("MYSQL_DB")
    DB_HOST:str = os.getenv("MYSQL_SERVER")
    DB_PORT:int = int(os.getenv("MYSQL_SERVER_PORT"))
    DATABASE_URL:str = f'mysql+pymsql://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}' %quote_plus(DB_PASSWORD)
    
    
    
def get_setting()->Settings:
    return Settings()
  
