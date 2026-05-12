from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    All config is read from environment variables (or .env in development).
    Pydantic validates types and raises a clear error on startup if anything
    required is missing.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    # --- MongoDB ----------------------------------------------------------------
    MONGO_URI: str
    MONGO_DB_NAME: str

    # --- Collection Names -------------------------------------------------------
    COLLECTION_USERS: str = "users"
    COLLECTION_MAZES: str = "mazes"
    COLLECTION_LIKES: str = "likes"

    # --- Authentication ---------------------------------------------------------
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # --- CORS -------------------------------------------------------------------
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    # --- App --------------------------------------------------------------------
    ENV: str = "dev"  # "development" | "production"
    DEBUG: bool = True


settings = Settings() # type: ignore[call-arg]
