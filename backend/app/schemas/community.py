from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas.maze import MazeSummary


# ------------------------------------------------------------------
# Feed / browse
# ------------------------------------------------------------------


class MazeFeedItem(MazeSummary):
    """
    A maze card in the community gallery.
    Extends MazeSummary with community-specific fields.
    """

    like_count: int = 0
    author_username: str


class MazeFeed(BaseModel):
    """Paginated response for GET /community/mazes"""

    items: list[MazeFeedItem]
    total: int
    page: int
    limit: int
    has_more: bool


# ------------------------------------------------------------------
# Likes
# ------------------------------------------------------------------


class LikeOut(BaseModel):
    """Returned by POST /community/{id}/like"""

    maze_id: str
    liked: bool  # True = user just liked, False = user just unliked
    count: int  # updated total like count


class LikeCount(BaseModel):
    """Returned by GET /community/{id}/likes"""

    maze_id: str
    count: int


# ------------------------------------------------------------------
# User profile
# ------------------------------------------------------------------


class UserProfile(BaseModel):
    """Returned by GET /profile/{username}"""

    id: str
    username: str
    avatar_url: Optional[str] = None
    joined: datetime
    published_mazes: list[MazeSummary]
    total_likes_received: int
