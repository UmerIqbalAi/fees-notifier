"""FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.api import auth, payments
from src import database

app = FastAPI(title="Gym WhatsApp Receipt API", version="1.0.0")

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database on startup
@app.on_event("startup")
def startup():
    database.init_db()

# Include routers
app.include_router(auth.router, tags=["Authentication"])
app.include_router(payments.router, tags=["Payments"])

@app.get("/")
def root():
    return {"message": "Gym WhatsApp Receipt API"}

# Serve frontend static files
app.mount(
    "/",
    StaticFiles(directory="../frontend/src/pages", html=True),
    name="frontend"
)
