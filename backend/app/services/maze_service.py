from datetime import datetime, timezone

from fastapi import HTTPException, status

from app.repositories.maze_repo import MazeRepository


class MazeService:
    """
    Handles all maze CRUD business logic.
    Enforces ownership rules — a user can only edit or delete their own mazes.
    """

    def __init__(self):
        self.maze_repo = MazeRepository()

    # ------------------------------------------------------------------
    # Fetch
    # ------------------------------------------------------------------

    async def get_maze(self, maze_id: str, requesting_user_id: str | None = None) -> dict:
        """
        Fetch a maze by ID.
        - Published mazes are visible to anyone.
        - Draft mazes are only visible to the owner.
        Raises 404 if not found, 403 if a draft is accessed by a non-owner.
        """
        # TODO:
        # maze = await self.maze_repo.find_by_id(maze_id)
        # if not maze:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Maze not found")
        # if not maze["is_published"] and maze["owner_id"] != requesting_user_id:
        #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
        # return maze
        return {}

    async def get_my_mazes(
        self, owner_id: str, skip: int = 0, limit: int = 20
    ) -> list[dict]:
        """Return all mazes (drafts + published) for the current user."""
        # TODO: return await self.maze_repo.find_by_owner(owner_id, skip=skip, limit=limit)
        return []

    # ------------------------------------------------------------------
    # Create
    # ------------------------------------------------------------------

    async def create_maze(
        self,
        owner_id: str,
        title: str,
        grid: list,
        rows: int,
        cols: int,
        start: list[int],
        end: list[int],
    ) -> dict:
        """
        Create a new draft maze.
        Validates that start and end positions are within bounds.
        """
        # TODO:
        # if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        #     raise HTTPException(status_code=400, detail="Start position out of bounds")
        # if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        #     raise HTTPException(status_code=400, detail="End position out of bounds")
        # if start == end:
        #     raise HTTPException(status_code=400, detail="Start and end cannot be the same cell")
        # maze_id = await self.maze_repo.create_maze(
        #     owner_id, title, grid, rows, cols, start, end
        # )
        # return await self.maze_repo.find_by_id(maze_id)
        return {}

    # ------------------------------------------------------------------
    # Update
    # ------------------------------------------------------------------

    async def update_maze(
        self, maze_id: str, owner_id: str, update_data: dict
    ) -> dict:
        """
        Update maze fields. Only the owner can update.
        Raises 403 if the requesting user is not the owner.
        """
        # TODO:
        # maze = await self.maze_repo.find_by_id(maze_id)
        # if not maze:
        #     raise HTTPException(status_code=404, detail="Maze not found")
        # if maze["owner_id"] != owner_id:
        #     raise HTTPException(status_code=403, detail="You do not own this maze")
        # update_data["updated_at"] = datetime.now(timezone.utc)
        # await self.maze_repo.update_one(maze_id, update_data)
        # return await self.maze_repo.find_by_id(maze_id)
        return {}

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------

    async def delete_maze(self, maze_id: str, owner_id: str) -> None:
        """
        Delete a maze. Only the owner can delete.
        Raises 403 if the requesting user is not the owner.
        """
        # TODO:
        # maze = await self.maze_repo.find_by_id(maze_id)
        # if not maze:
        #     raise HTTPException(status_code=404, detail="Maze not found")
        # if maze["owner_id"] != owner_id:
        #     raise HTTPException(status_code=403, detail="You do not own this maze")
        # await self.maze_repo.delete_one(maze_id)
        pass