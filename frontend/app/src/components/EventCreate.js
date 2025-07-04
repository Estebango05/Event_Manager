import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createEvent } from '../api';
import {
  Container,
  TextField,
  Button,
  Typography,
  Box,
  Snackbar, Alert
} from '@mui/material';

export default function EventCreate() {
  const [form, setForm] = useState({
    name: '',
    eventDate: '',
    description: '',
    location: ''
  });
  const [alert, setAlert] = useState({ open: false, message: '', severity: 'success' });
  const navigate = useNavigate();

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  const handleCloseAlert = (e, reason) => {
    if (reason === 'clickaway') return;
    setAlert(a => ({ ...a, open:false }));
  };

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await createEvent(form);
      setAlert({ open: true, message: '¡Evento creado con éxito!', severity: 'success' });
      setTimeout(() => navigate('/'), 500);
    } catch (err) {
      setAlert({ open:true, message:'Error al crear el evento', severity:'error' });
      console.error(err);
    }
  }

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" gutterBottom>Crear Evento</Typography>
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
          Crear Evento
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