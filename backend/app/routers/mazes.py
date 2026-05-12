from fastapi import APIRouter, Depends, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database import get_db

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_maze(db: AsyncIOMotorDatabase = Depends(get_db)):
    """Create a new maze (auth required)."""
    # TODO: accept MazeCreate schema, insert into mazes collection, return MazeOut
    return {"message": "create maze — coming soon"}


@router.get("/mine")
async def get_my_mazes(db: AsyncIOMotorDatabase = Depends(get_db)):
    """Return all mazes belonging to the current user."""
    # TODO: query mazes by owner_id from JWT, return paginated list
    return {"message": "my mazes — coming soon"}


@router.get("/{maze_id}")
async def get_maze(maze_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    """Fetch a single maze by ID."""
    # TODO: find maze by _id, 404 if not found or not owner/published
    return {"message": f"get maze {maze_id} — coming soon"}


@router.put("/{maze_id}")
async def update_maze(maze_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    """Update maze grid, title, or metadata (auth + ownership required)."""
    # TODO: accept MazeUpdate schema, verify ownership, patch document
    return {"message": f"update maze {maze_id} — coming soon"}


@router.delete("/{maze_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_maze(maze_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    """Delete a maze (auth + ownership required)."""
    # TODO: verify ownership, delete document
    return None
