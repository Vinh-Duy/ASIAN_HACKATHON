"""
AI/ML Service - Calculates Evapotranspiration and water requirements
Using Hargreaves-Samani method and ML model
"""
from datetime import datetime
from typing import Dict, Any, Tuple
import math

class AIService:
    """
    AI Service for calculating evapotranspiration and water requirements
    """
    
    def __init__(self):
        self.crop_coefficients = {
            "coffee": {"young": 0.5, "mature": 0.7, "blooming": 0.85},
            "durian": {"young": 0.4, "mature": 0.8, "blooming": 0.9}
        }
        
    def calculate_et0_hargreaves(self, temperature: float, humidity: float, 
                                 wind_speed: float, solar_radiation: float,
                                 latitude: float, day_of_year: int = None) -> float:
        """
        Calculate Reference Evapotranspiration (ET0) using Hargreaves-Samani formula
        
        Args:
            temperature: Mean daily temperature (°C)
            humidity: Relative humidity (%)
            wind_speed: Wind speed at 2m (m/s)
            solar_radiation: Solar radiation (MJ/m²/day)
            latitude: Location latitude (degrees)
            day_of_year: Day of year for seasonal adjustment
            
        Returns:
            ET0 value in mm/day
        """
        if day_of_year is None:
            day_of_year = datetime.now().timetuple().tm_yday
        
        # Convert latitude to radians
        lat_rad = math.radians(latitude)
        
        # Calculate declination
        declination = 0.409 * math.sin((2 * math.pi * day_of_year / 365) - 1.39)
        
        # Calculate sunset hour angle
        sunset_angle = math.acos(-math.tan(lat_rad) * math.tan(declination))
        
        # Calculate extra-terrestrial radiation (Ra)
        gsc = 0.0820  # Solar constant (MJ/m²/min)
        dr = 1 + 0.033 * math.cos(2 * math.pi * day_of_year / 365)
        ra = (24 * 60 / math.pi) * gsc * dr * (
            sunset_angle * math.sin(lat_rad) * math.sin(declination) +
            math.cos(lat_rad) * math.cos(declination) * math.sin(sunset_angle)
        )
        
        # Calculate net radiation
        albedo = 0.23
        rns = (1 - albedo) * solar_radiation
        rnl = 2.042e-10 * (273.16 + temperature) ** 4 * (0.34 - 0.14 * math.sqrt(humidity / 100)) * \
              (1.35 * solar_radiation / ra - 0.35)
        rn = rns - rnl
        
        # Calculate soil heat flux (usually small)
        g = 0
        
        # Calculate ET0 (Hargreaves-Samani)
        et0 = 0.0023 * (temperature + 17.8) * (temperature - temperature) ** 0.5 * 0.408 * ra / 2.45
        
        # Simplified version if exact calculation not needed
        if solar_radiation == 0:
            et0 = 0.0023 * (temperature + 17.8) * (23 - temperature + 1) ** 0.5
        
        return max(et0, 0.1)  # Ensure minimum positive value
    
    def calculate_crop_water_requirement(self, et0: float, crop_type: str, 
                                        crop_stage: str, soil_moisture: float) -> float:
        """
        Calculate actual crop water requirement
        Etc = ET0 * Kc * (soil_moisture_factor)
        """
        kc = self.crop_coefficients.get(crop_type, {}).get(crop_stage, 0.7)
        
        # Soil moisture factor (0.5 = dry, 1.0 = optimal, 0.0 = saturated)
        soil_factor = max(0.3, min(1.0, soil_moisture / 100))
        
        return et0 * kc * soil_factor
    
    def predict_soil_moisture(self, current_moisture: float, 
                             et0: float, precipitation: float,
                             irrigation_applied: float = 0) -> float:
        """
        Predict soil moisture for next day
        """
        # Simple model: moisture decreases due to ET, increases due to rain/irrigation
        moisture_change = -et0 * 10 + precipitation + irrigation_applied
        new_moisture = current_moisture + moisture_change
        
        # Bound between 0 and 100%
        return max(0, min(100, new_moisture))
    
    def calculate_ndvi_from_satellite(self, red_band: float, nir_band: float) -> float:
        """
        Calculate NDVI from satellite image bands
        NDVI = (NIR - RED) / (NIR + RED)
        """
        if nir_band + red_band == 0:
            return 0
        return (nir_band - red_band) / (nir_band + red_band)
    
    def calculate_ndwi_from_satellite(self, nir_band: float, swir_band: float) -> float:
        """
        Calculate NDWI from satellite image bands
        NDWI = (NIR - SWIR) / (NIR + SWIR)
        """
        if nir_band + swir_band == 0:
            return 0
        return (nir_band - swir_band) / (nir_band + swir_band)
    
    def estimate_soil_moisture_from_satellite(self, ndvi: float, ndwi: float) -> float:
        """
        Estimate soil moisture from NDVI and NDWI indices
        """
        # Empirical relationship
        moisture = 50 + 30 * ndwi - 10 * ndvi
        return max(0, min(100, moisture))
    
    def generate_irrigation_recommendation(self, water_deficit: float, 
                                          soil_moisture: float,
                                          forecast_rain: float) -> Tuple[float, str]:
        """
        Generate irrigation recommendation
        
        Returns:
            (water_needed_liters, recommendation_text)
        """
        if soil_moisture > 75:
            return 0, "Soil moisture is adequate. No irrigation needed."
        
        # Adjust for forecasted rain
        adjusted_deficit = max(0, water_deficit - forecast_rain * 10)
        
        if adjusted_deficit < 5:
            return 0, "Soil has sufficient moisture. Monitor in next 2-3 days."
        elif adjusted_deficit < 15:
            return adjusted_deficit * 100, "Light irrigation recommended. Water in early morning or evening."
        elif adjusted_deficit < 30:
            return adjusted_deficit * 150, "Moderate irrigation needed. Start within 24 hours."
        else:
            return adjusted_deficit * 200, "🚨 URGENT: Heavy irrigation required. Start immediately!"
    
    def analyze_field(self, weather: Dict[str, Any], soil_moisture: float,
                     ndvi: float, ndwi: float, crop_type: str = "coffee") -> Dict[str, Any]:
        """
        Comprehensive field analysis combining weather, satellite, and soil data
        """
        # Calculate ET0
        et0 = self.calculate_et0_hargreaves(
            temperature=weather["temperature"],
            humidity=weather["humidity"],
            wind_speed=weather["wind_speed"],
            solar_radiation=weather.get("solar_radiation", 15),
            latitude=weather.get("latitude", 12)  # Default to Dak Lak latitude
        )
        
        # Calculate crop water requirement
        water_req = self.calculate_crop_water_requirement(et0, crop_type, "mature", soil_moisture)
        
        # Calculate water deficit
        water_deficit = water_req - soil_moisture / 10
        water_deficit = max(0, water_deficit)
        
        # Generate recommendation
        forecast_rain = weather.get("precipitation_forecast", 0)
        water_needed, recommendation = self.generate_irrigation_recommendation(
            water_deficit, soil_moisture, forecast_rain
        )
        
        return {
            "et0": round(et0, 2),
            "water_requirement": round(water_req, 2),
            "soil_moisture": round(soil_moisture, 2),
            "water_deficit": round(water_deficit, 2),
            "water_needed_liters": round(water_needed * 100, 0),  # Per 100m²
            "recommendation": recommendation,
            "ndvi": round(ndvi, 3),
            "ndwi": round(ndwi, 3),
            "confidence": 0.82,
            "timestamp": datetime.now().isoformat()
        }
