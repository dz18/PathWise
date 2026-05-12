from typing import Literal

from pydantic import BaseModel, Field


# ------------------------------------------------------------------
# Request schemas (inbound)
# ------------------------------------------------------------------

class SolveRequest(BaseModel):
    """Body for POST /mazes/{id}/solve"""
    algorithm: Literal["bfs", "dijkstra", "astar"] = Field(
        ...,
        description="Pathfinding algorithm to use",
    )


# ------------------------------------------------------------------
# Response schemas (outbound)
# ------------------------------------------------------------------

class SolveResult(BaseModel):
    """
    Returned after a successful solve.

    path           — ordered list of [row, col] from start to end
    visited_order  — all cells the algorithm examined, in traversal order
                     used by the frontend to animate the search
    path_length    — number of steps in the solution (len of path)
    nodes_explored — total cells visited during the search
    time_ms        — server-side solve time in milliseconds
    algorithm      — which algorithm produced this result
    """
    algorithm: str
    path: list[list[int]]
    visited_order: list[list[int]]
    path_length: int
    nodes_explored: int
    time_ms: float