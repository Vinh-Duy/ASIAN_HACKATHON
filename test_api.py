"""
Test script to demo AgriDrop API
Run this to see the system in action
"""
import asyncio
import httpx
from datetime import datetime

BASE_URL = "http://localhost:8000"

async def test_api():
    """Test AgriDrop API endpoints"""
    print("🌾 AgriDrop API Test")
    print("=" * 60)
    
    async with httpx.AsyncClient() as client:
        # 1. Health check
        print("\n1️⃣ Health Check")
        response = await client.get(f"{BASE_URL}/api/v1/health")
        print(f"   Status: {response.json()['status']}")
        
        # 2. Create a field
        print("\n2️⃣ Creating Field")
        field_data = {
            "name": "Field A - Coffee Farm Dak Lak",
            "latitude": 12.6667,
            "longitude": 108.0333,
            "area_hectares": 5,
            "crop_type": "coffee"
        }
        response = await client.post(f"{BASE_URL}/api/v1/fields", json=field_data)
        field = response.json()
        field_id = field["field_id"]
        print(f"   ✓ Created field: {field['name']}")
        print(f"   Field ID: {field_id}")
        
        # 3. Get weather
        print("\n3️⃣ Fetching Real Weather Data")
        response = await client.get(
            f"{BASE_URL}/api/v1/weather",
            params={"latitude": 12.6667, "longitude": 108.0333}
        )
        weather = response.json()
        print(f"   🌡️  Temperature: {weather['temperature']}°C")
        print(f"   💨 Humidity: {weather['humidity']}%")
        print(f"   💧 Wind Speed: {weather['wind_speed']} m/s")
        print(f"   ☔ Precipitation: {weather['precipitation']} mm")
        
        # 4. Get weather forecast
        print("\n4️⃣ Weather Forecast (7 days)")
        response = await client.get(
            f"{BASE_URL}/api/v1/weather/forecast",
            params={"latitude": 12.6667, "longitude": 108.0333, "days": 7}
        )
        forecast = response.json()
        if forecast["forecast"]:
            for i, item in enumerate(forecast["forecast"][:3]):
                print(f"   Day {i+1}: {item['temp']}°C, Humidity: {item['humidity']}%")
        
        # 5. Get satellite indices
        print("\n5️⃣ Satellite Indices (NDVI, NDWI)")
        response = await client.get(
            f"{BASE_URL}/api/v1/satellite/indices",
            params={"latitude": 12.6667, "longitude": 108.0333}
        )
        satellite = response.json()
        print(f"   🌿 NDVI (Vegetation): {satellite['ndvi']}")
        print(f"   💧 NDWI (Water Index): {satellite['ndwi']}")
        
        # 6. Get water stress map
        print("\n6️⃣ Water Stress Analysis")
        response = await client.get(
            f"{BASE_URL}/api/v1/satellite/water-stress",
            params={"latitude": 12.6667, "longitude": 108.0333}
        )
        stress = response.json()
        print(f"   Stress Level: {stress['stress_level']}")
        print(f"   Stress Index: {stress['stress_index']}")
        
        # 7. Comprehensive field analysis
        print("\n7️⃣ Field Analysis (AI/ML)")
        response = await client.get(f"{BASE_URL}/api/v1/analysis/{field_id}")
        analysis = response.json()
        print(f"   Soil Moisture: {analysis['soil_moisture']}%")
        print(f"   ET0 (Evapotranspiration): {analysis['evapotranspiration']} mm/day")
        print(f"   Water Deficit: {analysis['water_deficit']} mm")
        print(f"   💡 Recommendation: {analysis['recommendation']}")
        print(f"   Confidence: {analysis['confidence']*100:.0f}%")
        
        # 8. Schedule irrigation
        print("\n8️⃣ Scheduling Irrigation")
        response = await client.post(
            f"{BASE_URL}/api/v1/irrigation/schedule",
            params={
                "field_id": field_id,
                "water_needed": 15.5,
                "scheduled_time": "2026-05-09T17:00:00"
            }
        )
        schedule = response.json()
        print(f"   ✓ Scheduled {schedule['water_needed_liters']}L at {schedule['scheduled_time']}")
        
        # 9. Trigger irrigation
        print("\n9️⃣ Triggering Irrigation (Manual)")
        response = await client.post(
            f"{BASE_URL}/api/v1/irrigation/trigger",
            json={"field_id": field_id, "action": "start", "duration_minutes": 30}
        )
        result = response.json()
        print(f"   ✓ Valve Status: {result['valve_status']}")
        print(f"   💧 Flow Rate: {result['flow_rate_liters_per_hour']} L/h")
        print(f"   📊 Estimated Water: {result['estimated_water_volume']} L")
        
        # 10. Get irrigation history
        print("\n🔟 Irrigation History")
        response = await client.get(
            f"{BASE_URL}/api/v1/irrigation/history",
            params={"field_id": field_id, "days": 30}
        )
        history = response.json()
        print(f"   Total events: {len(history)}")
        
        # 11. Calculate water savings
        print("\n1️⃣1️⃣ Water Savings Report")
        response = await client.get(
            f"{BASE_URL}/api/v1/irrigation/savings",
            params={"field_id": field_id}
        )
        savings = response.json()
        if 'total_water_used_liters' in savings:
            print(f"   💧 Water Used: {savings.get('total_water_used_liters')} L")
            print(f"   ♻️  Saved (vs traditional): {savings.get('water_savings_liters')} L ({savings.get('water_savings_percent')}%)")
            print(f"   💰 Cost Savings: ${savings.get('water_savings_cost_usd')}")
        else:
            print(f"   ⚠️  Savings response: {savings}")
        
        # 12. Temporal satellite trend
        print("\n1️⃣2️⃣ Vegetation Trend (30 days)")
        response = await client.get(
            f"{BASE_URL}/api/v1/satellite/temporal-trend",
            params={"latitude": 12.6667, "longitude": 108.0333, "days": 30}
        )
        trend = response.json()
        print(f"   Trend Direction: {trend['trend']}")
        print(f"   Current NDVI: {trend['ndvi_trend'][-1]} (30 days ago: {trend['ndvi_trend'][0]})")
    
    print("\n" + "="*60)
    print("✅ API Test Complete!")
    print("\nNext Steps:")
    print("1. Open http://localhost:5173 to view dashboard")
    print("2. Check http://localhost:8000/docs for interactive API docs")
    print("3. Try creating more fields with different locations")

if __name__ == "__main__":
    print("🚀 Make sure backend is running at http://localhost:8000")
    asyncio.run(test_api())
