from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class LikeDocument(BaseModel):
    """
    Represents a like document as stored in MongoDB.

    One document per user+maze pair — the compound unique index
    on (user_id, maze_id) enforces this at the database level,
    preventing duplicate likes even under concurrent requests.
    """

    id: Optional[str] = Field(default=None, alias="_id")
    user_id: str        # references users._id
    maze_id: str        # references mazes._id
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
    }

    @staticmethod
    def indexes() -> list[dict]:
        """
        MongoDB indexes for the likes collection.

        Usage:
            for index in LikeDocument.indexes():
                await db["likes"].create_index(**index)
        """
        return [
            # Unique constraint: one like per user per maze
            {"keys": [("user_id", 1), ("maze_id", 1)], "unique": True},
            # Fast count of all likes on a specific maze
            {"keys": "maze_id"},
            # Fast lookup of everything a user has liked
            {"keys": "user_id"},
        ]