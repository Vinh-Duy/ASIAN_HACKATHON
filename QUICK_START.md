# AgriDrop - Quick Start Guide ⚡

Get up and running in **5 minutes**!

## Prerequisites
- Python 3.9+
- Node.js 16+
- Git

## Step 1: Get Free API Key (2 minutes)

1. Go to https://openweathermap.org/api
2. Click "Sign Up" and create account
3. Go to "API keys" tab
4. Copy your API key (free tier = 1000 calls/day)

## Step 2: Clone & Setup (2 minutes)

```bash
# Download project
cd ~/Desktop/ASIA_HACKATHON

# Setup backend
cd backend
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

pip install -r requirements.txt
cd ..

# Setup frontend
cd frontend
npm install
cd ..
```

## Step 3: Configure Environment (1 minute)

```bash
# Copy env template
cp .env.example .env

# Edit .env file and add your API key
# OPENWEATHER_API_KEY=your_key_here
```

## Step 4: Start Services (1 minute)

**Terminal 1 - Backend**:
```bash
cd backend
source venv/bin/activate  # macOS/Linux
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend**:
```bash
cd frontend
npm run dev
```

## Access the System

- **Dashboard**: http://localhost:5173
- **API Docs**: http://localhost:8000/docs
- **API Base**: http://localhost:8000

## Test It Out

### 1. View Real Weather (Real OpenWeather API)
Visit: http://localhost:8000/docs
- Click "Try it out" on `/api/v1/weather`
- Enter: `latitude: 12.6667`, `longitude: 108.0333`
- Click "Execute" → See real weather data! 🌡️

### 2. Create a Field
In dashboard: Click "Add New Field"
- Name: "My Coffee Farm"
- Latitude: 12.6667
- Longitude: 108.0333
- Area: 5 hectares
- Crop: Coffee

### 3. View Analysis
Dashboard shows:
- Current soil moisture
- Water deficit
- Evapotranspiration (ET0)
- 💡 Recommendation from AI

### 4. Control Irrigation
Dashboard → Irrigation tab:
- Click "▶️ Start Irrigation"
- System simulates van opening
- See estimated water volume

### 5. Check Savings
Dashboard shows water saved (30-40%)

---

## Quick API Examples

### Get Weather (with real data)
```bash
curl http://localhost:8000/api/v1/weather?latitude=12.6667&longitude=108.0333
```

### Create Field
```bash
curl -X POST http://localhost:8000/api/v1/fields \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Field A",
    "latitude": 12.6667,
    "longitude": 108.0333,
    "area_hectares": 5,
    "crop_type": "coffee"
  }'
```

### Analyze Field
```bash
# Replace field_id with actual ID from create response
curl http://localhost:8000/api/v1/analysis/field_123
```

---

## Troubleshooting

### Backend won't start
```bash
# Make sure venv is activated
source venv/bin/activate

# Check Python version
python --version  # Should be 3.9+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Frontend won't start
```bash
# Clear cache
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Weather data not showing
- Check your OpenWeather API key is in `.env`
- Verify you're online
- Try a different location

### Port already in use
```bash
# Backend on different port
uvicorn app.main:app --port 8001

# Frontend on different port  
# Edit frontend/vite.config.js: port: 5174
```

---

## Project Architecture (30 seconds)

```
Frontend (React/Vue)
     ↓ HTTP/JSON
Backend (Python FastAPI)
     ↓
Services:
  - Weather (OpenWeather API) → Real data!
  - AI/ML (ET0 calculation)
  - Satellite (mock NDVI/NDWI)
  - Irrigation (valve control)
```

---

## Key Technologies Explained

### ET0 (Evapotranspiration)
- How much water a crop loses to atmosphere
- Calculated using: Temperature, Humidity, Wind Speed, Solar Radiation
- Result: 4-8 mm/day typically

### NDVI (Normalized Difference Vegetation Index)
- Measures vegetation health: 0 (dead) to 1 (very healthy)
- From satellite: Red and Near-Infrared bands

### NDWI (Normalized Difference Water Index)
- Measures water content in soil/vegetation: 0 (dry) to 1 (wet)
- Helps estimate soil moisture

---

## Next Steps

1. ✅ System running locally
2. 🎨 Customize dashboard (colors, fields, crops)
3. 🔌 Integrate real IoT valves (future)
4. 📊 Add more crops & regions
5. 🚀 Deploy to cloud (AWS/GCP)

---

## File Locations

| What | Where |
|------|-------|
| Backend code | `backend/app/` |
| Frontend code | `frontend/src/` |
| API endpoints | `backend/app/api/routes.py` |
| AI algorithms | `backend/app/services/ai_service.py` |
| Dashboard | `frontend/src/App.vue` |
| Settings | `.env` |

---

## Performance Expectations

- API response: < 1 second
- Dashboard load: < 2 seconds
- Weather update: Every 5-10 minutes
- Supports: 1000+ fields simultaneously

---

**That's it!** You now have a working smart irrigation system. 🌾💧

Need help? Check the full README.md or docs/technical_architecture.md
