"""
MLFORGE API Schemas
Pydantic data models for requests, responses, filters, and metrics.
"""

from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class ResponseEnvelope(BaseModel):
    data: Any
    meta: Optional[Dict[str, Any]] = None


class ErrorEnvelope(BaseModel):
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None


class ProjectSummary(BaseModel):
    id: str
    slug: str
    name: str
    category: str
    type: str
    status: str
    dataset: str
    model: str
    version: str
    complexity_level: str
    responsible_use_flags: List[str]
    demo_mode_available: bool
    tags: List[str]
    description: str


class ProjectDetail(ProjectSummary):
    owner: str
    limitations: str
    responsible_use_notes: str
    metrics: List[str]


class TrainRequest(BaseModel):
    hyperparameters: Optional[Dict[str, Any]] = Field(default_factory=dict)
    random_seed: Optional[int] = 42
    dataset_version: Optional[str] = "1.0"


class PredictRequest(BaseModel):
    inputs: Any = Field(..., description="Feature array, dict of inputs, text string, or image tensor")
    request_id: Optional[str] = None


class PredictionResponse(BaseModel):
    project_id: str
    request_id: str
    prediction: Any
    probabilities: Optional[Any] = None
    explanation: Optional[Dict[str, Any]] = None
    latency_ms: float
    model_version: str


class RollbackRequest(BaseModel):
    project_id: str
    target_version: str


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    username: str


class NotificationResponse(BaseModel):
    id: str
    title: str
    message: str
    type: str
    read: bool
    timestamp_iso: str
    project_id: str
