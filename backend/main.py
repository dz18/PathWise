from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import connect_db, close_db
from app.core.exceptions import register_exception_handlers
from app.routers import auth, mazes, solver, community, users


# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: open MongoDB connection pool
    await connect_db()
    print(f"Connected to MongoDB at {settings.MONGO_URI}")
    yield
    # Shutdown: close the connection pool cleanly
    await close_db()
    print("MongoDB connection closed")


# App Factory
app = FastAPI(
    title="PathWise",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

register_exception_handlers(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # e.g. ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(mazes.router, prefix="/mazes", tags=["mazes"])
app.include_router(solver.router, prefix="/mazes", tags=["solver"])
app.include_router(community.router, prefix="/community", tags=["community"])
app.include_router(users.router, prefix="/profile", tags=["users"])


# Health check
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok", "version": app.version}
