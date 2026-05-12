from datetime import datetime, timezone

from app.core.database import get_mazes_collection
from app.repositories.base import BaseRepository


class MazeRepository(BaseRepository):

    def __init__(self):
        super().__init__(get_mazes_collection())

    # ------------------------------------------------------------------
    # Lookups
    # ------------------------------------------------------------------

    async def find_by_owner(
        self, owner_id: str, skip: int = 0, limit: int = 20
    ) -> list[dict]:
        """Return all mazes belonging to a user (published and drafts)."""
        # TODO:
        # return await self.find_many(
        #     {"owner_id": owner_id}, skip=skip, limit=limit
        # )
        return []

    async def find_published(
        self,
        skip: int = 0,
        limit: int = 20,
        sort_field: str = "created_at",
        tags: list[str] | None = None,
        search: str | None = None,
    ) -> list[dict]:
        """
        Return published mazes for the community gallery.
        Supports tag filtering and title search.
        """
        # TODO:
        # filter: dict = {"is_published": True}
        # if tags:
        #     filter["tags"] = {"$in": tags}
        # if search:
        #     filter["title"] = {"$regex": search, "$options": "i"}
        # return await self.find_many(filter, skip=skip, limit=limit, sort_field=sort_field)
        return []

    async def find_published_by_owner(self, owner_id: str) -> list[dict]:
        """Return only published mazes for a user's public profile."""
        # TODO:
        # return await self.find_many(
        #     {"owner_id": owner_id, "is_published": True}
        # )
        return []

    # ------------------------------------------------------------------
    # Writes
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
    ) -> str:
        """
        Insert a new maze document.
        Returns the new maze's ID as a string.
        """
        # TODO:
        # now = datetime.now(timezone.utc)
        # document = {
        #     "owner_id": owner_id,
        #     "title": title,
        #     "description": None,
        #     "grid": grid,
        #     "rows": rows,
        #     "cols": cols,
        #     "start": start,
        #     "end": end,
        #     "is_published": False,
        #     "tags": [],
        #     "play_count": 0,
        #     "created_at": now,
        #     "updated_at": now,
        # }
        # return await self.insert_one(document)
        return ""

    async def publish_maze(
        self, maze_id: str, title: str, description: str, tags: list[str]
    ) -> bool:
        """Publish a maze to the community gallery."""
        # TODO:
        # return await self.update_one(maze_id, {
        #     "is_published": True,
        #     "title": title,
        #     "description": description,
        #     "tags": tags,
        #     "updated_at": datetime.now(timezone.utc),
        # })
        return False

    async def increment_play_count(self, maze_id: str) -> None:
        """Increment play_count by 1 each time a maze is solved."""
        # TODO:
        # await self.collection.update_one(
        #     {"_id": self.to_object_id(maze_id)},
        #     {"$inc": {"play_count": 1}},
        # )
        pass