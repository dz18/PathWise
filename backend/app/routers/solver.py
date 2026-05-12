from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.database import get_db

router = APIRouter()


@router.post("/{maze_id}/solve")
async def solve_maze(maze_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    """
    Run a pathfinding algorithm on a maze and return the solution.

    Request body will accept:
        { "algorithm": "bfs" | "dijkstra" | "astar" }

    Response will include:
        - path: list of [row, col] coordinates
        - visited_order: traversal order for frontend animation
        - path_length: number of steps
        - nodes_explored: total cells visited
        - time_ms: solve duration
    """
    # TODO:
    # 1. Fetch maze from DB by maze_id
    # 2. Validate start and end cells exist
    # 3. Dispatch to the correct algorithm class (BFS / Dijkstra / A*)
    # 4. Return SolveResult schema
    return {"message": f"solve maze {maze_id} — coming soon"}
