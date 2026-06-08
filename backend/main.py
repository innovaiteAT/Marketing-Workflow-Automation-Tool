from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-marketing-workflow-automat.vercel.app",
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve a simple status response while the frontend runs separately on Vite.
@app.get("/")
async def root():
    return {
        "message": "FastAPI backend is running. Start the Vite dev server separately for the frontend.",
    }

# Health check endpoint used by the frontend and docs to test connectivity.
@app.get("/ping")
async def ping():
    return {"status": "ok", "message": "Backend is alive!"}


# Data endpoint used by the React app through the Vite proxy.
@app.get("/api/items")
async def get_items():
    return [
        {"id": 1, "name": "Item One"},
        {"id": 2, "name": "Item Two"},
        {"id": 3, "name": "Item Three"},
    ]


# Keep the simpler ping route available for compatibility with the current build.
@app.get("/api/ping")
async def api_ping():
    return {"status": "ok", "message": "Backend is alive!"}