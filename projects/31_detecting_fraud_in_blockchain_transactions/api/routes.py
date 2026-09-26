"""
FastAPI router dedicated to Detecting Fraud In Blockchain Transactions (ML031).
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional

router = APIRouter(prefix="/ml031", tags=["Project ML031"])

class PredictPayload(BaseModel):
    inputs: Any
    request_id: Optional[str] = None

@router.get("/info")
def get_info():
    return {"project_id": "ML031", "name": "Detecting Fraud In Blockchain Transactions", "category": "Security / Fraud"}

@router.post("/predict")
def predict_endpoint(payload: PredictPayload):
    return {"project_id": "ML031", "prediction": [1], "status": "success"}
