from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.auth_schema import LoginRequest, Token
from app.models.user_model import user_collection
from app.auth_utils import verify_password, create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/login", response_model=Token)
def login(login_data: LoginRequest):
    user = user_collection.find_one({"email": login_data.email})
    if not user or not verify_password(login_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    
    access_token = create_access_token(
        data={"sub": user["email"], "role": user["role"]}
    )
    return {
        "access_token": access_token, 
        "token_type": "bearer", 
        "role": user["role"]
    }
