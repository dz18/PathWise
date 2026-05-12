from app.repositories.user_repo import UserRepository


class AuthService:
    """
    Handles all authentication business logic.
    Calls UserRepository for DB access, core/security for JWT + hashing.
    """

    def __init__(self):
        self.user_repo = UserRepository()

    # ------------------------------------------------------------------
    # Register
    # ------------------------------------------------------------------

    async def register(self, username: str, email: str, password: str) -> dict:
        """
        Register a new user.
        Raises 409 if email or username is already taken.
        Returns the created user's ID and username.
        """
        # TODO:
        # if await self.user_repo.email_exists(email):
        #     raise HTTPException(
        #         status_code=status.HTTP_409_CONFLICT,
        #         detail="Email is already registered",
        #     )
        # if await self.user_repo.username_exists(username):
        #     raise HTTPException(
        #         status_code=status.HTTP_409_CONFLICT,
        #         detail="Username is already taken",
        #     )
        # password_hash = hash_password(password)
        # user_id = await self.user_repo.create_user(username, email, password_hash)
        # return {"id": user_id, "username": username}
        return {}

    # ------------------------------------------------------------------
    # Login
    # ------------------------------------------------------------------

    async def login(self, email: str, password: str) -> dict:
        """
        Verify credentials and return a signed JWT access token.
        Raises 401 if email not found or password is wrong.
        """
        # TODO:
        # user = await self.user_repo.find_by_email(email)
        # if not user:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Invalid email or password",
        #     )
        # if not verify_password(password, user["password_hash"]):
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Invalid email or password",
        #     )
        # token = create_access_token({"sub": user["id"], "username": user["username"]})
        # return {"access_token": token, "token_type": "bearer"}
        return {}

    # ------------------------------------------------------------------
    # Get current user
    # ------------------------------------------------------------------

    async def get_current_user(self, user_id: str) -> dict:
        """
        Fetch the authenticated user's profile by their ID (decoded from JWT).
        Raises 404 if the user no longer exists.
        """
        # TODO:
        # user = await self.user_repo.find_by_id(user_id)
        # if not user:
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND,
        #         detail="User not found",
        #     )
        # # Strip password_hash before returning
        # user.pop("password_hash", None)
        # return user
        return {}
