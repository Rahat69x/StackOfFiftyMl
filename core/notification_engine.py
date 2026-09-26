"""
MLFORGE Core — Shared Notification Engine
Delivers real-time status alerts for completed training runs, evaluations,
model drift warnings, and system events.
"""

import time
import uuid
from typing import Any, Dict, List, Optional
import logging

logger = logging.getLogger("mlforge.core.notification_engine")


class NotificationEngine:
    """
    In-memory and persistent notification buffer for MLFORGE events.
    """

    def __init__(self):
        self.notifications: List[Dict[str, Any]] = [
            {
                "id": f"notif_{uuid.uuid4().hex[:6]}",
                "title": "MLFORGE System Initialized",
                "message": "Platform ready with all 50 machine learning project modules registered.",
                "type": "info",
                "timestamp": time.time(),
                "timestamp_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "read": False,
                "project_id": "SYSTEM"
            }
        ]

    def emit(
        self,
        title: str,
        message: str,
        notif_type: str = "info",
        project_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Emits a new user notification."""
        notif = {
            "id": f"notif_{uuid.uuid4().hex[:8]}",
            "title": title,
            "message": message,
            "type": notif_type,  # 'info' | 'success' | 'warning' | 'error'
            "timestamp": time.time(),
            "timestamp_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "read": False,
            "project_id": project_id or "SYSTEM",
            "metadata": metadata or {}
        }
        self.notifications.insert(0, notif)
        if len(self.notifications) > 200:
            self.notifications.pop()
        logger.info(f"Notification emitted [{notif_type.upper()}]: {title}")
        return notif

    def list_notifications(self, unread_only: bool = False, limit: int = 50) -> List[Dict[str, Any]]:
        """Lists notifications with optional filtering."""
        items = [n for n in self.notifications if not (unread_only and n.get("read"))]
        return items[:limit]

    def mark_as_read(self, notif_id: str) -> bool:
        """Marks a notification as read."""
        for n in self.notifications:
            if n["id"] == notif_id:
                n["read"] = True
                return True
        return False

    def mark_all_as_read(self) -> int:
        """Marks all notifications as read."""
        count = 0
        for n in self.notifications:
            if not n["read"]:
                n["read"] = True
                count += 1
        return count


# Global singleton instance
notification_engine = NotificationEngine()
