### https://neetcode.io/problems/count-number-of-islands

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dr, dc in adj:
                dfs(r + dr, c + dc)

        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands
