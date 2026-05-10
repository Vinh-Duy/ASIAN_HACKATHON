"""
Pydantic schemas for API requests/responses
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FieldCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    area_hectares: float
    crop_type: str = "coffee"

class FieldResponse(BaseModel):
    field_id: str
    name: str
    latitude: float
    longitude: float
    area_hectares: float
    crop_type: str
    created_at: datetime

class WeatherDataResponse(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    precipitation: float
    solar_radiation: Optional[float] = None
    timestamp: datetime
    location: str

class IrrigationScheduleResponse(BaseModel):
    field_id: str
    water_needed_liters: float
    scheduled_time: str
    confidence: float
    status: str
    created_at: datetime
    
class IrrigationCommandRequest(BaseModel):
    field_id: str
    action: str  # "start", "stop"
    duration_minutes: Optional[int] = None

class AnalysisResultResponse(BaseModel):
    field_id: str
    soil_moisture: float
    evapotranspiration: float
    water_deficit: float
    recommendation: str
    confidence: float
    timestamp: datetime
