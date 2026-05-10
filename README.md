# AgriDrop - Smart Precision Irrigation System 🌾💧

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**AgriDrop** là hệ thống tưới tiêu chính xác thông minh sử dụng dữ liệu vệ tinh, AI/ML và IoT để tối ưu hóa sử dụng nước trong nông nghiệp. Dự án nhằm giải quyết vấn đề hạn hán tại Tây Nguyên và các vùng khác.

## 🎯 Vấn đề & Giải pháp

### Vấn đề
- Nông dân tưới nước theo "cảm tính", thấy đất khô là bơm nước lênh láng
- Lãng phí 30-40% lượng nước ngầm
- Hạn hán kéo dài tại Tây Nguyên ảnh hưởng đến trồng cà phê, sầu riêng

### Giải pháp AgriDrop
1. **Tưới tiêu chính xác (Precision Irrigation)** kết hợp dữ liệu vệ tinh
2. **AI** tính toán Evapotranspiration (ET0) - lượng nước thực sự cần thiết
3. **Cảm biến độ ẩm** + **Dữ liệu thời tiết thực tế** từ OpenWeather API
4. **Điều khiển tự động** van tưởi nhỏ giọt (IoT)

## 🏗️ Kiến trúc Hệ thống

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend Dashboard (React/Vue)            │
│  - Bản đồ trực tuyến + Chỉ số sức khỏe cây (NDVI, NDWI)   │
│  - Điều khiển van tưới, xem dự báo thời tiết               │
└──────────────────┬──────────────────────────────────────────┘
                   │ API Calls
┌──────────────────▼──────────────────────────────────────────┐
│              Backend API (Python FastAPI)                     │
│  ├─ /api/v1/fields - Quản lý thửa ruộng                    │
│  ├─ /api/v1/analysis - Phân tích toàn bộ                   │
│  ├─ /api/v1/irrigation - Điều khiển tưới tiêu             │
│  ├─ /api/v1/weather - Dữ liệu thời tiết                   │
│  └─ /api/v1/satellite - Chỉ số vệ tinh                     │
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

### Yêu cầu
- Python 3.9+
- Node.js 16+
- API Key từ OpenWeather (miễn phí)

### 1. Backend Setup

```bash
# Clone repo
cd backend

# Tạo virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# hoặc: venv\Scripts\activate  # Windows

# Cài đặt dependencies
pip install -r requirements.txt

# Tạo .env file
cp ../.env.example ../.env
# Điền OPENWEATHER_API_KEY vào .env

# Chạy server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server chạy tại: `http://localhost:8000`
- API Docs (Swagger): `http://localhost:8000/docs`

### 2. Frontend Setup

```bash
# Mở terminal mới
cd frontend

# Cài dependencies
npm install

# Dev server
npm run dev
```

Dashboard chạy tại: `http://localhost:5173`

## 📊 API Endpoints

### Fields Management
```bash
POST   /api/v1/fields              # Tạo thửa ruộng
GET    /api/v1/fields              # Danh sách thửa
GET    /api/v1/fields/{field_id}   # Chi tiết thửa
```

### Weather & Satellite Data
```bash
GET    /api/v1/weather                    # Thời tiết hiện tại
GET    /api/v1/weather/forecast           # Dự báo 7 ngày
GET    /api/v1/satellite/indices          # NDVI, NDWI
GET    /api/v1/satellite/water-stress     # Bản đồ stress
```

### Field Analysis
```bash
GET    /api/v1/analysis/{field_id}        # Phân tích toàn bộ
```

### Irrigation Control
```bash
POST   /api/v1/irrigation/trigger         # Kích hoạt tưới
POST   /api/v1/irrigation/schedule        # Lên lịch tưới
GET    /api/v1/irrigation/schedules       # Xem lịch
GET    /api/v1/irrigation/savings         # Tính nước tiết kiệm
```

## 🤖 AI/ML Engine

### Evapotranspiration (ET0) Calculation
Sử dụng **Hargreaves-Samani Formula**:
```
ET0 = 0.0023 * (T + 17.8) * √(Tmax - Tmin) * Ra
```

Với:
- T = Nhiệt độ trung bình (°C)
- Tmax, Tmin = Nhiệt độ cao/thấp
- Ra = Bức xạ ngoài khí quyển

### Crop Water Requirement
```
ETc = ET0 × Kc × (Soil_Moisture_Factor)
```

Kc (hệ số cây):
- Cà phê trưởng thành: 0.7
- Sầu riêng trưởng thành: 0.8

## 📈 Features

### ✅ Hiện tại
- [x] API backend hoàn chỉnh
- [x] Dashboard frontend React/Vue
- [x] Tính ET0 từ dữ liệu thời tiết
- [x] Lấy dữ liệu từ OpenWeather API (thực)
- [x] Mock satellite data (NDVI, NDWI)
- [x] Điều khiển van tưới (mô phỏng)
- [x] Lập lịch tưới tiêu

### 🔄 Sắp tới (Production Ready)
- [ ] Kết nối Google Earth Engine API
- [ ] Database PostgreSQL
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

1. **Tạo thửa ruộng**: Nhập GPS + diện tích
2. **Xem phân tích**: Dashboard hiển thị độ ẩm đất, ET0, khuyến nghị
3. **Kiểm tra thời tiết**: Dự báo 7 ngày từ OpenWeather
4. **Điều khiển tưới**: 
   - **Auto Mode**: Hệ thống tự tưới dựa trên độ ẩm
   - **Manual Mode**: Bấm button để kích hoạt van
5. **Xem kết quả**: Lượng nước tiết kiệm so với tưới truyền thống (40% tối ưu)

## 📊 Expected Results

- **Tiết kiệm nước**: 30-40%
- **Tiết kiệm chi phí**: ~20-30% (điện, nước)
- **Tăng năng suất**: +15-20% (cây khỏe hơn)
- **ROI**: 6-12 tháng

## 🔐 Security

- [ ] API authentication (JWT)
- [ ] Rate limiting
- [ ] Input validation
- [ ] SQL injection protection
- [ ] CORS configuration

## 📝 License

MIT License - Tự do sử dụng cho mục đích giáo dục & thương mại

## 👥 Team

Dự án AgriDrop được phát triển cho **ASIA Hackathon 2026**

## 📞 Support

- 📧 Email: support@agridrop.io
- 🐛 Issues: [GitHub Issues](https://github.com/agridrop/issues)
- 📚 Docs: [Technical Architecture](./docs/technical_architecture.md)

---

**"Nông nghiệp thông minh, tương lai xanh. 🌾💚"**
