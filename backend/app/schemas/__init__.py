from app.schemas.user import UserCreate, UserLogin, UserOut, Token, RegisterOut
from app.schemas.maze import MazeCreate, MazeUpdate, MazePublish, MazeOut, MazeSummary
from app.schemas.solver import SolveRequest, SolveResult
from app.schemas.community import (
    MazeFeedItem,
    MazeFeed,
    LikeOut,
    LikeCount,
    UserProfile,
)

__all__ = [
    # User
    "UserCreate",
    "UserLogin",
    "UserOut",
    "Token",
    "RegisterOut",
    # Maze
    "MazeCreate",
    "MazeUpdate",
    "MazePublish",
    "MazeOut",
    "MazeSummary",
    # Solver
    "SolveRequest",
    "SolveResult",
    # Community
    "MazeFeedItem",
    "MazeFeed",
    "LikeOut",
    "LikeCount",
    "UserProfile",
]
