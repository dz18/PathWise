from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserDocument(BaseModel):
    """
    Represents a user document as stored in MongoDB.
    This is the internal model — never expose password_hash to the API.
    """

    id: Optional[str] = Field(default=None, alias="_id")
    username: str
    email: EmailStr
    password_hash: str
    avatar_url: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {
        "populate_by_name": True,  # allow both "id" and "_id"
        "arbitrary_types_allowed": True,
    }

    @staticmethod
    def indexes() -> list[dict]:
        """
        MongoDB indexes to create on startup or migration.

        Usage in database setup:
            for index in UserDocument.indexes():
                await db["users"].create_index(**index)
        """
        return [
            # Unique email — prevents duplicate registrations
            {"keys": "email", "unique": True},
            # Unique username — prevents duplicate handles
            {"keys": "username", "unique": True},
        ]
