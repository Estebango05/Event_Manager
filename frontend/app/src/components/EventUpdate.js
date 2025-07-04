import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { updateEvent, getEvent } from '../api';
import { useParams } from 'react-router-dom';
import {
  Container,
  TextField,
  Button,
  Typography,
  Box,
  Snackbar, Alert
} from '@mui/material';

export default function EventUpdate(props) {
  const { id } = useParams();
  const [form, setForm] = useState({
    name: '',
    eventDate: '',
    description: '',
    location: ''
  });
  const [alert, setAlert] = useState({ open: false, message: '', severity: 'success' });
  const navigate = useNavigate();


  const handleCloseAlert = (e, reason) => {
    if (reason === 'clickaway') return;
    setAlert(a => ({ ...a, open: false }));
  };
  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const { id, ...data } = form;
      await updateEvent(id, data);
      setAlert({ open: true, message: '¡Evento actualizado con éxito!', severity: 'success' });
      setTimeout(() => navigate('/'), 500);
    } catch (err) {
      setAlert({ open: true, message: 'Error intentando actualizar el evento', severity: 'error' });
      console.error(err);
    }
  }

  async function getEventById(id) {
    try {
      const data = await getEvent(id);
      setForm(data);
    } catch (err) {
      console.error(err);
    }
  }

  useEffect(() => {
    if (id) {
      getEventById(id);
    }

  }, [id])

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" gutterBottom>Actualizar Evento</Typography>
      <Box component="form" onSubmit={handleSubmit} sx={{ display: 'grid', gap: 2 }}>
        <TextField
          label="Nombre"
          name="name"
          value={form.name}
          onChange={handleChange}
          required
        />
        <TextField
          label="Fecha"
          name="eventDate"
          type="date"
          InputLabelProps={{ shrink: true }}
          value={form.eventDate}
          onChange={handleChange}
          required
        />
        <TextField
          label="Descripción"
          name="description"
          multiline
          rows={4}
          value={form.description}
          onChange={handleChange}
          required
        />
        <TextField
          label="Lugar"
          name="location"
          value={form.location}
          onChange={handleChange}
          required
        />
        <Button variant="contained" type="submit">
          Actualizar Evento
        </Button>
      </Box>
      <Snackbar
        open={alert.open}
        autoHideDuration={4000}
        onClose={handleCloseAlert}
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
      >
        <Alert onClose={handleCloseAlert} severity={alert.severity} sx={{ width: '100%' }}>
          {alert.message}
        </Alert>
      </Snackbar>
    </Container>
  );
}