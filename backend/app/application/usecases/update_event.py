from app.domain.entities import Event
from app.domain.repository import EventRepository
from app.schemas.event_schema import EventUpdate


class UpdateEvent:
    """
    Caso de uso: actualizar datos de un evento existente.
    """

    def __init__(self, repository: EventRepository):
        self.repository = repository

    def execute(self, event_id: int, data: EventUpdate) -> Event:
        """
        Fusiona valores actualizados y persiste el cambio.
        :param event_id: ID del evento.
        :param data: DTO con campos opcionales.
        :return: Entidad Event actualizada.
        """
        existing = self.repository.get_by_id(event_id)
        if existing is None:
            raise ValueError(f"Evento con ID {event_id} no encontrado.")

        updated_event = Event(
            id=event_id,
            name=data.name or existing.name,
            eventDate=data.eventDate or existing.eventDate,
            description=data.description or existing.description,
            location=data.location or existing.location,
        )
        return self.repository.update(updated_event)