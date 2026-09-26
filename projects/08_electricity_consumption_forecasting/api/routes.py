"""
FastAPI router dedicated to Electricity Consumption Forecasting (ML008).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml008", tags=["Project ML008"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML008", "name": "Electricity Consumption Forecasting", "category": "Time Series"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML008", "prediction": [1], "status": "success"}
