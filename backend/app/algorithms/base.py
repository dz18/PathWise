from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class SolverResult:
    """
    Returned by every algorithm after a solve attempt.

    path          — ordered [row, col] steps from start to end.
                    Empty list if no solution exists.
    visited_order — every cell examined during traversal, in order.
                    Used by the frontend to animate the search.
    """
    path: list[list[int]] = field(default_factory=list)
    visited_order: list[list[int]] = field(default_factory=list)


# Wall index constants — matches the cell format [N, S, E, W]
NORTH = 0
SOUTH = 1
EAST  = 2
WEST  = 3

# (row_delta, col_delta, wall_on_current_cell, wall_on_neighbour)
DIRECTIONS = [
    (-1,  0, NORTH, SOUTH),   # move north
    ( 1,  0, SOUTH, NORTH),   # move south
    ( 0,  1, EAST,  WEST),    # move east
    ( 0, -1, WEST,  EAST),    # move west
]


class SolverBase(ABC):
    """
    Abstract base class for all pathfinding algorithms.

    Subclasses implement solve() and return a SolverResult.
    Grid format: grid[row][col] = [N, S, E, W] wall booleans.
                 True  = wall present (cannot pass)
                 False = open passage (can pass)
    """

    def __init__(
        self,
        grid: list[list[list[bool]]],
        start: tuple[int, int],
        end: tuple[int, int],
    ):
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def can_move(self, row: int, col: int, direction: int) -> bool:
        """Return True if moving in `direction` from (row, col) is not blocked by a wall."""
        return not self.grid[row][col][direction]

    def get_neighbours(self, row: int, col: int) -> list[tuple[int, int]]:
        """Return all cells reachable from (row, col) — no walls blocking the path."""
        neighbours = []
        for dr, dc, wall, _ in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if self.in_bounds(nr, nc) and self.can_move(row, col, wall):
                neighbours.append((nr, nc))
        return neighbours

    def reconstruct_path(
        self, came_from: dict[tuple, tuple], end: tuple[int, int]
    ) -> list[list[int]]:
        """Walk the came_from map backwards to build the solution path."""
        path = []
        current = end
        while current is not None:
            path.append(list(current))
            current = came_from.get(current)
        path.reverse()
        return path

    @abstractmethod
    def solve(self) -> SolverResult:
        """Run the algorithm and return a SolverResult."""
        ...