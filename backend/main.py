from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

# Create the FastAPI application instance used by Uvicorn.
app = FastAPI()

# Resolve the frontend folder and main HTML file location.
FRONTEND_DIR = Path(__file__).resolve().parents[1] / "frontend"
INDEX_FILE = FRONTEND_DIR / "index.html"

# Serve the frontend page when a user visits the site root.
@app.get("/")
async def root():
    return FileResponse(INDEX_FILE)

# Ping endpoint used by the frontend button to test connectivity.
@app.get("/ping")
async def ping():
    return {"status": "ok", "message": "Backend is alive!"}