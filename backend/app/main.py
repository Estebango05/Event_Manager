from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.adapters.inbound.rest.events_router import router as events_router


def create_app() -> FastAPI:
    """
    Configura y retorna la aplicación FastAPI.
    """
    app = FastAPI(
        title="API de Eventos",
        version="1.0.0",
        description="API para la administración de eventos",
    )
        # Configuración de CORS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",  # tu front en dev
            # Puedes poner "*" para permitir todos los orígenes
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(events_router)
    return app


app = create_app()
