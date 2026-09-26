"""
FastAPI router dedicated to Clothing Style Recommendation System (ML036).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml036", tags=["Project ML036"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML036", "name": "Clothing Style Recommendation System", "category": "Recommendation"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML036", "prediction": [1], "status": "success"}
