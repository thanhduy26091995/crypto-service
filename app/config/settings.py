import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    binance_api_key: str = os.getenv('BINANCE_API_KEY', "")
    binance_secret_key: str = os.getenv('BINANCE_SECRET_KEY', "")
    fetch_interval: int = 1  # In minutes
    database_url: str = os.getenv('DATABASE_URL', "")

    class Config:
        env_file = ".env"


# Instantiate the settings
settings = Settings()
