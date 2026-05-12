from collections import deque

from app.algorithms.base import SolverBase, SolverResult


class BFSSolver(SolverBase):
    """
    Breadth-First Search — guarantees the shortest path (fewest steps).

    How it works:
        Explores cells layer by layer, radiating outward from the start.
        The first time it reaches the end cell, that path is guaranteed
        to be the shortest because BFS never revisits a cell and always
        processes closer cells before farther ones.

    Time complexity:  O(V + E) where V = cells, E = open passages
    Space complexity: O(V)
    Best for:         Unweighted mazes where all steps cost the same.
    """

    def solve(self) -> SolverResult:
        start, end = self.start, self.end
        queue: deque[tuple[int, int]] = deque([start])

        # came_from[cell] = the cell we arrived from (None for start)
        came_from: dict[tuple, tuple | None] = {start: None}
        visited_order: list[list[int]] = [list(start)]

        while queue:
            current = queue.popleft()

            if current == end:
                path = self.reconstruct_path(came_from, end)
                return SolverResult(path=path, visited_order=visited_order)

            for neighbour in self.get_neighbours(*current):
                if neighbour not in came_from:
                    came_from[neighbour] = current
                    visited_order.append(list(neighbour))
                    queue.append(neighbour)

        # No path found
        return SolverResult(path=[], visited_order=visited_order)