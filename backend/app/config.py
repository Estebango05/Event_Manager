"""
Configuración de la aplicación usando Pydantic BaseSettings.
Carga variables de entorno desde un archivo .env y expone un objeto `settings`.
"""
import os
from pydantic import AnyUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # URL de conexión a PostgreSQL
    DATABASE_URL: str
    # Entorno de la aplicación: development, staging, production
    ENVIRONMENT: str = "development"
    # Puerto donde correrá la aplicación (FastAPI/Uvicorn)
    APP_PORT: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instancia global de settings
settings = Settings()