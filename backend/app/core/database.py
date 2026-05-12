from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings


# ----------------------------------------------------------------------------------------
# Module-level Client: One instance for the entire process lifetime
# ----------------------------------------------------------------------------------------

_client: AsyncIOMotorClient | None = None


def get_client() -> AsyncIOMotorClient:
    """ Return the active Motor client. Raises if called before connect_db(). """
    if _client is None:
        raise RuntimeError("Database not initialised. Call connect_db() first.")
    return _client


def get_db() -> AsyncIOMotorDatabase:
    """
    FastAPI dependency — inject this into any route or service that needs the DB.
 
    Usage:
        async def my_route(db: AsyncIOMotorDatabase = Depends(get_db)):
            ...
    """
    return get_client()[settings.MONGO_DB_NAME]


# ----------------------------------------------------------------------------------------
# Lifecycle helpers - called from main.py lifespan
# ----------------------------------------------------------------------------------------

async def connect_db() -> None:
    """ Open the Motor connection pool and verify the server is reachable """
    global _client

    _client = AsyncIOMotorClient(
        settings.MONGO_URI,
        maxPoolSize=10,
        minPoolSize=1,
        serverSelectionTimeoutMS=5_000,
        connectTimeoutMS=5_000
    )

    await _client.admin.command("ping")


async def close_db() -> None:
    """Close the Motor connection pool on shutdown."""
    global _client
    if _client is not None:
        _client.close()
        _client = None


# ---------------------------------------------------------------------------
# Collection helpers — typed shortcuts used by repositories
# ---------------------------------------------------------------------------

def get_users_collection():
    return get_db()[settings.COLLECTION_USERS]
 

def get_mazes_collection():
    return get_db()[settings.COLLECTION_MAZES]
 

def get_likes_collection():
    return get_db()[settings.COLLECTION_LIKES]

