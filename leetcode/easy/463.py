### https://leetcode.com/problems/island-perimeter/

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        adj = [[-1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r: int, c: int):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0

            grid[r][c] = -1
            ans = 0
            for dr, dc in adj:
                ans += dfs(r + dr, c + dc)
            return ans

        perimeter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    perimeter += dfs(r, c)

        return perimeter
