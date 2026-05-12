from fastapi import APIRouter, Depends, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database import get_db

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(db: AsyncIOMotorDatabase = Depends(get_db)):
    """Register a new user."""
    # TODO: accept UserCreate schema, hash password, insert into users collection
    return {"message": "register endpoint — coming soon"}


@router.post("/signin")
async def signin(db: AsyncIOMotorDatabase = Depends(get_db)):
    """Sign-In and return a JWT access token."""
    # TODO: verify credentials, return access + refresh token
    return {"message": "signin endpoint — coming soon"}


@router.get("/me")
async def get_me():
    """Return the currently authenticated user."""
    # TODO: decode JWT from Authorization header, return user profile
    return {"message": "me endpoint — coming soon"}
