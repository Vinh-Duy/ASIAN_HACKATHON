"""
Weather Service - Calls OpenWeather API for real-time data
"""
import os
import httpx
from datetime import datetime
from typing import Dict, Any
import asyncio

class WeatherService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5"
        
    async def get_current_weather(self, latitude: float, longitude: float) -> Dict[str, Any]:
        """
        Get current weather data for a location
        Returns: temperature, humidity, wind_speed, cloud_coverage, etc.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/weather",
                    params={
                        "lat": latitude,
                        "lon": longitude,
                        "appid": self.api_key,
                        "units": "metric"
                    }
                )
                response.raise_for_status()
                data = response.json()
                
                return {
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"],
                    "precipitation": data.get("rain", {}).get("1h", 0),
                    "clouds": data["clouds"]["all"],  # Cloud coverage %
                    "description": data["weather"][0]["description"],
                    "timestamp": datetime.now().isoformat()
                }
        except Exception as e:
            print(f"Error fetching weather: {e}")
            return self._get_mock_weather()
    
    async def get_forecast(self, latitude: float, longitude: float, days: int = 7) -> Dict[str, Any]:
        """Get 7-day weather forecast"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/forecast",
                    params={
                        "lat": latitude,
                        "lon": longitude,
                        "appid": self.api_key,
                        "units": "metric",
                        "cnt": 40  # 5 days forecast with 3-hour intervals
                    }
                )
                response.raise_for_status()
                data = response.json()
                
                forecast_data = []
                for item in data["list"][:40]:  # Get 5-day data
                    forecast_data.append({
                        "datetime": item["dt_txt"],
                        "temp": item["main"]["temp"],
                        "humidity": item["main"]["humidity"],
                        "wind_speed": item["wind"]["speed"],
                        "precipitation_prob": item.get("pop", 0),
                        "precipitation": item.get("rain", {}).get("3h", 0)
                    })
                
                return {"forecast": forecast_data}
        except Exception as e:
            print(f"Error fetching forecast: {e}")
            return {"forecast": []}
    
    def _get_mock_weather(self) -> Dict[str, Any]:
        """Return mock weather data for demo purposes"""
        return {
            "temperature": 32.5,
            "humidity": 65,
            "wind_speed": 2.3,
            "precipitation": 0,
            "clouds": 20,
            "description": "clear sky",
            "timestamp": datetime.now().isoformat()
        }
