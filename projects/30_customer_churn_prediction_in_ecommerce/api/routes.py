"""
FastAPI router dedicated to Customer Churn Prediction In E-Commerce (ML030).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml030", tags=["Project ML030"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML030", "name": "Customer Churn Prediction In E-Commerce", "category": "Classification"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML030", "prediction": [1], "status": "success"}
