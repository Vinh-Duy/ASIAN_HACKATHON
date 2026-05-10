"""
FastAPI main application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager

from config import Config
from app.api.routes import router

# Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🌾 AgriDrop Server Starting...")
    yield
    # Shutdown
    print("🌾 AgriDrop Server Shutting Down...")

# Create FastAPI app
app = FastAPI(
    title="AgriDrop API",
    description="Smart Precision Irrigation System using Satellite Data & AI",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZIP compression
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Include routes
app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to AgriDrop - Smart Irrigation System",
        "docs": "/docs",
        "status": "running"
    }

@app.get("/api/v1/status")
async def api_status():
    """API status"""
    return {
        "status": "operational",
        "service": "AgriDrop Smart Irrigation API",
        "version": "1.0.0",
        "features": [
            "Real-time weather integration",
            "Satellite-based crop monitoring",
            "AI-powered water requirement prediction",
            "Precision irrigation scheduling"
        ]
    }
