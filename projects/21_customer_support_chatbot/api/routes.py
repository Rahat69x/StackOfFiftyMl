"""
FastAPI router dedicated to Customer Support Chatbot (ML021).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml021", tags=["Project ML021"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML021", "name": "Customer Support Chatbot", "category": "NLP"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML021", "prediction": [1], "status": "success"}
