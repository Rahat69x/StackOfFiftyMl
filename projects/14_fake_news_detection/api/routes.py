"""
FastAPI router dedicated to Fake News Detection (ML014).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml014", tags=["Project ML014"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML014", "name": "Fake News Detection", "category": "NLP"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML014", "prediction": [1], "status": "success"}
