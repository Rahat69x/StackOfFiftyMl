"""
FastAPI router dedicated to Predicting Building Energy Consumption (ML025).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml025", tags=["Project ML025"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML025", "name": "Predicting Building Energy Consumption", "category": "Regression / Forecasting"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML025", "prediction": [1], "status": "success"}
