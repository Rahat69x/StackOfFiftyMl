"""
FastAPI router dedicated to Matching Resumes To Job Descriptions (ML045).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml045", tags=["Project ML045"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML045", "name": "Matching Resumes To Job Descriptions", "category": "NLP"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML045", "prediction": [1], "status": "success"}
