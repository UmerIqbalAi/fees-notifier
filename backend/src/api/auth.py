"""Authentication endpoints."""
from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from src.services import auth_service

router = APIRouter()

class LoginRequest(BaseModel):
    password: str

@router.post("/login")
def login(request: LoginRequest, response: Response):
    """Admin login endpoint."""
    if not auth_service.validate_password(request.password):
        raise HTTPException(status_code=401, detail="Invalid admin password")
    
    # Set session cookie
    response.set_cookie(
        key="session",
        value="authenticated",
        httponly=True,
        samesite="lax",
        max_age=8 * 3600  # 8 hours
    )
    
    return {"message": "Login successful"}
