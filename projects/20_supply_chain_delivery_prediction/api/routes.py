"""
FastAPI router dedicated to Supply Chain Delivery Prediction (ML020).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml020", tags=["Project ML020"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML020", "name": "Supply Chain Delivery Prediction", "category": "Regression / Forecasting"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML020", "prediction": [1], "status": "success"}
