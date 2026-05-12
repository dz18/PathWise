from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection


class BaseRepository:
    """
    Shared asycn CRUD helpers inherited by all repositories.
    Each subclass passes in its collection on instantiation.
    """

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def to_object_id(id: str) -> ObjectId:
        """Convert a string ID to ObjectId, raising ValueError if invalid"""

        try:
            return ObjectId(id)
        except Exception:
            raise ValueError(f"Invalid ObjectId: {id}")

    @staticmethod
    def serialize(document: dict) -> dict:
        """Convert ObjectId to strings for JSON serialization."""

        if document and "_id" in document:
            document["id"] = str(document.pop("_id"))
        return document

    # ------------------------------------------------------------------
    # Core Operations
    # ------------------------------------------------------------------

    async def find_by_id(self, id: str) -> dict | None:
        """Find a single document by its _id. Return None if not found."""
        doc = await self.collection.find_one({"_id": self.to_object_id(id)})
        return self.serialize(doc) if doc else None

    async def find_one(self, filter: dict) -> dict | None:
        """Find a single document matching the filter"""
        doc = await self.collection.find_one(filter)
        return self.serialize(doc) if doc else None

    async def find_many(
        self,
        filter: dict,
        skip: int = 0,
        limit: int = 20,
        sort_field: str = "created_at",
        sort_order: int = -1,  # -1 = descending, 1 = ascending
    ) -> list[dict]:
        """Find multiple documents with optional pagination and sorting"""
        cursor = (
            self.collection.find(filter)
            .sort(sort_field, sort_order)
            .skip(skip)
            .limit(limit)
        )

        docs = cursor.to_list(length=limit)
        return [self.serialize(doc) for doc in docs]

    async def insert_one(self, document: dict) -> str:
        """Insert a document and return the new_id as a string."""
        result = await self.collection.insert_one(document)
        return str(result.inserted_id)

    async def update_one(self, id: str, update: dict) -> bool:
        """
        Partially updates a document by _id using $set.
        Returns True if a document was modified.
        """
        result = await self.collection.update_one(
            {"_id": self.to_object_id(id)}, {"$set": update}
        )
        return result.modified_count > 0

    async def delete_one(self, id: str) -> bool:
        """Delete a document by _id. Returns True if deleted."""
        result = await self.collection.delete_one({"_id": self.to_object_id(id)})
        return result.deleted_count > 0

    async def count(self, filter: dict) -> int:
        """Count documents matching a filter."""
        return await self.collection.count_documents(filter)

    async def exists(self, filter: dict) -> bool:
        """Return True if at least one document matches the filter."""
        doc = await self.collection.find_one(filter, {"_id": 1})
        return doc is not None
