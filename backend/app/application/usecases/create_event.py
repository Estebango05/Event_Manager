from app.domain.entities import Event
from app.domain.repository import EventRepository
from app.schemas.event_schema import EventCreate


class CreateEvent:
    """
    Caso de uso: crear un nuevo evento.
    """

    def __init__(self, repository: EventRepository):
        self.repository = repository

    def execute(self, data: EventCreate) -> Event:
        """
        Valida datos y persiste un nuevo evento.
        :param data: DTO con datos validados.
        :return: Entidad Event con ID asignado.
        """
        event = Event(
            id=None,
            name=data.name,
            eventDate=data.eventDate,
            description=data.description,
            location=data.location,
        )
        return self.repository.save(event)
