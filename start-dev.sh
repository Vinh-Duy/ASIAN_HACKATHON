#!/bin/bash
# Start AgriDrop Development Environment

echo "🌾 Starting AgriDrop..."
echo "====================="

# Start Backend in background
echo "Starting Backend Server..."
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Give backend time to start
sleep 3

# Start Frontend
echo "Starting Frontend Server..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Services started!"
echo ""
echo "📊 Dashboard: http://localhost:5173"
echo "📚 API Docs:  http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for Ctrl+C
trap "echo 'Stopping services...'; kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT
wait
