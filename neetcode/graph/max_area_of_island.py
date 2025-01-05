### https://neetcode.io/problems/max-area-of-island

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        seen = set()

        def dfs(r: int, c: int) -> int:
            seen.add((r, c))

            ans = 0
            for dr, dc in adj:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] == 1
                    and (nr, nc) not in seen
                ):
                    ans += 1
                    ans += dfs(nr, nc)

            return ans

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c) + 1)

        return ans
