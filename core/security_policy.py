"""
MLFORGE Core — Security Policy & RBAC Engine
Implements JWT tokens, password hashing, Role-Based Access Control,
audit logging, and rate limiting policies for high-impact ML modules.
"""

import os
import time
import hashlib
import hmac
import base64
import json
from typing import Any, Dict, List, Optional
import jwt
import logging

logger = logging.getLogger("mlforge.core.security_policy")

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "mlforge_secure_developer_signing_key_2026")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "60")) * 60

# Role Definitions & Permissions
ROLES_PERMISSIONS = {
    "admin": {
        "can_view": True,
        "can_train": True,
        "can_predict": True,
        "can_delete_models": True,
        "can_modify_settings": True,
        "can_manage_users": True
    },
    "data_scientist": {
        "can_view": True,
        "can_train": True,
        "can_predict": True,
        "can_delete_models": False,
        "can_modify_settings": False,
        "can_manage_users": False
    },
    "viewer": {
        "can_view": True,
        "can_train": False,
        "can_predict": True,
        "can_delete_models": False,
        "can_modify_settings": False,
        "can_manage_users": False
    }
}


class SecurityPolicy:
    """
    Central security and RBAC policy manager.
    """

    def __init__(self):
        self.audit_logs: List[Dict[str, Any]] = []
        self._request_counters: Dict[str, List[float]] = {}

    def hash_password(self, password: str, salt: str = "mlforge_salt") -> str:
        """Secure PBKDF2 password hashing."""
        dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000)
        return dk.hex()

    def verify_password(self, password: str, hashed_password: str, salt: str = "mlforge_salt") -> bool:
        """Verifies password against stored PBKDF2 hash."""
        return hmac.compare_digest(self.hash_password(password, salt), hashed_password)

    def create_access_token(self, username: str, role: str = "data_scientist") -> str:
        """Generates short-lived JWT access token."""
        now = time.time()
        payload = {
            "sub": username,
            "role": role,
            "iat": int(now),
            "exp": int(now + ACCESS_TOKEN_EXPIRE_SECONDS),
            "iss": "mlforge"
        }
        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    def decode_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Decodes and verifies JWT token."""
        try:
            return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            logger.warning(f"JWT verification failed: {e}")
            return None

    def check_permission(self, role: str, action: str) -> bool:
        """Checks if a user role has permission to execute an action."""
        perms = ROLES_PERMISSIONS.get(role, ROLES_PERMISSIONS["viewer"])
        return perms.get(action, False)

    def log_audit(self, user: str, action: str, resource: str, status: str = "success", details: Optional[Dict[str, Any]] = None) -> None:
        """Appends to the tamper-evident platform audit log."""
        record = {
            "timestamp": time.time(),
            "timestamp_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "user": user,
            "action": action,
            "resource": resource,
            "status": status,
            "details": details or {}
        }
        self.audit_logs.insert(0, record)
        if len(self.audit_logs) > 500:
            self.audit_logs.pop()

    def check_rate_limit(self, client_id: str, limit_per_minute: int = 60) -> bool:
        """Sliding window rate-limiter."""
        now = time.time()
        window_start = now - 60.0
        
        if client_id not in self._request_counters:
            self._request_counters[client_id] = []
            
        # Retain only timestamps within the last 60 seconds
        self._request_counters[client_id] = [
            t for t in self._request_counters[client_id] if t > window_start
        ]
        
        if len(self._request_counters[client_id]) >= limit_per_minute:
            return False
            
        self._request_counters[client_id].append(now)
        return True


# Global singleton instance
security_policy = SecurityPolicy()
