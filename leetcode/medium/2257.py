### https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        def mark_guarded(r: int, c: int) -> None:
            for nr in range(r + 1, m):
                if grid[nr][c] in [1, 2]:
                    break
                grid[nr][c] = 3
            for nr in reversed(range(0, r)):
                if grid[nr][c] in [1, 2]:
                    break
                grid[nr][c] = 3
            for nc in range(c + 1, n):
                if grid[r][nc] in [1, 2]:
                    break
                grid[r][nc] = 3
            for nc in reversed(range(0, c)):
                if grid[r][nc] in [1, 2]:
                    break
                grid[r][nc] = 3

        for r, c in guards:
            mark_guarded(r, c)

        unguarded = 0
        for r in grid:
            for c in r:
                if c == 0:
                    unguarded += 1

        return unguarded
