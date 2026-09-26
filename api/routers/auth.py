"""
MLFORGE API — Authentication Router
Endpoints for user authentication, JWT issuance, and RBAC profile queries.
"""

from fastapi import APIRouter, HTTPException, Depends
from core.security_policy import security_policy, ROLES_PERMISSIONS
from api.schemas.common import ResponseEnvelope, LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Built-in demo accounts for instant local login
DEMO_ACCOUNTS = {
    "admin": {"password": "adminpassword", "role": "admin", "email": "admin@mlforge.internal"},
    "datascientist": {"password": "dspassword", "role": "data_scientist", "email": "scientist@mlforge.internal"},
    "viewer": {"password": "viewerpassword", "role": "viewer", "email": "viewer@mlforge.internal"}
}


@router.post("/login", response_model=ResponseEnvelope)
def login(req: LoginRequest):
    """Logs in and returns a JWT access token."""
    account = DEMO_ACCOUNTS.get(req.username.lower())
    if not account or account["password"] != req.password:
        security_policy.log_audit(req.username, "login_attempt", "auth", status="failed")
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    token = security_policy.create_access_token(req.username, role=account["role"])
    security_policy.log_audit(req.username, "login_success", "auth", status="success")

    return ResponseEnvelope(
        data={
            "access_token": token,
            "token_type": "bearer",
            "username": req.username,
            "role": account["role"],
            "permissions": ROLES_PERMISSIONS.get(account["role"], {})
        }
    )


@router.get("/me", response_model=ResponseEnvelope)
def get_current_user_profile(username: str = "datascientist"):
    """Returns current user's profile and active permissions."""
    account = DEMO_ACCOUNTS.get(username.lower(), DEMO_ACCOUNTS["viewer"])
    return ResponseEnvelope(
        data={
            "username": username,
            "role": account["role"],
            "email": account["email"],
            "permissions": ROLES_PERMISSIONS.get(account["role"], {})
        }
    )
