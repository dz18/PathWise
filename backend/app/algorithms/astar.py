import heapq

from app.algorithms.base import SolverBase, SolverResult


def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
    """
    Manhattan distance heuristic — admissible for grid mazes with
    no diagonal movement. Never overestimates the true cost, which
    guarantees A* finds the optimal path.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class AStarSolver(SolverBase):
    """
    A* Search — finds the shortest path using a heuristic to guide exploration.

    How it works:
        Like Dijkstra, but each cell is prioritised by f(n) = g(n) + h(n):
            g(n) = actual cost from start to this cell
            h(n) = estimated cost from this cell to end (Manhattan distance)

        The heuristic steers the search toward the goal, so A* typically
        explores far fewer cells than BFS or Dijkstra on open mazes.

    Time complexity:  O((V + E) log V) — but explores much less in practice
    Space complexity: O(V)
    Best for:         Large mazes where speed matters. Optimal with an
                      admissible heuristic (Manhattan distance qualifies).

    Tie-breaking:
        When two cells have the same f-score, we prefer the one with the
        higher g-score (closer to the goal). This reduces the number of
        cells explored in corridors with equal f-values.
    """

    def solve(self) -> SolverResult:
        start, end = self.start, self.end

        # Heap entries: (f_score, tie_breaker, g_score, row, col)
        # tie_breaker is a counter to ensure stable heap ordering
        counter = 0
        h_start = manhattan(start, end)
        heap: list = [(h_start, counter, 0, *start)]

        came_from: dict[tuple, tuple | None] = {start: None}
        g_score: dict[tuple, int] = {start: 0}
        visited_order: list[list[int]] = [list(start)]

        while heap:
            f, _, g, row, col = heapq.heappop(heap)
            current = (row, col)

            if current == end:
                path = self.reconstruct_path(came_from, end)
                return SolverResult(path=path, visited_order=visited_order)

            # Stale entry — a cheaper path to this cell was already found
            if g > g_score.get(current, float("inf")):
                continue

            for neighbour in self.get_neighbours(row, col):
                tentative_g = g + 1  # uniform cost, extend for weighted terrain

                if tentative_g < g_score.get(neighbour, float("inf")):
                    g_score[neighbour] = tentative_g
                    came_from[neighbour] = current
                    visited_order.append(list(neighbour))

                    h = manhattan(neighbour, end)
                    f = tentative_g + h

                    counter += 1
                    heapq.heappush(heap, (f, counter, tentative_g, *neighbour))

        # No path found
        return SolverResult(path=[], visited_order=visited_order)