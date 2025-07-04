from typing import Optional
from app.domain.entities import Event
from app.domain.repository import EventRepository


class GetEvent:
    """
    Caso de uso: obtener un evento por ID.
    """

    def __init__(self, repository: EventRepository):
        self.repository = repository

    def execute(self, event_id: int) -> Optional[Event]:
        """
        :param event_id: ID del evento a buscar.
        :return: Entidad Event o None.
        """
        return self.repository.get_by_id(event_id)