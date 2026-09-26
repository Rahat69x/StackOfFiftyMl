"""
FastAPI router dedicated to Demand Forecasting For Products (ML015).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml015", tags=["Project ML015"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML015", "name": "Demand Forecasting For Products", "category": "Time Series / Forecasting"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML015", "prediction": [1], "status": "success"}
