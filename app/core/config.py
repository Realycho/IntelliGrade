from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "IntelliGrade API"
    DEBUG_MODE: bool = False

    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/intelligrade_db" # Example URL

    # JWT settings
    SECRET_KEY: str = "YOUR_SECRET_KEY_NEEDS_TO_BE_CHANGED" # IMPORTANT: Change this in production!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Access tokens expire after 30 minutes

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        # In Pydantic V2, this would be extra = 'ignore' or 'allow' if needed
        # For V1, this is fine.

settings = Settings()
