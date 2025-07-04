import React, { useState, useEffect } from 'react';
import { fetchEvents, deleteEvent } from '../api';
import { useNavigate } from 'react-router-dom';
import EventFilter from './EventFilter';
import {
    Container,
    List,
    ListItem,
    ListItemText,
    IconButton,
    Typography,
    Box
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';

export default function EventList(props) {
    const [events, setEvents] = useState([]);
    const [filterDate, setFilterDate] = useState('');

    useEffect(() => { load(); }, []);

    useEffect(() => {
        if (filterDate) {
            load(filterDate);
        } else {
            load();
        }
    }, [filterDate])
    const navigate = useNavigate();

    async function load(filteredDate) {
        try {
            console.log(filteredDate);
            const data = await fetchEvents(filteredDate);
            setEvents(data);
        } catch (err) {
            console.error(err);
        }
    }

    async function handleDelete(id) {
        try {
            await deleteEvent(id);
            load();
        } catch (err) {
            console.error(err);
        }
    }

    return (
        <Container style={{
            width: "100%",
            display: "flex",
            flexWrap: "wrap",
            maxWidth: 'none',
        }}>
            <Typography style={{ width: "100%", display: "block" }} variant="h4" gutterBottom>Eventos</Typography>
            <div style={{
                width: "15%",
                display: "flex",
                flexWrap: "wrap",
                paddingTop: "8px",
                paddingBottom: "8px",
                paddingRight: "48px",
                borderRight: "1px solid silver"
            }}>

                <EventFilter style={{ width: "100%" }} value={filterDate} onChange={setFilterDate} />
            </div>
            <div style={{
                width: "85%"
            }}>

                {events.length === 0
                    ? <Typography style={{ width: "100%", display: "flex", justifyContent: "center" }} variant="body1">No hay eventos.</Typography>
                    : (
                        <List>
                            {events.map(e => (
                                <ListItem
                                    key={e.id}
                                    style={{
                                        cursor: "pointer"
                                    }}
                                    onClick={() => {
                                        navigate('/' + e.id);
                                    }}
                                    secondaryAction={
                                        <IconButton edge="end" onClick={() => handleDelete(e.id)}>
                                            <DeleteIcon />
                                        </IconButton>
                                    }

                                >
                                    <ListItemText
                                        primary={e.name}
                                        secondary={`${e.eventDate} — ${e.location}`}
                                    />
                                </ListItem>
                            ))}
                        </List>
                    )
                }
            </div>

        </Container>
    );
}