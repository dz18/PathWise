from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


# ------------------------------------------------------------------
# Request schemas (inbound)
# ------------------------------------------------------------------

class UserCreate(BaseModel):
    """Body for POST /auth/register"""
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)

    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not v.replace("_", "").replace("-", "").isalnum():
            raise ValueError("Username may only contain letters, numbers, hyphens, and underscores")
        return v.lower()

    @field_validator("email")
    @classmethod
    def email_lowercase(cls, v: str) -> str:
        return v.lower()


class UserLogin(BaseModel):
    """Body for POST /auth/login"""
    email: EmailStr
    password: str


# ------------------------------------------------------------------
# Response schemas (outbound)
# ------------------------------------------------------------------

class UserOut(BaseModel):
    """Safe public representation of a user — no password_hash."""
    id: str
    username: str
    email: str
    avatar_url: Optional[str] = None
    created_at: datetime


class Token(BaseModel):
    """Returned by POST /auth/login"""
    access_token: str
    token_type: str = "bearer"


class RegisterOut(BaseModel):
    """Returned by POST /auth/register"""
    id: str
    username: str
    message: str = "Account created successfully"