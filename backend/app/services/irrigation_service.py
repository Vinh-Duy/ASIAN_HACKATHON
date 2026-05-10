"""
Irrigation Service - Controls irrigation and manages schedules
"""
from datetime import datetime, timedelta
from typing import Dict, List, Any
import uuid

class IrrigationService:
    """
    Manages irrigation schedules and commands
    """
    
    def __init__(self):
        self.active_schedules: Dict[str, Dict] = {}
        self.history: List[Dict] = []
    
    def create_schedule(self, field_id: str, water_needed: float, 
                       scheduled_time: str, confidence: float) -> str:
        """
        Create an irrigation schedule for a field
        """
        schedule_id = str(uuid.uuid4())
        
        schedule = {
            "schedule_id": schedule_id,
            "field_id": field_id,
            "water_needed_liters": water_needed,
            "scheduled_time": scheduled_time,
            "confidence": confidence,
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "executed_at": None
        }
        
        self.active_schedules[schedule_id] = schedule
        return schedule_id
    
    def trigger_irrigation(self, field_id: str, duration_minutes: int = 30) -> Dict[str, Any]:
        """
        Trigger immediate irrigation for a field
        In real scenario, this would open the drip irrigation valve via IoT
        """
        return {
            "status": "success",
            "message": f"Irrigation triggered for field {field_id}",
            "duration_minutes": duration_minutes,
            "valve_status": "open",
            "flow_rate_liters_per_hour": 50,
            "estimated_water_volume": duration_minutes * 50 / 60,
            "triggered_at": datetime.now().isoformat(),
            "estimated_completion": (datetime.now() + timedelta(minutes=duration_minutes)).isoformat()
        }
    
    def stop_irrigation(self, field_id: str) -> Dict[str, Any]:
        """
        Stop irrigation for a field
        """
        return {
            "status": "success",
            "message": f"Irrigation stopped for field {field_id}",
            "valve_status": "closed",
            "stopped_at": datetime.now().isoformat()
        }
    
    def execute_schedule(self, schedule_id: str) -> Dict[str, Any]:
        """
        Execute a scheduled irrigation
        """
        if schedule_id not in self.active_schedules:
            return {"status": "error", "message": "Schedule not found"}
        
        schedule = self.active_schedules[schedule_id]
        schedule["status"] = "active"
        schedule["executed_at"] = datetime.now().isoformat()
        
        # Simulate irrigation
        result = {
            "status": "success",
            "schedule_id": schedule_id,
            "field_id": schedule["field_id"],
            "water_volume": schedule["water_needed_liters"],
            "started_at": datetime.now().isoformat(),
            "estimated_duration_minutes": max(15, schedule["water_needed_liters"] / 3)
        }
        
        self.history.append(result)
        return result
    
    def get_active_schedules(self, field_id: str = None) -> List[Dict]:
        """
        Get active irrigation schedules
        """
        schedules = list(self.active_schedules.values())
        if field_id:
            schedules = [s for s in schedules if s["field_id"] == field_id]
        return schedules
    
    def get_irrigation_history(self, field_id: str = None, days: int = 30) -> List[Dict]:
        """
        Get irrigation history
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        history = [h for h in self.history]
        
        if field_id:
            history = [h for h in history if h.get("field_id") == field_id]
        
        return sorted(history, key=lambda x: x.get("started_at", ""), reverse=True)
    
    def calculate_water_savings(self, field_id: str) -> Dict[str, Any]:
        """
        Calculate water savings compared to traditional irrigation
        """
        history = self.get_irrigation_history(field_id)
        
        if not history:
            return {"savings_liters": 0, "savings_percent": 0}
        
        total_water_used = sum(h.get("water_volume", 0) for h in history)
        
        # Assume traditional irrigation uses 40% more water
        traditional_usage = total_water_used * 1.4
        savings = traditional_usage - total_water_used
        savings_percent = (savings / traditional_usage) * 100 if traditional_usage > 0 else 0
        
        return {
            "total_water_used_liters": round(total_water_used, 2),
            "estimated_traditional_usage": round(traditional_usage, 2),
            "water_savings_liters": round(savings, 2),
            "water_savings_percent": round(savings_percent, 1),
            "water_savings_cost_usd": round(savings * 0.0001, 2),  # Rough estimate
            "period_days": 30
        }
