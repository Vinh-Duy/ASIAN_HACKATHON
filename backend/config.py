import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    # API Keys
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./agridrop.db")
    
    # App Settings
    DEBUG = os.getenv("DEBUG", "False") == "True"
    PORT = int(os.getenv("PORT", 8000))
    
    # CORS
    CORS_ORIGINS = ["http://localhost:5173", "http://localhost:3000", "*"]
