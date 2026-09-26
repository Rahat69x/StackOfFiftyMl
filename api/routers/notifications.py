"""
MLFORGE API — Notifications Router
Endpoints for real-time notification alerts and status tracking.
"""

from typing import Optional
from fastapi import APIRouter, Query, HTTPException
from core.notification_engine import notification_engine
from api.schemas.common import ResponseEnvelope

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("", response_model=ResponseEnvelope)
def get_notifications(
    unread_only: bool = Query(False),
    limit: int = Query(50, ge=1, le=100)
):
    """Returns platform notifications."""
    notifs = notification_engine.list_notifications(unread_only=unread_only, limit=limit)
    unread_count = sum(1 for n in notification_engine.notifications if not n.get("read"))
    return ResponseEnvelope(
        data=notifs,
        meta={"unread_count": unread_count, "total": len(notifs)}
    )


@router.post("/{notification_id}/read", response_model=ResponseEnvelope)
def mark_notification_read(notification_id: str):
    """Marks a single notification as read."""
    success = notification_engine.mark_as_read(notification_id)
    if not success:
        raise HTTPException(status_code=404, detail="Notification not found.")
    return ResponseEnvelope(data={"status": "marked_read", "id": notification_id})


@router.post("/read-all", response_model=ResponseEnvelope)
def mark_all_read():
    """Marks all notifications as read."""
    count = notification_engine.mark_all_as_read()
    return ResponseEnvelope(data={"status": "all_marked_read", "updated_count": count})
