from pydantic_settings import BaseSettings
from dotenv import load_dotenv



#i wanto to specify the path of the .env file
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRES_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()