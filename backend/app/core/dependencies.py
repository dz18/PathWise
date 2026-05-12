from fastapi import Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database import get_db
from app.core.security import get_current_user
from app.repositories.user_repo import UserRepository


# ------------------------------------------------------------------
# Database
# ------------------------------------------------------------------

async def get_database(
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> AsyncIOMotorDatabase:
    """
    Yields the active MongoDB database instance.

    Usage:
        async def my_route(db: AsyncIOMotorDatabase = Depends(get_database)):
            ...
    """
    return db


# ------------------------------------------------------------------
# Auth — current user (required)
# ------------------------------------------------------------------

async def require_auth(
    current_user: dict = Depends(get_current_user),
) -> dict:
    """
    Require a valid JWT. Returns the decoded user payload.
    Raises 401 if no token or token is invalid.

    Usage:
        async def my_route(user: dict = Depends(require_auth)):
            user["id"]       # MongoDB user _id as string
            user["username"] # username from token
    """
    return current_user


# ------------------------------------------------------------------
# Auth — current user with full DB profile
# ------------------------------------------------------------------

async def require_auth_user(
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> dict:
    """
    Require auth AND fetch the full user document from MongoDB.
    Use this when you need fields beyond id and username (e.g. avatar_url).
    Raises 401 if unauthenticated, 404 if user no longer exists in DB.

    Usage:
        async def my_route(user: dict = Depends(require_auth_user)):
            user["email"]
            user["avatar_url"]
    """
    repo = UserRepository()
    user = await repo.find_by_id(current_user["id"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Authenticated user no longer exists",
        )
    user.pop("password_hash", None)
    return user


# ------------------------------------------------------------------
# Auth — optional (public routes that behave differently when logged in)
# ------------------------------------------------------------------

async def optional_auth(
    current_user: dict | None = Depends(get_current_user),
) -> dict | None:
    """
    Attempt to decode the JWT but do NOT raise if missing or invalid.
    Returns the user payload if authenticated, None otherwise.

    Usage:
        async def my_route(user: dict | None = Depends(optional_auth)):
            if user:
                # personalise response
            else:
                # return generic response
    """
    try:
        return current_user
    except HTTPException:
        return None


# ------------------------------------------------------------------
# Pagination
# ------------------------------------------------------------------

async def pagination_params(
    page: int = 1,
    limit: int = 20,
) -> dict:
    """
    Common pagination query params injected into list endpoints.
    Clamps limit to a max of 50 to prevent abusive large queries.

    Usage:
        async def my_route(pagination: dict = Depends(pagination_params)):
            pagination["skip"]
            pagination["limit"]
            pagination["page"]
    """
    if page < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Page must be 1 or greater",
        )
    limit = min(limit, 50)  # hard cap
    skip = (page - 1) * limit
    return {"page": page, "limit": limit, "skip": skip}