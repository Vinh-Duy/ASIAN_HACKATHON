# AgriDrop - Smart Precision Irrigation System 🌾💧

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**AgriDrop** is a smart precision irrigation system using satellite data, AI/ML and IoT to optimize water usage in agriculture. The project aims to solve the water scarcity problems in Central Highlands and other regions.

## 🎯 Problem & Solution

### Problem
- Farmers irrigate based on "intuition" - when soil looks dry, they pump water carelessly
- Waste 30-40% of groundwater
- Prolonged drought in Central Highlands affects coffee and durian cultivation

### AgriDrop Solution
1. **Precision Irrigation** combined with satellite data
2. **AI** calculates Evapotranspiration (ET0) - the actual water needed
3. **Soil moisture sensors** + **Real-time weather data** from OpenWeather API
4. **Automatic control** of drip irrigation valves (IoT)

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend Dashboard (React/Vue)            │
│  - Online map + Crop health indices (NDVI, NDWI)           │
│  - Control irrigation valves, view weather forecast        │
└──────────────────┬──────────────────────────────────────────┘
                   │ API Calls
┌──────────────────▼──────────────────────────────────────────┐
│              Backend API (Python FastAPI)                     │
│  ├─ /api/v1/fields - Field management                      │
│  ├─ /api/v1/analysis - Complete analysis                   │
│  ├─ /api/v1/irrigation - Irrigation control                │
│  ├─ /api/v1/weather - Weather data                         │
│  └─ /api/v1/satellite - Satellite indices                  │
└──────────────────┬──────────────────────────────────────────┘
                   │
       ┌───────────┼───────────┐
       │           │           │
   ┌───▼──┐  ┌──────▼────┐  ┌──▼────┐
   │ AI   │  │ Weather   │  │Satellite│
   │Engine│  │ API       │  │ Data    │
   │ (ML) │  │(OpenWeather)│ │(Sentinel)│
   └──────┘  └───────────┘  └─────────┘
```

## 🚀 Quick Start

### Requirements
- Python 3.9+
- Node.js 16+
- API Key from OpenWeather (free)

### 1. Backend Setup

```bash
# Clone repo
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp ../.env.example ../.env
# Fill in OPENWEATHER_API_KEY in .env

# Run server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server runs at: `http://localhost:8000`
- API Docs (Swagger): `http://localhost:8000/docs`

### 2. Frontend Setup

```bash
# Open new terminal
cd frontend

# Install dependencies
npm install

# Dev server
npm run dev
```

Dashboard runs at: `http://localhost:5173`

## 📊 API Endpoints

### Fields Management
```bash
POST   /api/v1/fields              # Create field
GET    /api/v1/fields              # List fields
GET    /api/v1/fields/{field_id}   # Field details
```

### Weather & Satellite Data
```bash
GET    /api/v1/weather                    # Current weather
GET    /api/v1/weather/forecast           # 7-day forecast
GET    /api/v1/satellite/indices          # NDVI, NDWI
GET    /api/v1/satellite/water-stress     # Stress map
```

### Field Analysis
```bash
GET    /api/v1/analysis/{field_id}        # Complete analysis
```

### Irrigation Control
```bash
POST   /api/v1/irrigation/trigger         # Start irrigation
POST   /api/v1/irrigation/schedule        # Schedule irrigation
GET    /api/v1/irrigation/schedules       # View schedules
GET    /api/v1/irrigation/savings         # Calculate water savings
```

## 🤖 AI/ML Engine

### Evapotranspiration (ET0) Calculation
Using **Hargreaves-Samani Formula**:
```
ET0 = 0.0023 * (T + 17.8) * √(Tmax - Tmin) * Ra
```

Where:
- T = Mean temperature (°C)
- Tmax, Tmin = Max/Min temperature
- Ra = Extraterrestrial radiation

### Crop Water Requirement
```
ETc = ET0 × Kc × (Soil_Moisture_Factor)
```

Kc (crop coefficient):
- Mature coffee: 0.7
- Mature durian: 0.8

## 📈 Features

### ✅ Current
- [x] Complete backend API
- [x] Dashboard frontend React/Vue
- [x] Calculate ET0 from weather data
- [x] Get data from OpenWeather API (real)
- [x] Mock satellite data (NDVI, NDWI)
- [x] Irrigation valve control (simulation)
- [x] Irrigation scheduling

### 🔄 Coming Soon (Production Ready)
- [ ] Google Earth Engine API integration
- [ ] PostgreSQL database
- [ ] Authentication & Authorization
- [ ] Mobile app (React Native/Flutter)
- [ ] Real IoT valve control
- [ ] ML model training (XGBoost)
- [ ] Predictive watering schedules
- [ ] Multi-language support

## 📁 Project Structure

```
AgriDrop/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py           # API endpoints
│   │   ├── services/
│   │   │   ├── weather_service.py  # OpenWeather API
│   │   │   ├── ai_service.py       # ET0, ML calculations
│   │   │   ├── irrigation_service.py
│   │   │   └── satellite_service.py # NDVI, NDWI
│   │   ├── main.py                 # FastAPI app
│   │   ├── models.py               # Data models
│   │   └── schemas.py              # Pydantic schemas
│   ├── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── MapContainer.vue
│   │   │   ├── AnalyticsChart.vue
│   │   │   ├── WeatherWidget.vue
│   │   │   ├── IrrigationControl.vue
│   │   │   └── FieldsManager.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── docs/
│   └── technical_architecture.md
├── .env.example
└── README.md
```

## 🌡️ Example API Response

```json
{
  "field_id": "abc123",
  "soil_moisture": 45.2,
  "evapotranspiration": 6.8,
  "water_deficit": 3.5,
  "recommendation": "💧 Moderate irrigation needed. Start within 24 hours.",
  "confidence": 0.82,
  "timestamp": "2026-05-09T10:30:00"
}
```

## 💡 Demo Walkthrough

1. **Create field**: Enter GPS + area
2. **View analysis**: Dashboard shows soil moisture, ET0, recommendations
3. **Check weather**: 7-day forecast from OpenWeather
4. **Control irrigation**: 
   - **Auto Mode**: System automatically irrigates based on moisture
   - **Manual Mode**: Click button to activate valve
5. **See results**: Water savings compared to traditional irrigation (40% optimized)

## 📊 Expected Results

- **Water savings**: 30-40%
- **Cost savings**: ~20-30% (electricity, water)
- **Productivity increase**: +15-20% (healthier crops)
- **ROI**: 6-12 months

## 🔐 Security

- [ ] API authentication (JWT)
- [ ] Rate limiting
- [ ] Input validation
- [ ] SQL injection protection
- [ ] CORS configuration

## 📝 License

MIT License - Free to use for educational & commercial purposes

## 👥 Team

AgriDrop project developed for **ASIA Hackathon 2026**

## 📞 Support

- 📧 Email: support@agridrop.io
- 🐛 Issues: [GitHub Issues](https://github.com/agridrop/issues)
- 📚 Docs: [Technical Architecture](./docs/technical_architecture.md)

---

**"Smart agriculture, green future. 🌾💚"**
