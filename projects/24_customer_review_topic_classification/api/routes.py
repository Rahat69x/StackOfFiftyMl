"""
FastAPI router dedicated to Customer Review Topic Classification (ML024).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml024", tags=["Project ML024"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML024", "name": "Customer Review Topic Classification", "category": "NLP"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML024", "prediction": [1], "status": "success"}
