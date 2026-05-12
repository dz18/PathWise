from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


# A cell is represented as a list of 4 booleans: [north, south, east, west]
# True = wall exists on that side, False = open passage
Cell = list[bool]

# The grid is a 2D array of cells: grid[row][col]
Grid = list[list[Cell]]


class MazeDocument(BaseModel):
    """
    Represents a maze document as stored in MongoDB.

    Grid format:
        Each cell stores its 4 walls as booleans [N, S, E, W].
        Example 3x3 grid cell with all walls closed:
            grid[0][0] = [True, True, True, True]
        A cell with only the east wall open:
            grid[0][0] = [True, True, False, True]

    Start / end:
        Stored as [row, col] — e.g. start = [0, 0], end = [4, 4]
    """

    id: Optional[str] = Field(default=None, alias="_id")
    owner_id: str  # references users._id
    title: str
    description: Optional[str] = None

    # Grid data
    grid: Grid  # 2D array of cells
    rows: int
    cols: int
    start: list[int]  # [row, col]
    end: list[int]  # [row, col]

    # Community
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)
    play_count: int = 0

    # Timestamps
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
    }

    @staticmethod
    def indexes() -> list[dict]:
        """
        MongoDB indexes for the mazes collection.

        Usage:
            for index in MazeDocument.indexes():
                await db["mazes"].create_index(**index)
        """
        return [
            # Fast lookup of all mazes by a specific owner
            {"keys": "owner_id"},
            # Community gallery: filter published + sort by date
            {"keys": [("is_published", 1), ("created_at", -1)]},
            # Community gallery: filter published + sort by play count
            {"keys": [("is_published", 1), ("play_count", -1)]},
            # Tag filtering on the gallery
            {"keys": "tags"},
            # Text search on title and description
            {"keys": [("title", "text"), ("description", "text")]},
        ]
