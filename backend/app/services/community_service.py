from fastapi import HTTPException, status

from app.repositories.maze_repo import MazeRepository
from app.repositories.like_repo import LikeRepository
from app.algorithms.bfs import BFSSolver


class CommunityService:
    """
    Handles publishing, browsing, and liking mazes in the community gallery.
    """

    def __init__(self):
        self.maze_repo = MazeRepository()
        self.like_repo = LikeRepository()

    # ------------------------------------------------------------------
    # Browse
    # ------------------------------------------------------------------

    async def get_feed(
        self,
        skip: int = 0,
        limit: int = 20,
        sort: str = "newest",
        tags: list[str] | None = None,
        search: str | None = None,
    ) -> list[dict]:
        """
        Return a paginated feed of published mazes.
        sort options: "newest" | "most_liked" | "most_played"
        """
        # TODO:
        # sort_field_map = {
        #     "newest": "created_at",
        #     "most_liked": "like_count",   # denormalised field updated on like/unlike
        #     "most_played": "play_count",
        # }
        # sort_field = sort_field_map.get(sort, "created_at")
        # return await self.maze_repo.find_published(
        #     skip=skip, limit=limit, sort_field=sort_field, tags=tags, search=search
        # )
        return []

    # ------------------------------------------------------------------
    # Publish
    # ------------------------------------------------------------------

    async def publish_maze(
        self,
        maze_id: str,
        owner_id: str,
        title: str,
        description: str,
        tags: list[str],
    ) -> dict:
        """
        Publish a maze to the community gallery.
        Validates ownership, start/end presence, and solvability before publishing.
        """
        # TODO:
        # --- Ownership check ---
        # maze = await self.maze_repo.find_by_id(maze_id)
        # if not maze:
        #     raise HTTPException(status_code=404, detail="Maze not found")
        # if maze["owner_id"] != owner_id:
        #     raise HTTPException(status_code=403, detail="You do not own this maze")

        # --- Validate start / end ---
        # if not maze.get("start") or not maze.get("end"):
        #     raise HTTPException(status_code=422, detail="Maze must have a start and end before publishing")

        # --- Solvability check (BFS is fast and guaranteed correct) ---
        # solver = BFSSolver(
        #     grid=maze["grid"],
        #     start=tuple(maze["start"]),
        #     end=tuple(maze["end"]),
        # )
        # result = solver.solve()
        # if not result.path:
        #     raise HTTPException(status_code=422, detail="Maze has no valid solution — fix the maze before publishing")

        # --- Publish ---
        # await self.maze_repo.publish_maze(maze_id, title, description, tags)
        # return await self.maze_repo.find_by_id(maze_id)
        return {}

    # ------------------------------------------------------------------
    # Likes
    # ------------------------------------------------------------------

    async def toggle_like(self, maze_id: str, user_id: str) -> dict:
        """
        Like or unlike a maze.
        Returns the new like state and updated count.
        Raises 404 if the maze doesn't exist or isn't published.
        """
        # TODO:
        # maze = await self.maze_repo.find_by_id(maze_id)
        # if not maze or not maze["is_published"]:
        #     raise HTTPException(status_code=404, detail="Maze not found")
        # return await self.like_repo.toggle_like(user_id, maze_id)
        return {"liked": False, "count": 0}

    async def get_like_count(self, maze_id: str) -> dict:
        """Return the total like count for a maze."""
        # TODO:
        # count = await self.like_repo.count_likes(maze_id)
        # return {"maze_id": maze_id, "count": count}
        return {"maze_id": maze_id, "count": 0}