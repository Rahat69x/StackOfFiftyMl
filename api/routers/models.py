"""
MLFORGE API — Models Router
Endpoints for querying model registry, comparing versions, and executing rollbacks.
"""

from fastapi import APIRouter, HTTPException
from core.model_registry import model_registry
from core.project_registry import registry
from api.schemas.common import ResponseEnvelope, RollbackRequest

router = APIRouter(prefix="/models", tags=["Models"])


@router.get("", response_model=ResponseEnvelope)
def list_models():
    """Lists all models registered across all projects."""
    models = model_registry.list_all_models()
    return ResponseEnvelope(
        data=models,
        meta={"total": len(models)}
    )


@router.get("/{project_id}/compare", response_model=ResponseEnvelope)
def compare_project_models(project_id: str):
    """Compares metrics across multiple model versions for a given project."""
    p = registry.get_project(project_id)
    if not p:
        raise HTTPException(status_code=404, detail=f"Project '{project_id}' not found.")
    comparison = model_registry.compare_models(p["id"])
    return ResponseEnvelope(data=comparison)


@router.post("/rollback", response_model=ResponseEnvelope)
def rollback_model(req: RollbackRequest):
    """Rolls back the active model to a target historical version."""
    res = model_registry.rollback(req.project_id, req.target_version)
    if not res:
        raise HTTPException(status_code=404, detail=f"Target version '{req.target_version}' not found for project '{req.project_id}'.")
    return ResponseEnvelope(
        data={"message": f"Successfully rolled back {req.project_id} to {req.target_version}", "model": res}
    )
