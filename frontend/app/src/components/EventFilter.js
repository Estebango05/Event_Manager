import React from 'react';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';

export default function EventFilter({ value, onChange }) {
  return (
    <Box style={{ width: "100%" }}>
      <TextField
        label="Filtrar por Fecha"
        type="date"
        value={value || Date.now()}
        style={{ width: "100%" }}
        onChange={e => onChange(e.target.value)}
        InputLabelProps={{ shrink: true }}
      />
    </Box>
  );
}
