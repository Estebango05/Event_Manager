from typing import List, Optional
from datetime import date
from .entities import Event

# Importamos supuestas funciones de adaptador para persistencia
from app.adapters.outbound.persistence.postgres_event_repository import (
    insert_event,
    fetch_event_by_id,
    fetch_all_events,
    update_event_in_db,
    delete_event_by_id,
)


class EventRepository:
    """
    Repositorio de eventos que delega en funciones de adaptador de PostgreSQL.
    """

    def save(self, event: Event) -> Event:
        """
        Guarda un nuevo evento en la base de datos y retorna la entidad con ID asignado.
        """
        created = insert_event(
            name=event.name,
            eventDate=event.eventDate,
            description=event.description,
            location=event.location,
        )
        # Supongamos que insert_event devuelve un dict con los campos incluyendo 'id'
        return Event(**created)

    def get_by_id(self, event_id: int) -> Optional[Event]:
        """
        Obtiene un evento por su ID. Retorna None si no existe.
        """
        record = fetch_event_by_id(event_id)
        if record is None:
            return None
        return Event(**record)

    def list(self,  filteredDate: Optional[date] = None) -> List[Event]:
        """
        Devuelve una lista con todos los eventos.
        """
        records = fetch_all_events(filteredDate)
        return [Event(**r) for r in records]

    def update(self, event: Event) -> Event:
        """
        Actualiza un evento existente y retorna la entidad actualizada.
        """
        updated = update_event_in_db(
            event_id=event.id,
            name=event.name,
            eventDate=event.eventDate,
            description=event.description,
            location=event.location,
        )
        return Event(**updated)

    def delete(self, event_id: int) -> None:
        """
        Elimina un evento por su ID.
        """
        delete_event_by_id(event_id)
