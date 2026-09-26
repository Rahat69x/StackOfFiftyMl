"""
MLFORGE API — Categories Router
Provides distinct categories, types, and summary metrics.
"""

from fastapi import APIRouter
from core.project_registry import registry
from api.schemas.common import ResponseEnvelope

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("", response_model=ResponseEnvelope)
def get_categories():
    """Returns all project categories and counts."""
    categories = registry.get_categories()
    stats = registry.get_stats()
    return ResponseEnvelope(
        data={
            "categories": categories,
            "counts": stats.get("category_distribution", {}),
            "types": registry.get_ml_types(),
            "total_categories": len(categories)
        }
    )
