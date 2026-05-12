from fastapi import APIRouter, Depends, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database import get_db

router = APIRouter()


@router.get("/mazes")
async def browse_mazes(db: AsyncIOMotorDatabase = Depends(get_db)):
    """
    Return a paginated list of published mazes.

    Query params will support:
        - page, limit
        - sort: "newest" | "most_liked" | "most_played"
        - tags: comma-separated filter
        - q: title search string
    """
    # TODO: query published mazes, apply filters/sort, return MazeFeed schema
    return {"message": "community maze feed — coming soon"}


@router.post("/{maze_id}/publish", status_code=status.HTTP_200_OK)
async def publish_maze(maze_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    """Publish a maze to the community gallery (auth + ownership required)."""
    # TODO: validate maze has start/end, is solvable, set is_published=True
    return {"message": f"publish maze {maze_id} — coming soon"}


@router.post("/{maze_id}/like", status_code=status.HTTP_200_OK)
async def toggle_like(maze_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    """Like or unlike a published maze (auth required)."""
    # TODO: upsert/delete like document, return updated like count
    return {"message": f"toggle like on maze {maze_id} — coming soon"}


@router.get("/{maze_id}/likes")
async def get_likes(maze_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    """Return the like count for a maze."""
    # TODO: count documents in likes collection for this maze_id
    return {"message": f"likes for maze {maze_id} — coming soon"}
