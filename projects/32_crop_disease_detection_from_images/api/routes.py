"""
FastAPI router dedicated to Crop Disease Detection From Images (ML032).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml032", tags=["Project ML032"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML032", "name": "Crop Disease Detection From Images", "category": "Computer Vision"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML032", "prediction": [1], "status": "success"}
