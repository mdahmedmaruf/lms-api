from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', case_sensitive=True, extra='ignore')

    # App
    APP_NAME: str = 'Library Management API'
    ENVIRONMENT: str = 'development'
    DEBUG: bool = True

    # Security
    SECRET_KEY: str = ''

    # Database
    DATABASE_URL: str ='sqlite+aiosqlite:///./library.db'

@lru_cache
def get_settings() -> Settings:
    # Cached - avoids re-reading .env on every import.
    return Settings()


settings = get_settings()