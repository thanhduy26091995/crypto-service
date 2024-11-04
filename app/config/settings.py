from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    binance_api_key: str = ""
    binance_secret_key: str = ""
    fetch_interval: int = 10  # In minutes

    class Config:
        env_file = ".env"


settings = Settings()
