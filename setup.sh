#!/bin/bash
# AgriDrop Setup Script

echo "🌾 AgriDrop Setup Script"
echo "======================="

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check Python
echo -e "${BLUE}Checking Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.9+"
    exit 1
fi
echo -e "${GREEN}✓ Python found: $(python3 --version)${NC}"

# Check Node.js
echo -e "${BLUE}Checking Node.js...${NC}"
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 16+"
    exit 1
fi
echo -e "${GREEN}✓ Node.js found: $(node --version)${NC}"

# Setup Backend
echo -e "${BLUE}Setting up Backend...${NC}"
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..
echo -e "${GREEN}✓ Backend dependencies installed${NC}"

# Setup Frontend
echo -e "${BLUE}Setting up Frontend...${NC}"
cd frontend
npm install
cd ..
echo -e "${GREEN}✓ Frontend dependencies installed${NC}"

# Create .env file
echo -e "${BLUE}Creating .env file...${NC}"
cp .env.example .env
echo -e "${GREEN}✓ .env created. Please add your API keys!${NC}"

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "1. Add API keys to .env file"
echo "2. Start backend: cd backend && source venv/bin/activate && uvicorn app.main:app --reload"
echo "3. Start frontend: cd frontend && npm run dev"
echo ""
echo "Dashboard: http://localhost:5173"
echo "API Docs: http://localhost:8000/docs"
