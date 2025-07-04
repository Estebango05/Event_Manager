# Event Management System

## Descripción

Proyecto de sistema de gestión de eventos con arquitectura fullstack:
- **Backend (BE):** API REST en Python usando **FastAPI**
- **Frontend (FE):** Aplicación web en **React.js** con **Material-UI**.

El sistema permite crear, listar, filtrar por fecha y eliminar eventos. Incluye documentación automática de la API con Swagger.

---

## Tecnologías

- **Backend:**
  - Python 3.9+
  - FastAPI
  - Pydantic (modelos y DTOs)
  - SQLAlchemy (o cliente de PostgreSQL)
  - PostgreSQL
  - Arquitectura hexagonal (dominio, puertos/adaptadores, infraestructura)
  - Docker + Docker Compose
  - Uvicorn

- **Frontend:**
  - React.js (v17+)
  - Material-UI (MUI)
  - fetch API
  - Docker

- **DevOps & Despliegue:**
  - Azure DevOps (CI/CD)
  - Azure App Service / Azure Container Instances
  - SwaggerHub (documentación externa)
  - GitHub

---

## Estructura del proyecto

```
├── backend/
│   ├── app/
│   │   ├── core/             # Lógica de dominio y casos de uso
│   │   ├── domain/           # Entidades y reglas de negocio
│   │   ├── adapters/         # Implementaciones de puertos (DB, email, etc.)
│   │   ├── infrastructure/   # Configuración de base de datos, CORS, logging
│   │   ├── dtos/             # Objetos de transferencia de datos (DTOs)
│   │   ├── api/              # Rutas y controladores de FastAPI
│   │   └── main.py           # Punto de entrada de la aplicación
│   ├── Dockerfile
│   ├── docker-compose.yml    # Servicio: postgres
│   ├── requirements.txt
│
├── frontend/
│   |── app/
│     ├── public/
│     ├── src/
│     │   ├── components/       # Componentes reutilizables (formularios, botones, alerts)
│     │   ├── pages/            # Vistas: lista de eventos, crear, editar, etc.
│     │   ├── App.js
│     │   ├── api.js
│     │   └── index.js
│     ├── package.json
│
├── .gitignore               # Ignora __pycache__, node_modules, .env, etc.
└── README.md
```

---

## Requisitos previos

- **Instalaciones locales:**
  - Node.js & npm/yarn
  - Python 3.9+
  - Docker & Docker Compose (opcional)
  - Git

---

## Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Estebango05/Event_Manager
cd Event_Manager
```

### 2. Backend

1. Copiar variables de entorno:
   ```bash
   cd backend
   cp .env.example .env
   # Edita .env y configura DATABASE_URL.
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar localmente:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

_Alternativa Docker:_
```bash
docker-compose up --build
```

### 3. Frontend

1. Copiar entorno:
   ```bash
   cd frontend
   cp .env.local.example .env.local
   # Edita .env.local para apuntar al backend (p.ej. REACT_APP_API_URL=http://localhost:8000)
   ```
2. Instalar dependencias:
   ```bash
   npm install
   ```
3. Ejecutar:
   ```bash
   npm start
   ```

---

## Documentación de la API

- Una vez el backend esté corriendo, accede a:
  - **Swagger UI:** https://app.swaggerhub.com/apis/independiente-f0f-c89/EventManager/1.0.0#/

---

## Docker

El `docker-compose.yml` define:
- `postgres`: base de datos PostgreSQL

```bash
docker-compose up --build
```