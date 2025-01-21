### https://leetcode.com/problems/grid-game/

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = float("inf")

        top = sum(grid[0])
        bottom = 0
        for i in range(n):
            top -= grid[0][i]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][i]

        return ans
