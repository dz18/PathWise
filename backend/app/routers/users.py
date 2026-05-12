from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database import get_db

router = APIRouter()


@router.get("/{username}")
async def get_profile(username: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    """
    Public profile page for a user.

    Returns:
        - username, avatar_url, join date
        - all published mazes by this user
        - total likes received across all mazes
    """
    # TODO: find user by username, 404 if not found
    # TODO: fetch published mazes by owner_id, sum likes
    return {"message": f"profile for {username} — coming soon"}