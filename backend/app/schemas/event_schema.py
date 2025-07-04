from pydantic import BaseModel
from datetime import date
from typing import Optional


class EventBase(BaseModel):
    """
    Esquema base para eventos con atributos comunes.
    """
    name: str
    eventDate: date
    description: str
    location: str


class EventCreate(EventBase):
    """Esquema para crear un nuevo evento."""
    pass


class EventRead(EventBase):
    """Esquema para leer un evento con ID incluido."""
    id: int

    class Config:
        orm_mode = True


class EventUpdate(BaseModel):
    """Esquema para actualizar un evento (todos los campos opcionales)."""
    name: Optional[str] = None
    eventDate: Optional[date] = None
    description: Optional[str] = None
    location: Optional[str] = None