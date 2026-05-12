from app.core.database import get_likes_collection
from app.repositories.base import BaseRepository


class LikeRepository(BaseRepository):
    def __init__(self):
        super().__init__(get_likes_collection())

    # ------------------------------------------------------------------
    # Lookups
    # ------------------------------------------------------------------

    async def has_liked(self, user_id: str, maze_id: str) -> bool:
        """Check if a user has already liked a specific maze."""
        # TODO:
        # return await self.exists({"user_id": user_id, "maze_id": maze_id})
        return False

    async def count_likes(self, maze_id: str) -> int:
        """Return the total number of likes for a maze."""
        # TODO: return await self.count({"maze_id": maze_id})
        return 0

    async def total_likes_received(self, owner_id: str, maze_ids: list[str]) -> int:
        """
        Sum all likes across a user's published mazes.
        Used for displaying total likes on a public profile.
        """
        # TODO: return await self.count({"maze_id": {"$in": maze_ids}})
        return 0

    # ------------------------------------------------------------------
    # Writes
    # ------------------------------------------------------------------

    async def like(self, user_id: str, maze_id: str) -> bool:
        """
        Like a maze. Silently no-ops if already liked.
        Returns True if a new like was created.
        """
        # TODO:
        # already_liked = await self.has_liked(user_id, maze_id)
        # if already_liked:
        #     return False
        # await self.insert_one({
        #     "user_id": user_id,
        #     "maze_id": maze_id,
        #     "created_at": datetime.now(timezone.utc),
        # })
        # return True
        return False

    async def unlike(self, user_id: str, maze_id: str) -> bool:
        """
        Unlike a maze. Returns True if a like was removed.
        """
        # TODO:
        # result = await self.collection.delete_one(
        #     {"user_id": user_id, "maze_id": maze_id}
        # )
        # return result.deleted_count > 0
        return False

    async def toggle_like(self, user_id: str, maze_id: str) -> dict:
        """
        Like if not liked, unlike if already liked.
        Returns the new like state and updated count.
        """
        # TODO:
        # if await self.has_liked(user_id, maze_id):
        #     await self.unlike(user_id, maze_id)
        #     liked = False
        # else:
        #     await self.like(user_id, maze_id)
        #     liked = True
        # count = await self.count_likes(maze_id)
        # return {"liked": liked, "count": count}
        return {"liked": False, "count": 0}
