const API_URL = 'http://eventmanagerbeapi.southcentralus.azurecontainer.io:8000';

export async function fetchEvents(filteredDate) {
  const res = await fetch(`${API_URL}/events${filteredDate ? "?filteredDate="+filteredDate: ""}`);
  if (!res.ok) throw new Error('Error al cargar eventos');
  return res.json();
}


export async function getEvent(id) {
  const res = await fetch(`${API_URL}/events/${id}`);
  if (!res.ok) throw new Error('Error al cargar eventos');
  return res.json();
}
export async function createEvent(data) {
  const res = await fetch(`${API_URL}/events`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error('Error al crear evento');
  return res.json();
}

export async function updateEvent(id, data) {
  const res = await fetch(`${API_URL}/events/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error('Error al crear evento');
  return res.json();
}

export async function deleteEvent(id) {
  const res = await fetch(`${API_URL}/events/${id}`, { method: 'DELETE' });
  if (!res.ok) throw new Error('Error al eliminar evento');
  return;
}