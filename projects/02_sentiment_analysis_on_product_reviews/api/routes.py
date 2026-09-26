"""
FastAPI router dedicated to Sentiment Analysis On Product Reviews (ML002).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml002", tags=["Project ML002"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML002", "name": "Sentiment Analysis On Product Reviews", "category": "NLP"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML002", "prediction": [1], "status": "success"}
