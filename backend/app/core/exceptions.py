from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


# ------------------------------------------------------------------
# Custom exception classes
# ------------------------------------------------------------------

class NotFoundError(HTTPException):
    """Resource does not exist in the database."""
    def __init__(self, resource: str = "Resource"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} not found",
        )


class ForbiddenError(HTTPException):
    """Authenticated user does not have permission to perform this action."""
    def __init__(self, detail: str = "You do not have permission to perform this action"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )


class ConflictError(HTTPException):
    """Resource already exists (e.g. duplicate email or username)."""
    def __init__(self, detail: str = "Resource already exists"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
        )


class UnauthorizedError(HTTPException):
    """Missing or invalid authentication credentials."""
    def __init__(self, detail: str = "Authentication required"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class UnprocessableError(HTTPException):
    """Request is valid but cannot be processed (e.g. unsolvable maze)."""
    def __init__(self, detail: str = "Request cannot be processed"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
        )


class BadRequestError(HTTPException):
    """Malformed request or invalid input that passed schema validation."""
    def __init__(self, detail: str = "Bad request"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )


# ------------------------------------------------------------------
# Consistent error response shape
# ------------------------------------------------------------------

def error_response(status_code: int, detail: str) -> JSONResponse:
    """
    Return a consistent JSON error envelope:
        { "error": { "status": 404, "detail": "Maze not found" } }
    """
    return JSONResponse(
        status_code=status_code,
        content={"error": {"status": status_code, "detail": detail}},
    )


# ------------------------------------------------------------------
# Global exception handlers — register these in main.py
# ------------------------------------------------------------------

async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """Wrap all HTTPExceptions in the standard error envelope."""
    return error_response(exc.status_code, exc.detail)


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """
    Pydantic validation errors (422) — flatten the error list into
    a readable message instead of FastAPI's default nested structure.
    """
    errors = exc.errors()
    messages = []
    for err in errors:
        loc = " → ".join(str(l) for l in err["loc"] if l != "body")
        messages.append(f"{loc}: {err['msg']}" if loc else err["msg"])
    detail = "; ".join(messages)
    return error_response(status.HTTP_422_UNPROCESSABLE_ENTITY, detail)


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Catch-all for unexpected server errors — never expose stack traces."""
    return error_response(
        status.HTTP_500_INTERNAL_SERVER_ERROR,
        "An unexpected error occurred",
    )


# ------------------------------------------------------------------
# Registration helper — call this in main.py
# ------------------------------------------------------------------

def register_exception_handlers(app: FastAPI) -> None:
    """
    Attach all exception handlers to the FastAPI app instance.

    Call this in main.py after creating the app:
        from app.core.exceptions import register_exception_handlers
        register_exception_handlers(app)
    """
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)