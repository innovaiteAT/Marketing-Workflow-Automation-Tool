# Marketing Workflow Automation Tool

Internal marketing assistant for non-technical teams.

This project is being built in phases. The current goal is to establish a reliable frontend/backend connection before adding real product features.

## Project Purpose

The tool is intended to help a marketing team:

- Brainstorm campaign ideas
- Draft social media captions
- Generate creative assets

The product direction emphasizes:

- Simplicity for non-technical users
- Separate frontend and backend services during development
- Fast iteration with incremental feature releases

## Current Phase

Phase 1 (in progress): Foundation and connectivity

- Backend is running with FastAPI
- Frontend is scaffolded with React + Vite + TypeScript
- Frontend can call backend endpoint `GET /api/items`
- Frontend and backend run as separate services in development, connected through the Vite proxy

## Tech Stack

### Frontend

- React 19
- Vite
- TypeScript
- Tailwind CSS
- React Router DOM (installed for upcoming routing)
- Lucide React (installed for iconography)

### Backend

- Python 3.10+
- FastAPI
- Uvicorn

## Project Structure

```text
Marketing-Workflow-Automation-Tool/
├── backend/
│   ├── .venv/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
├── LICENSE
└── README.md
```

## Local Development Setup

### Prerequisites

- Python 3.10 or newer
- Node.js 18+ and npm

### 1) Backend Setup

From the project root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run backend:

```powershell
uvicorn main:app --reload --port 8000
```

Backend URL: `http://localhost:8000`

Health check endpoint:

- `GET http://localhost:8000/api/ping`

Expected response:

```json
{"message": "Backend is alive!"}
```

Example data endpoint:

- `GET http://localhost:8000/api/items`

Expected response:

```json
[{"id": 1, "name": "Item One"}]
```

### 2) Frontend Setup

Open a new terminal from the project root:

```powershell
cd frontend
npm install
```

Run frontend dev server:

```powershell
npm run dev
```

Frontend URL: `http://localhost:5173`

### 3) Run Both Services Together

Start the backend in one terminal:

```powershell
cd backend
uvicorn main:app --reload --port 8000
```

Start the frontend in a second terminal:

```powershell
cd frontend
npm run dev
```

Open:

- `http://localhost:5173`

In this setup, Vite proxies `/api` requests to FastAPI on `http://localhost:8000`.

## Frontend-Backend Connection

The frontend test button in `frontend/src/App.jsx` calls:

- `/api/items`

In development, Vite proxies `/api` to FastAPI.
In development, the React app runs on Vite and `/api` calls are proxied to FastAPI.

## Useful Commands

### Backend

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --port 8000
```

### Frontend

```powershell
cd frontend
npm run dev
npm run build
npm run preview
npm run lint
```

## Next Steps (Recommended)

1. Keep Phase 1 stable and verify ping works every run.
2. Add base app layout and initial routes with React Router.
3. Add first real marketing workflow endpoint(s) in FastAPI.
4. Add simple authentication and role boundaries for internal team usage.
5. Add a small set of reusable marketing workflow endpoints.

## Notes

- This repository is currently optimized for local development.
- Production deployment and environment configuration will be added in a later phase.
