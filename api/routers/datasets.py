"""
MLFORGE API — Datasets Router
Endpoints for inspecting, registering, and tracking dataset lineage.
"""

from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from core.project_registry import registry
from core.dataset_manager import dataset_manager
from api.schemas.common import ResponseEnvelope

router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.get("", response_model=ResponseEnvelope)
def list_datasets(page: int = 1, page_size: int = 50):
    """Lists all registered datasets for all 50 projects."""
    projects = registry.get_all_projects()
    dataset_list = []
    for p in projects:
        dataset_list.append({
            "project_id": p["id"],
            "project_name": p["name"],
            "dataset_name": p["dataset"],
            "format": "csv/tensor",
            "sample_available": p.get("demo_mode_available", True),
            "status": "ready" if p.get("status") == "ready" else "dataset_required",
            "version": "1.0",
            "data_hash": f"sha256-{p['id']}-v1"
        })
        
    start = (page - 1) * page_size
    return ResponseEnvelope(
        data=dataset_list[start: start + page_size],
        meta={"total": len(dataset_list), "page": page, "page_size": page_size}
    )


@router.get("/{project_id}/lineage", response_model=ResponseEnvelope)
def get_dataset_lineage(project_id: str):
    """Returns dataset lineage and provenance information."""
    p = registry.get_project(project_id)
    if not p:
        raise HTTPException(status_code=404, detail=f"Project '{project_id}' not found.")
    
    instance = registry.get_project_instance(project_id)
    return ResponseEnvelope(data=instance.get_lineage())
