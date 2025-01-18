### https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

from collections import defaultdict, deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direction = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        q = deque([(0, 0, 0)])
        min_cost = defaultdict(lambda: float("inf"))

        while q:
            r, c, cost = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return cost

            for d, [dr, dc] in direction.items():
                nr = r + dr
                nc = c + dc
                n_cost = cost if grid[r][c] == d else cost + 1

                if 0 <= nr < ROWS and 0 <= nc < COLS and n_cost < min_cost[(nr, nc)]:
                    min_cost[(nr, nc)] = n_cost
                    if grid[r][c] == d:
                        q.appendleft((nr, nc, n_cost))
                    else:
                        q.append((nr, nc, n_cost))
