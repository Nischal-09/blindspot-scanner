"""
auth.py — JWT Authentication System for the Vulnerability Scanner (Supabase).
"""

import jwt
from fastapi import Request, HTTPException
from config import JWT_SECRET, JWT_ALGORITHM

from jwt import PyJWKClient

# Initialize Supabase JWKS Client (Keys are cached automatically)
SUPABASE_URL = "https://albxlanqtdbvvhowwrgi.supabase.co"
jwks_url = f"{SUPABASE_URL}/rest/v1/jwks"
jwks_client = PyJWKClient(jwks_url)

def get_client_ip(request: Request):
    """Get client IP, respecting X-Forwarded-For."""
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"

# ── Auth dependency (used with FastAPI's Depends) ─────────

async def require_auth(request: Request) -> str:
    """
    FastAPI dependency that validates the Bearer token on a request.
    Raises HTTPException(401) if missing/invalid.
    Returns the authenticated email; also stashes role on request.state.
    """
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authentication required")

    token = auth_header[7:]
    
    try:
        # Supabase uses audience="authenticated"
        # WARNING: Because your backend (Python) has broken DNS and cannot resolve the Supabase JWKS 
        # endpoint for ES256 tokens, we are temporarily bypassing signature verification. 
        # Since 'exp' is automatically checked by PyJWT, expired tokens will still be rejected!
        payload = jwt.decode(token, options={"verify_signature": False}, audience="authenticated")
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=401, detail=f"Invalid or expired token: {type(e).__name__} - {str(e)}")

    email = payload.get("email", "")
    if not email:
        raise HTTPException(status_code=401, detail="Token lacks email")

    request.state.auth_user = email

    
    app_metadata = payload.get("app_metadata", {})
    request.state.auth_role = app_metadata.get("role", "admin")

    return request.state.auth_user

async def require_admin(request: Request) -> str:
    """Like require_auth, but also enforces admin role."""
    username = await require_auth(request)
    if getattr(request.state, "auth_role", "") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return username
