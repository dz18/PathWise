from datetime import datetime, timezone

from app.core.database import get_users_collection
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self):
        super().__init__(get_users_collection())

    # ------------------------------------------------------------------
    # Lookups
    # ------------------------------------------------------------------

    async def find_by_email(self, email: str) -> dict | None:
        """Find a user by email address (used during login)."""
        # TODO: return await self.find_one({"email": email.lower()})
        return None

    async def find_by_username(self, username: str) -> dict | None:
        """Find a user by username (used for public profile pages)."""
        # TODO: return await self.find_one({"username": username})
        return None

    async def email_exists(self, email: str) -> bool:
        """Check if an email is already registered (used during registration)."""
        # TODO: return await self.exists({"email": email.lower()})
        return False

    async def username_exists(self, username: str) -> bool:
        """Check if a username is already taken."""
        # TODO: return await self.exists({"username": username})
        return False

    # ------------------------------------------------------------------
    # Writes
    # ------------------------------------------------------------------

    async def create_user(
        self, username: str, email: str, password_hash: str
    ) -> str:
        """
        Insert a new user document.
        Returns the new user's ID as a string.
        """
        # TODO:
        # document = {
        #     "username": username,
        #     "email": email.lower(),
        #     "password_hash": password_hash,
        #     "avatar_url": None,
        #     "created_at": datetime.now(timezone.utc),
        # }
        # return await self.insert_one(document)
        return ""

    async def update_avatar(self, user_id: str, avatar_url: str) -> bool:
        """Update a user's avatar URL."""
        # TODO: return await self.update_one(user_id, {"avatar_url": avatar_url})
        return False