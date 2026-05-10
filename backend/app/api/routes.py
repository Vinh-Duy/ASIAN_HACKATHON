"""
API Routes for AgriDrop
"""
from fastapi import APIRouter, HTTPException, Query
from typing import List
import uuid

from app.schemas import (
    FieldCreate, FieldResponse, WeatherDataResponse, 
    IrrigationScheduleResponse, AnalysisResultResponse,
    IrrigationCommandRequest
)
from app.services.weather_service import WeatherService
from app.services.ai_service import AIService
from app.services.irrigation_service import IrrigationService
from app.services.satellite_service import SatelliteService

router = APIRouter(prefix="/api/v1", tags=["agridrop"])

# Service instances
weather_service = WeatherService()
ai_service = AIService()
irrigation_service = IrrigationService()
satellite_service = SatelliteService()

# In-memory field storage (replace with database in production)
fields_db = {}

@router.post("/fields", response_model=FieldResponse)
async def create_field(field_data: FieldCreate):
    """Create a new field"""
    field_id = str(uuid.uuid4())
    
    field = {
        "field_id": field_id,
        "name": field_data.name,
        "latitude": field_data.latitude,
        "longitude": field_data.longitude,
        "area_hectares": field_data.area_hectares,
        "crop_type": field_data.crop_type,
        "created_at": "2026-05-09T00:00:00"
    }
    
    fields_db[field_id] = field
    return field

@router.get("/fields/{field_id}", response_model=FieldResponse)
async def get_field(field_id: str):
    """Get field details"""
    if field_id not in fields_db:
        raise HTTPException(status_code=404, detail="Field not found")
    return fields_db[field_id]

@router.get("/fields")
async def list_fields():
    """List all fields"""
    return list(fields_db.values())

@router.get("/weather", response_model=WeatherDataResponse)
async def get_current_weather(latitude: float, longitude: float):
    """Get current weather for a location"""
    weather = await weather_service.get_current_weather(latitude, longitude)
    weather["location"] = f"{latitude:.2f}, {longitude:.2f}"
    return weather

@router.get("/weather/forecast")
async def get_weather_forecast(latitude: float, longitude: float, days: int = Query(7)):
    """Get weather forecast for a location"""
    forecast = await weather_service.get_forecast(latitude, longitude, days)
    return forecast

@router.get("/analysis/{field_id}", response_model=AnalysisResultResponse)
async def analyze_field(field_id: str):
    """Get comprehensive field analysis"""
    if field_id not in fields_db:
        raise HTTPException(status_code=404, detail="Field not found")
    
    field = fields_db[field_id]
    
    # Get current weather
    weather = await weather_service.get_current_weather(field["latitude"], field["longitude"])
    
    # Get satellite data
    satellite = await satellite_service.get_satellite_indices(field["latitude"], field["longitude"])
    
    # Estimate soil moisture from satellite
    soil_moisture = ai_service.estimate_soil_moisture_from_satellite(
        satellite["ndvi"], satellite["ndwi"]
    )
    
    # Perform analysis
    analysis = ai_service.analyze_field(
        weather=weather,
        soil_moisture=soil_moisture,
        ndvi=satellite["ndvi"],
        ndwi=satellite["ndwi"],
        crop_type=field["crop_type"]
    )
    
    return {
        "field_id": field_id,
        "soil_moisture": analysis["soil_moisture"],
        "evapotranspiration": analysis["et0"],
        "water_deficit": analysis["water_deficit"],
        "recommendation": analysis["recommendation"],
        "confidence": analysis["confidence"],
        "timestamp": analysis["timestamp"]
    }

@router.get("/satellite/indices")
async def get_satellite_indices(latitude: float, longitude: float):
    """Get NDVI and NDWI from satellite"""
    indices = await satellite_service.get_satellite_indices(latitude, longitude)
    return indices

@router.get("/satellite/water-stress")
async def get_water_stress(latitude: float, longitude: float):
    """Get water stress map"""
    stress = await satellite_service.get_water_stress_map(latitude, longitude)
    return stress

@router.get("/satellite/temporal-trend")
async def get_temporal_trend(latitude: float, longitude: float, days: int = Query(30)):
    """Get temporal trends in satellite data"""
    trend = await satellite_service.compare_temporal_data(latitude, longitude, days)
    return trend

@router.post("/irrigation/schedule")
async def schedule_irrigation(field_id: str, water_needed: float, scheduled_time: str):
    """Create irrigation schedule"""
    if field_id not in fields_db:
        raise HTTPException(status_code=404, detail="Field not found")
    
    schedule_id = irrigation_service.create_schedule(
        field_id=field_id,
        water_needed=water_needed,
        scheduled_time=scheduled_time,
        confidence=0.85
    )
    
    return {
        "schedule_id": schedule_id,
        "field_id": field_id,
        "water_needed_liters": water_needed,
        "scheduled_time": scheduled_time,
        "status": "pending"
    }

@router.post("/irrigation/trigger")
async def trigger_irrigation(command: IrrigationCommandRequest):
    """Trigger or stop irrigation"""
    if command.action == "start":
        result = irrigation_service.trigger_irrigation(
            field_id=command.field_id,
            duration_minutes=command.duration_minutes or 30
        )
    elif command.action == "stop":
        result = irrigation_service.stop_irrigation(field_id=command.field_id)
    else:
        raise HTTPException(status_code=400, detail="Invalid action")
    
    return result

@router.get("/irrigation/schedules")
async def get_schedules(field_id: str = None):
    """Get active irrigation schedules"""
    schedules = irrigation_service.get_active_schedules(field_id)
    return schedules

@router.get("/irrigation/history")
async def get_irrigation_history(field_id: str = None, days: int = Query(30)):
    """Get irrigation history"""
    history = irrigation_service.get_irrigation_history(field_id, days)
    return history

@router.get("/irrigation/savings")
async def get_water_savings(field_id: str):
    """Calculate water savings"""
    if field_id not in fields_db:
        raise HTTPException(status_code=404, detail="Field not found")
    
    savings = irrigation_service.calculate_water_savings(field_id)
    return savings

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "AgriDrop API"}
