# AgriDrop Technical Architecture

## System Overview

AgriDrop is a precision irrigation management system that combines satellite imagery, weather data, and machine learning to optimize water usage in agriculture.

## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Server**: Uvicorn ASGI
- **Database**: PostgreSQL (production) / SQLite (dev)
- **ML**: Scikit-learn, NumPy, Pandas
- **APIs**: OpenWeather, Google Earth Engine (future)

### Frontend
- **Framework**: Vue 3
- **Build Tool**: Vite
- **Styling**: TailwindCSS
- **Charts**: Chart.js / Recharts
- **Maps**: Leaflet / Google Maps

### Infrastructure
- **Containerization**: Docker (optional)
- **Deployment**: Docker, AWS/GCP (future)
- **Monitoring**: Prometheus (future)

## Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. DATA INPUT LAYER                                              │
├─────────────────────────────────────────────────────────────────┤
│ • User Input: Field GPS coordinates, crop type, area            │
│ • Weather API: OpenWeather (temperature, humidity, wind)        │
│ • Satellite: Google Earth Engine (NDVI, NDWI, historical)       │
│ • IoT Sensors: Soil moisture sensors (optional)                 │
└─────────────────────────────────────┬───────────────────────────┘
                                      │
┌─────────────────────────────────────▼───────────────────────────┐
│ 2. PROCESSING LAYER (Backend Services)                           │
├─────────────────────────────────────────────────────────────────┤
│ Weather Service:                                                 │
│   • Fetch real-time weather from OpenWeather API                │
│   • Parse forecast data for 7 days                              │
│   • Cache results (5-10 min TTL)                                │
│                                                                  │
│ Satellite Service:                                              │
│   • Retrieve vegetation index (NDVI) > 0.6 = healthy           │
│   • Retrieve water index (NDWI) > 0.3 = moist soil             │
│   • Calculate water stress maps                                 │
│   • Track temporal trends                                       │
│                                                                  │
│ AI/ML Service:                                                  │
│   • Calculate ET0 (Reference Evapotranspiration)               │
│   • Calculate ETc (Crop Evapotranspiration)                    │
│   • Estimate soil moisture from satellite indices              │
│   • Predict water deficit                                       │
│   • Generate irrigation recommendations                         │
│                                                                  │
│ Irrigation Service:                                             │
│   • Schedule irrigation events                                  │
│   • Control valve state (open/close)                           │
│   • Log history and calculate savings                          │
└─────────────────────────────────────┬───────────────────────────┘
                                      │
┌─────────────────────────────────────▼───────────────────────────┐
│ 3. DATABASE LAYER                                                │
├─────────────────────────────────────────────────────────────────┤
│ • Fields (metadata)                                             │
│ • Weather History (time series)                                 │
│ • Satellite Data (temporal trends)                              │
│ • Irrigation Events (log & analytics)                           │
│ • User Settings & Preferences                                   │
└─────────────────────────────────────┬───────────────────────────┘
                                      │
