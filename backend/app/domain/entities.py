from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Event:
    """
    Entidad Event del dominio.

    Attributes:
        id: Optional[int] - Identificador único del evento (None si es nuevo).
        name: str - Nombre del evento.
        eventDate: date - Fecha del evento.
        description: str - Descripción del evento.
        location: str - Lugar donde se realizará el evento.
    """
    id: Optional[int]
    name: str
    eventDate: date
    description: str
    location: str