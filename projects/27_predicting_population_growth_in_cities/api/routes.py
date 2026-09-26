"""
FastAPI router dedicated to Predicting Population Growth In Cities (ML027).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml027", tags=["Project ML027"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML027", "name": "Predicting Population Growth In Cities", "category": "Time Series"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML027", "prediction": [1], "status": "success"}