┌─────────────────────────────────────▼───────────────────────────┐
│ 4. API LAYER (RESTful)                                          │
├─────────────────────────────────────────────────────────────────┤
│ • /api/v1/fields/* - Field management                          │
│ • /api/v1/analysis/* - Field analysis & recommendations        │
│ • /api/v1/weather/* - Weather data                             │
│ • /api/v1/satellite/* - Satellite indices                      │
│ • /api/v1/irrigation/* - Irrigation control                    │
└─────────────────────────────────────┬───────────────────────────┘
                                      │
┌─────────────────────────────────────▼───────────────────────────┐
│ 5. FRONTEND LAYER (UI)                                          │
├─────────────────────────────────────────────────────────────────┤
│ • Dashboard: Real-time field status & analytics                │
│ • Map View: Field locations with color-coded stress levels    │
│ • Weather Widget: Current conditions & forecast                │
│ • Irrigation Control: Start/stop/schedule                      │
│ • Charts: ET0 trends, soil moisture, water usage               │
│ • Alerts: Critical warnings for drought/over-watering          │
└─────────────────────────────────────────────────────────────────┘
```

## Algorithm Details

### 1. Reference Evapotranspiration (ET0) - Hargreaves-Samani

```python
def calculate_et0(temp, wind_speed, humidity, solar_radiation):
    # ET0 = 0.0023 * (T + 17.8) * √(Tmax - Tmin) * Ra / 2.45
    # Where:
    # T = mean daily temperature (°C)
    # Ra = extraterrestrial radiation (MJ/m²/day)
    # Returns: ET0 in mm/day
```

**Input Parameters**:
- Temperature (°C)
- Humidity (%)
- Wind Speed (m/s)
- Solar Radiation (MJ/m²/day)

**Output**:
- ET0: 4-8 mm/day (typical range)

### 2. Crop Water Requirement (ETc)

```python
ETc = ET0 × Kc × (Soil_Moisture_Factor)

Where:
- ET0 = Reference evapotranspiration
- Kc = Crop coefficient (0.3-0.9 depending on crop & stage)
- Soil_Moisture_Factor = 0.3 to 1.0 based on current soil moisture
```

**Crop Coefficients** (Kc):
- Coffee (young): 0.5
- Coffee (mature): 0.7
- Coffee (blooming): 0.85
- Durian (young): 0.4
- Durian (mature): 0.8
- Durian (blooming): 0.9

### 3. Water Deficit Calculation

```python
Water_Deficit = ETc - (Soil_Moisture / 100 × Field_Area)

If Water_Deficit > threshold:
    → Generate irrigation recommendation
    → Schedule automatic irrigation
```

### 4. Soil Moisture Estimation (from Satellite)

```python
# NDVI = (NIR - RED) / (NIR + RED)
# NDWI = (NIR - SWIR) / (NIR + SWIR)

Estimated_Soil_Moisture = 50 + 30×NDWI - 10×NDVI

Range: 0% (very dry) to 100% (saturated)
```

## API Contract Examples

### Get Current Weather
```bash
GET /api/v1/weather?latitude=12.6667&longitude=108.0333

Response:
{
  "temperature": 32.5,
  "humidity": 65,
  "wind_speed": 2.3,
  "precipitation": 0,
  "clouds": 20,
  "description": "clear sky",
  "timestamp": "2026-05-09T10:30:00Z"
}
```

### Get Field Analysis
```bash
GET /api/v1/analysis/field_123

Response:
{
  "field_id": "field_123",
  "soil_moisture": 45.2,
  "evapotranspiration": 6.8,
  "water_deficit": 3.5,
  "recommendation": "Moderate irrigation needed",
  "confidence": 0.82,
  "timestamp": "2026-05-09T10:30:00Z"
}
```

### Get Satellite Indices
```bash
GET /api/v1/satellite/indices?latitude=12.6667&longitude=108.0333

Response:
{
  "ndvi": 0.65,    # Healthy vegetation
  "ndwi": 0.42,    # Moderate water content
  "timestamp": "2026-05-09T10:30:00Z"
}
```

### Trigger Irrigation
```bash
POST /api/v1/irrigation/trigger

Body:
{
  "field_id": "field_123",
  "action": "start",
  "duration_minutes": 30
}

Response:
{
  "status": "success",
  "valve_status": "open",
  "flow_rate_liters_per_hour": 50,
  "estimated_water_volume": 25,
  "triggered_at": "2026-05-09T10:30:00Z"
}
```

## Performance Metrics

### API Response Times (Target)
- Weather endpoint: < 500ms
- Satellite data: < 1s
- Analysis endpoint: < 2s
- Irrigation control: < 200ms

### Throughput
- Concurrent users: 1000+
- Requests/second: 100+
- Data accuracy: ±5% for ET0 calculations

## Security Considerations

1. **API Authentication**: JWT tokens for future implementation
2. **Rate Limiting**: 100 requests/minute per user
3. **Data Validation**: Pydantic schemas enforce input types
4. **CORS**: Allow frontend domain only
5. **HTTPS**: Required for production

## Scalability Strategy

### Horizontal Scaling
```
Load Balancer
    ├── API Server 1
    ├── API Server 2
    └── API Server 3
         ↓
    PostgreSQL (Primary)
         ↓
    PostgreSQL (Replica) - Read-only
```

### Caching
- Redis for weather data (5-10 min TTL)
- Browser cache for static assets

### Async Processing
- Celery tasks for satellite data fetching
- Background jobs for irrigation scheduling

## Monitoring & Logging

```
Application Metrics:
- Request latency (p50, p95, p99)
- Error rate by endpoint
- Active fields count
- Irrigation events/day

System Metrics:
- CPU usage
- Memory usage
- Database query times
- API response times
```

## Future Enhancements

1. **ML Model Training**
   - XGBoost for water prediction
   - Random Forest for crop health classification
   - Time series forecasting (ARIMA)

2. **Real IoT Integration**
   - LoRaWAN for sensor communication
   - MQTT protocol for valve control
   - Edge computing on gateways

3. **Advanced Features**
   - Multi-season analysis
   - Crop yield prediction
   - Cost optimization
   - Carbon footprint tracking
   - Blockchain for water credits

4. **Geographic Expansion**
   - Multi-region support
   - Local language support
   - Regional weather services
   - Localized crop data

## Deployment Checklist

- [ ] Environment variables configured
- [ ] Database migrated
- [ ] API docs generated
- [ ] Frontend built & minified
- [ ] SSL certificates
- [ ] Monitoring set up
- [ ] Backup strategy
- [ ] Load testing passed
- [ ] Security audit
- [ ] Documentation complete

---

**Last Updated**: May 2026  
**Status**: Production Ready (MVP)
