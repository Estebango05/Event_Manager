from typing import List
from app.domain.entities import Event
from app.domain.repository import EventRepository


class ListEvents:
    """
    Caso de uso: listar todos los eventos.
    """

    def __init__(self, repository: EventRepository):
        self.repository = repository

    def execute(self, filteredDate) -> List[Event]:
        """
        :return: Lista de entidades Event.
        """
        return self.repository.list(filteredDate)