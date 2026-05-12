import heapq

from app.algorithms.base import SolverBase, SolverResult


# Default traversal cost per cell type.
# Extend this dict when you add weighted terrain to the maze editor
# (e.g. mud = 3, water = 5, teleporter = 0).
DEFAULT_WEIGHT = 1


class DijkstraSolver(SolverBase):
    """
    Dijkstra's Algorithm — finds the lowest-cost path in a weighted maze.

    How it works:
        Uses a min-heap (priority queue) to always expand the cheapest
        unvisited cell first. When all cells have the same cost (DEFAULT_WEIGHT)
        it produces the same result as BFS, but explores more systematically
        and handles weighted terrain correctly.

    Time complexity:  O((V + E) log V)
    Space complexity: O(V)
    Best for:         Weighted mazes where different cells have different costs.
                      Falls back to BFS behaviour on uniform-weight mazes.

    Cell weights:
        Override get_weight() in a subclass or pass a weight_map to support
        terrain types (e.g. swamp tiles that cost more to traverse).
    """

    def __init__(self, *args, weight_map: dict[tuple, int] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        # weight_map: {(row, col): cost} — defaults to 1 for all cells
        self.weight_map = weight_map or {}

    def get_weight(self, row: int, col: int) -> int:
        """Return the traversal cost of entering cell (row, col)."""
        return self.weight_map.get((row, col), DEFAULT_WEIGHT)

    def solve(self) -> SolverResult:
        start, end = self.start, self.end

        # Min-heap entries: (cumulative_cost, row, col)
        heap: list[tuple[int, int, int]] = [(0, *start)]
        came_from: dict[tuple, tuple | None] = {start: None}
        cost_so_far: dict[tuple, int] = {start: 0}
        visited_order: list[list[int]] = [list(start)]

        while heap:
            current_cost, row, col = heapq.heappop(heap)
            current = (row, col)

            if current == end:
                path = self.reconstruct_path(came_from, end)
                return SolverResult(path=path, visited_order=visited_order)

            # Skip if we've already found a cheaper route to this cell
            if current_cost > cost_so_far.get(current, float("inf")):
                continue

            for neighbour in self.get_neighbours(row, col):
                new_cost = current_cost + self.get_weight(*neighbour)
                if new_cost < cost_so_far.get(neighbour, float("inf")):
                    cost_so_far[neighbour] = new_cost
                    came_from[neighbour] = current
                    visited_order.append(list(neighbour))
                    heapq.heappush(heap, (new_cost, *neighbour))

        # No path found
        return SolverResult(path=[], visited_order=visited_order)
