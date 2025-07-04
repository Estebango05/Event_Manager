from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from datetime import date
from typing import List
from app.schemas.event_schema import EventCreate, EventRead, EventUpdate
from app.domain.repository import EventRepository
from app.application import CreateEvent, ListEvents, GetEvent, UpdateEvent, DeleteEvent

router = APIRouter(prefix="/events", tags=["events"])

# Instanciamos repositorio y casos de uso
repo = EventRepository()
create_uc = CreateEvent(repo)
list_uc = ListEvents(repo)
get_uc = GetEvent(repo)
update_uc = UpdateEvent(repo)
delete_uc = DeleteEvent(repo)

@router.post("/", response_model=EventRead)
def create_event(data: EventCreate) -> EventRead:
    """Crea un nuevo evento."""
    event = create_uc.execute(data)
    return EventRead(**event.__dict__)

@router.get("/", response_model=List[EventRead])
def list_events(
    filteredDate: Optional[date] = Query(
        None,
        description="Filtra eventos por fecha en formato YYYY-MM-DD"
    )
) -> List[EventRead]:
    """
    Lista todos los eventos. Si se pasa 'fecha', retorna solo los eventos de esa fecha.
    """
    events = list_uc.execute(filteredDate)
    return [EventRead(**e.__dict__) for e in events]

@router.get("/{event_id}", response_model=EventRead)
def get_event(event_id: int) -> EventRead:
    """Obtiene un evento por su ID."""
    event = get_uc.execute(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return EventRead(**event.__dict__)

@router.put("/{event_id}", response_model=EventRead)
def update_event(event_id: int, data: EventUpdate) -> EventRead:
    """Actualiza un evento existente."""
    try:
        event = update_uc.execute(event_id, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return EventRead(**event.__dict__)

@router.delete("/{event_id}", status_code=204)
def delete_event(event_id: int):
    """Elimina un evento."""
    try:
        delete_uc.execute(event_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Evento no encontrado")