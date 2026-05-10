"""
Data models for AgriDrop
"""
from datetime import datetime
from typing import Optional

class Field:
    """Represents a farm field"""
    def __init__(self, field_id: str, name: str, latitude: float, longitude: float, area_hectares: float):
        self.field_id = field_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.area_hectares = area_hectares
        self.created_at = datetime.now()
        self.crop_type = "coffee"  # or "durian"
        
class WeatherData:
    """Current weather data"""
    def __init__(self, temperature: float, humidity: float, wind_speed: float, 
                 precipitation: float, solar_radiation: Optional[float] = None):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.precipitation = precipitation
        self.solar_radiation = solar_radiation or 0
        self.timestamp = datetime.now()

class IrrigationSchedule:
    """Irrigation schedule for a field"""
    def __init__(self, field_id: str, water_needed_liters: float, 
                 scheduled_time: str, confidence: float):
        self.field_id = field_id
        self.water_needed_liters = water_needed_liters
        self.scheduled_time = scheduled_time
        self.confidence = confidence
        self.status = "pending"  # pending, active, completed
        self.created_at = datetime.now()

class SatelliteData:
    """Satellite data indices"""
    def __init__(self, ndvi: float, ndwi: float, field_id: str):
        self.ndvi = ndvi  # Vegetation index
        self.ndwi = ndwi  # Water index
        self.field_id = field_id
        self.timestamp = datetime.now()
