// src/App.js
import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import EventList from './components/EventList';
import EventCreate from './components/EventCreate';
import EventUpdate from './components/EventUpdate';

export default function App() {
  return (
    <BrowserRouter>
      <nav style={{ padding: '1rem', background: '#f5f5f5' }}>
        <Link to="/" style={{ marginRight: '1rem' }}>Eventos</Link>
        <Link to="/create">Crear evento</Link>
      </nav>
      <Routes>
        <Route path="/" element={<EventList />} />
        <Route path="/create" element={<EventCreate />} />
        <Route path="/:id" element={<EventUpdate />} />
      </Routes>
    </BrowserRouter>
  );
}
