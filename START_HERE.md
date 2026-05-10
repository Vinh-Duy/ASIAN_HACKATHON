# 📖 Read These Files First

## For Quick Start (5 minutes)
1. **Start here** → [GETTING_STARTED.md](GETTING_STARTED.md) ⭐ **READ THIS FIRST**
2. **Quick setup** → [QUICK_START.md](QUICK_START.md)
3. **Run the app** → [start-dev.sh](start-dev.sh)

## For Project Overview
1. **What is it?** → [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
2. **All features** → [FEATURES.md](FEATURES.md)
3. **Full guide** → [README.md](README.md)

## For Developers
1. **Architecture** → [docs/technical_architecture.md](docs/technical_architecture.md)
2. **File structure** → [INDEX.md](INDEX.md)
3. **API endpoints** → [backend/app/api/routes.py](backend/app/api/routes.py)

## For Hackathon
1. **Submission info** → [SUBMISSION.md](SUBMISSION.md)
2. **Feature checklist** → [FEATURES.md](FEATURES.md)
3. **Demo script** → [test_api.py](test_api.py)

---

## 🚀 Quickest Path to Working System

```
1. Read: GETTING_STARTED.md (5 min)
   ↓
2. Run: ./setup.sh (2 min)
   ↓
3. Run: ./start-dev.sh (1 min)
   ↓
4. Open: http://localhost:5173 (1 min)
   ↓
5. Done! System is running 🎉
```

---

## 📁 Key Files You Need

### To Run the System
- [setup.sh](setup.sh) - First time setup
- [start-dev.sh](start-dev.sh) - Start both servers
- [.env.example](.env.example) - Configuration template
- [test_api.py](test_api.py) - Test all APIs

### To Understand Code
- [backend/app/main.py](backend/app/main.py) - Backend entry point
- [backend/app/api/routes.py](backend/app/api/routes.py) - All API endpoints
- [backend/app/services/ai_service.py](backend/app/services/ai_service.py) - ET0 calculation
- [frontend/src/App.vue](frontend/src/App.vue) - Frontend main component

### To Deploy
- [docker-compose.yml](docker-compose.yml) - Docker setup
- [Dockerfile.backend](Dockerfile.backend) - Backend image
- [Dockerfile.frontend](Dockerfile.frontend) - Frontend image

---

## 📚 Documentation Overview

| Document | What It Contains | Read Time |
|----------|------------------|-----------|
| GETTING_STARTED.md | How to run everything | 5 min |
| QUICK_START.md | Step-by-step setup | 5 min |
| PROJECT_OVERVIEW.md | What the project does | 5 min |
| README.md | Complete documentation | 10 min |
| FEATURES.md | All 60+ features | 10 min |
| SUBMISSION.md | Hackathon details | 5 min |
| docs/technical_architecture.md | Deep technical dive | 20 min |
| INDEX.md | All files explained | 10 min |

---

## ✨ What Makes This Special

✅ **Real weather data** - Uses OpenWeather API (not fake)  
✅ **AI algorithms** - ET0 calculation with Hargreaves-Samani formula  
✅ **Beautiful UI** - Dark mode professional dashboard  
✅ **Production code** - Error handling, async/await, validation  
✅ **5-minute setup** - Works immediately  
✅ **Well documented** - 5000+ lines of docs  
✅ **Deployable** - Docker ready  

---

## 🎯 Quick Reference

### URLs When Running
- **Dashboard**: http://localhost:5173
- **API Docs**: http://localhost:8000/docs
- **API Base**: http://localhost:8000

### Common Commands
```bash
# Setup
./setup.sh

# Run
./start-dev.sh

# Test
python test_api.py

# Docker
docker-compose up
```

### API Endpoints (Most Important)
```
GET  /api/v1/weather              - Real weather from OpenWeather
GET  /api/v1/analysis/{field_id}  - AI analysis
POST /api/v1/irrigation/trigger   - Control watering
GET  /api/v1/satellite/indices    - NDVI/NDWI data
```

---

## 🎓 Learn the Concepts

**ET0 (Evapotranspiration)** - How much water plants lose to air  
**NDVI** - Vegetation health from satellite (0=dead, 1=healthy)  
**NDWI** - Water content from satellite (0=dry, 1=wet)  
**Kc** - Crop coefficient (how much water THIS crop needs)  

---

## 🏆 Demo Highlights

When demoing to judges:
1. **Show real weather** - Open API docs, execute weather endpoint
2. **Show analysis** - Display AI recommendation
3. **Show UI** - Dashboard looks professional
4. **Show control** - Click irrigation button
5. **Show results** - Water savings calculation

**Total demo time**: 10 minutes

---

## 💡 Pro Tips

- Keep API docs open: http://localhost:8000/docs
- Use test script to verify everything: `python test_api.py`
- Check logs in terminal to understand flow
- Mobile dashboard works on phone: `http://YOUR_IP:5173`

---

## ❓ Still Have Questions?

1. **How do I run it?** → [GETTING_STARTED.md](GETTING_STARTED.md)
2. **What is it?** → [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
3. **How does it work?** → [docs/technical_architecture.md](docs/technical_architecture.md)
4. **What features?** → [FEATURES.md](FEATURES.md)
5. **I'm a developer** → [INDEX.md](INDEX.md)

---

## ✅ Final Checklist

Before demo:
- [ ] API key added to .env
- [ ] Backend running (http://localhost:8000/docs works)
- [ ] Frontend running (http://localhost:5173 loads)
- [ ] At least 1 field created
- [ ] Test script works (`python test_api.py`)
- [ ] Can see real weather data

---

**🌾 Ready to change agriculture with AI? Let's go!**

Next step: Read [GETTING_STARTED.md](GETTING_STARTED.md) now!
