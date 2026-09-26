"""
FastAPI router dedicated to Noise Reduction In Speech Recordings (ML048).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml048", tags=["Project ML048"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML048", "name": "Noise Reduction In Speech Recordings", "category": "Audio"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML048", "prediction": [1], "status": "success"}
