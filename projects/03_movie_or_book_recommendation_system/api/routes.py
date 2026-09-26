"""
FastAPI router dedicated to Movie Or Book Recommendation System (ML003).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml003", tags=["Project ML003"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML003", "name": "Movie Or Book Recommendation System", "category": "Recommendation"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML003", "prediction": [1], "status": "success"}
