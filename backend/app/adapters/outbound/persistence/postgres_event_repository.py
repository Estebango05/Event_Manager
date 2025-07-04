import os
from typing import List, Optional
from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, String, Date,
    insert, select, update as sa_update, delete as sa_delete
)
from app.config import settings

# Carga URL de conexión
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Definición de la tabla
events_table = Table(
    "events", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("eventDate", Date, nullable=False),
    Column("description", String, nullable=False),
    Column("location", String, nullable=False),
)
metadata.create_all(engine)


def insert_event(name: str, eventDate, description: str, location: str) -> dict:
    """Inserta un nuevo evento y retorna el registro completo con COMMIT."""
    with engine.begin() as conn:
        result = conn.execute(
            insert(events_table)
            .values(name=name, eventDate=eventDate, description=description, location=location)
        )
        pk = result.inserted_primary_key[0]
        row = conn.execute(
            select(events_table).where(events_table.c.id == pk)
        ).first()
    return dict(row._mapping)


def fetch_event_by_id(event_id: int) -> Optional[dict]:
    """Recupera un evento por ID."""
    # lectura; no necesita begin()
    with engine.connect() as conn:
        row = conn.execute(
            select(events_table).where(events_table.c.id == event_id)
        ).first()
    return dict(row._mapping) if row else None


def fetch_all_events(filteredDate) -> List[dict]:
    """Recupera todos los eventos."""
    with engine.connect() as conn:
        stmt = select(events_table)
        if filteredDate is not None:
            stmt = stmt.where(events_table.c.eventDate == filteredDate)
        rows = conn.execute(stmt).fetchall()
    return [dict(r._mapping) for r in rows]

def update_event_in_db(event_id: int, name: str, eventDate, description: str, location: str) -> dict:
    """Actualiza un evento y retorna el registro actualizado con COMMIT."""
    with engine.begin() as conn:
        conn.execute(
            sa_update(events_table)
            .where(events_table.c.id == event_id)
            .values(name=name, eventDate=eventDate, description=description, location=location)
        )
        row = conn.execute(
            select(events_table).where(events_table.c.id == event_id)
        ).first()
    return dict(row._mapping)


def delete_event_by_id(event_id: int) -> None:
    """Elimina un evento por ID con COMMIT."""
    with engine.begin() as conn:
        conn.execute(
            sa_delete(events_table).where(events_table.c.id == event_id)
        )
