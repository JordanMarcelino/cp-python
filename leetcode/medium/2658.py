### https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ADJ = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        seen = set()
        dp = {}

        def dfs(r: int, c: int) -> int:
            seen.add((r, c))

            ans = grid[r][c]
            for dr, dc in ADJ:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and (nr, nc) not in seen
                    and grid[nr][nc] > 0
                ):
                    ans += dfs(nr, nc)

            dp[(r, c)] = ans
            return ans

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0:
                    ans = max(ans, dfs(r, c))

        return ans
