"""
Satellite Service - Integrates with Google Earth Engine and Copernicus APIs
For demo: uses mock satellite data
"""
import random
from typing import Dict, Any
from datetime import datetime

class SatelliteService:
    """
    Simulates satellite data retrieval
    In production, would integrate with Google Earth Engine API
    """
    
    def __init__(self):
        self.cache = {}
    
    async def get_satellite_indices(self, latitude: float, longitude: float) -> Dict[str, float]:
        """
        Get NDVI and NDWI indices from satellite imagery
        NDVI: Vegetation health (0-1, higher = healthier)
        NDWI: Water content (0-1, higher = more water)
        """
        
        # In real scenario, would call Google Earth Engine API
        # For now, generate realistic mock data based on location
        
        # Simulate some variations based on location
        location_key = f"{latitude:.2f}_{longitude:.2f}"
        
        if location_key not in self.cache:
            # Mock satellite data - would be from actual satellite in production
            self.cache[location_key] = {
                "ndvi": round(random.uniform(0.45, 0.75), 3),  # Typical for agriculture
                "ndwi": round(random.uniform(0.15, 0.55), 3),  # Water content
                "timestamp": datetime.now().isoformat()
            }
        
        return self.cache[location_key]
    
    async def get_vegetation_map(self, latitude: float, longitude: float, 
                                 radius_km: float = 5) -> Dict[str, Any]:
        """
        Get vegetation map for a region (mock visualization data)
        """
        # Generate grid of NDVI values for visualization
        grid_size = 10
        ndvi_grid = []
        
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                # Create spatial variation
                ndvi = 0.5 + 0.2 * (i / grid_size) - 0.1 * (j / grid_size)
                ndvi = max(0, min(1, ndvi))
                row.append(round(ndvi, 2))
            ndvi_grid.append(row)
        
        return {
            "center": {"latitude": latitude, "longitude": longitude},
            "radius_km": radius_km,
            "ndvi_grid": ndvi_grid,
            "resolution_m": 10,  # Sentinel-2 resolution
            "timestamp": datetime.now().isoformat()
        }
    
    async def get_water_stress_map(self, latitude: float, longitude: float) -> Dict[str, Any]:
        """
        Generate water stress map combining NDVI and NDWI
        Red = high stress, Yellow = moderate, Green = low stress
        """
        indices = await self.get_satellite_indices(latitude, longitude)
        
        # Water stress index
        stress = 1 - (indices["ndvi"] + indices["ndwi"]) / 2
        
        if stress > 0.7:
            stress_level = "🔴 CRITICAL"
            color = "red"
        elif stress > 0.5:
            stress_level = "🟠 HIGH"
            color = "orange"
        elif stress > 0.3:
            stress_level = "🟡 MODERATE"
            color = "yellow"
        else:
            stress_level = "🟢 NORMAL"
            color = "green"
        
        return {
            "stress_index": round(stress, 3),
            "stress_level": stress_level,
            "color": color,
            "ndvi": indices["ndvi"],
            "ndwi": indices["ndwi"],
            "timestamp": indices["timestamp"]
        }
    
    async def compare_temporal_data(self, latitude: float, longitude: float, 
                                    days_back: int = 30) -> Dict[str, Any]:
        """
        Compare satellite data over time
        Shows trends in vegetation and water content
        """
        # Mock temporal data
        dates = []
        ndvi_values = []
        ndwi_values = []
        
        for day in range(days_back, 0, -1):
            # Generate trend data
            trend = 1 - (day / days_back) * 0.3
            ndvi = 0.6 * trend + random.uniform(-0.05, 0.05)
            ndwi = 0.35 * trend + random.uniform(-0.05, 0.05)
            
            dates.append(f"2026-05-{max(1, 9-days_back+day):02d}")
            ndvi_values.append(round(max(0.2, ndvi), 2))
            ndwi_values.append(round(max(0.1, ndwi), 2))
        
        return {
            "dates": dates,
            "ndvi_trend": ndvi_values,
            "ndwi_trend": ndwi_values,
            "period_days": days_back,
            "trend": "declining" if ndvi_values[-1] < ndvi_values[0] else "improving"
        }
