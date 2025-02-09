from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "55c84cbfa7f9e183da2179cb34cc45526bea05ee80b5bef66ed950534730bf5d"
    ALGORITHM: str = "HS256"
    # 60 minutes * 24 hours * 7 days = 7 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    MYSQL_SERVER_IP : str
    MYSQL_SERVER_PORT : int
    MYSQL_SERVER_USER : str
    MYSQL_SERVER_PASSWORD : str
    MYSQL_DATABASE : str
    
    AWS_ACCESS_KEY : str
    AWS_SECRET_KEY : str
    BUCKET : str = "cv06-bucket2"

    SMTP_ADDRESS : str
    SMTP_PORT : int
    MAIL_ACCOUNT : str
    MAIL_PASSWORD : str
    
    class Config:
        env_file = ".env"
        
        
@lru_cache()
def get_settings():
    return Settings()