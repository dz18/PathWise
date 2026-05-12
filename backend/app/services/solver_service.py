import time

from fastapi import HTTPException, status

from app.repositories.maze_repo import MazeRepository
from app.algorithms.bfs import BFSSolver
from app.algorithms.dijkstra import DijkstraSolver
from app.algorithms.astar import AStarSolver


# Map algorithm names to their solver classes
SOLVERS = {
    "bfs": BFSSolver,
    "dijkstra": DijkstraSolver,
    "astar": AStarSolver,
}


class SolverService:
    """
    Dispatches a maze to the correct pathfinding algorithm.
    Increments play_count on the maze after each solve.
    """

    def __init__(self):
        self.maze_repo = MazeRepository()

    async def solve(self, maze_id: str, algorithm: str) -> dict:
        """
        Fetch the maze, run the chosen algorithm, return the result.

        Returns:
            path           — list of [row, col] from start to end
            visited_order  — all cells visited during traversal (for animation)
            path_length    — number of steps in the solution
            nodes_explored — total cells the algorithm examined
            time_ms        — how long the solve took in milliseconds
            algorithm      — which algorithm was used

        Raises:
            400 if algorithm name is invalid
            404 if maze not found
            422 if maze has no start/end or is unsolvable
        """
        # TODO:
        # --- Validate algorithm ---
        # if algorithm not in SOLVERS:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail=f"Unknown algorithm '{algorithm}'. Choose from: {list(SOLVERS.keys())}",
        #     )

        # --- Fetch maze ---
        # maze = await self.maze_repo.find_by_id(maze_id)
        # if not maze:
        #     raise HTTPException(status_code=404, detail="Maze not found")

        # --- Validate start / end ---
        # if not maze.get("start") or not maze.get("end"):
        #     raise HTTPException(status_code=422, detail="Maze must have a start and end cell")

        # --- Run solver ---
        # solver = SOLVERS[algorithm](
        #     grid=maze["grid"],
        #     start=tuple(maze["start"]),
        #     end=tuple(maze["end"]),
        # )
        # start_time = time.perf_counter()
        # result = solver.solve()
        # elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)

        # --- Unsolvable ---
        # if not result.path:
        #     raise HTTPException(status_code=422, detail="No path exists between start and end")

        # --- Increment play count ---
        # await self.maze_repo.increment_play_count(maze_id)

        # return {
        #     "algorithm": algorithm,
        #     "path": result.path,
        #     "visited_order": result.visited_order,
        #     "path_length": len(result.path),
        #     "nodes_explored": len(result.visited_order),
        #     "time_ms": elapsed_ms,
        # }
        return {}