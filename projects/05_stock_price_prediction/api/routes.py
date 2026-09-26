"""
FastAPI router dedicated to Stock Price Prediction (ML005).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml005", tags=["Project ML005"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML005", "name": "Stock Price Prediction", "category": "Time Series / Finance"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML005", "prediction": [1], "status": "success"}
