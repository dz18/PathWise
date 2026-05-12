from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ------------------------------------------------------------------
# Request schemas (inbound)
# ------------------------------------------------------------------


class MazeCreate(BaseModel):
    """Body for POST /mazes"""

    title: str = Field(..., min_length=1, max_length=100)
    grid: list[list[list[bool]]]  # grid[row][col] = [N, S, E, W]
    rows: int = Field(..., ge=3, le=50)
    cols: int = Field(..., ge=3, le=50)
    start: list[int] = Field(..., min_length=2, max_length=2)
    end: list[int] = Field(..., min_length=2, max_length=2)

    @field_validator("grid")
    @classmethod
    def grid_dimensions_match(cls, v: list, info) -> list:
        data = info.data
        rows = data.get("rows")
        cols = data.get("cols")
        if rows and len(v) != rows:
            raise ValueError(f"Grid has {len(v)} rows but rows={rows}")
        if cols and any(len(row) != cols for row in v):
            raise ValueError(
                "All grid rows must have the same number of columns as cols"
            )
        return v


class MazeUpdate(BaseModel):
    """Body for PUT /mazes/{id} — all fields optional"""

    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    grid: Optional[list[list[list[bool]]]] = None
    rows: Optional[int] = Field(default=None, ge=3, le=50)
    cols: Optional[int] = Field(default=None, ge=3, le=50)
    start: Optional[list[int]] = None
    end: Optional[list[int]] = None


class MazePublish(BaseModel):
    """Body for POST /community/{id}/publish"""

    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    tags: list[str] = Field(default_factory=list, max_length=10)

    @field_validator("tags")
    @classmethod
    def tags_lowercase(cls, v: list[str]) -> list[str]:
        return [tag.strip().lower() for tag in v if tag.strip()]


# ------------------------------------------------------------------
# Response schemas (outbound)
# ------------------------------------------------------------------


class MazeOut(BaseModel):
    """Full maze representation returned by the API."""

    id: str
    owner_id: str
    title: str
    description: Optional[str] = None
    grid: list[list[list[bool]]]
    rows: int
    cols: int
    start: list[int]
    end: list[int]
    is_published: bool
    tags: list[str]
    play_count: int
    created_at: datetime
    updated_at: datetime


class MazeSummary(BaseModel):
    """
    Lightweight maze card used in list/feed views.
    Omits the full grid to keep list responses small.
    """

    id: str
    owner_id: str
    title: str
    description: Optional[str] = None
    rows: int
    cols: int
    is_published: bool
    tags: list[str]
    play_count: int
    created_at: datetime
    updated_at: datetime
