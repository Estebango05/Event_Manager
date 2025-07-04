from app.domain.repository import EventRepository


class DeleteEvent:
    """
    Caso de uso: eliminar un evento.
    """

    def __init__(self, repository: EventRepository):
        self.repository = repository

    def execute(self, event_id: int) -> None:
        """
        :param event_id: ID del evento a eliminar.
        """
        self.repository.delete(event_id)