### https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        ADJ = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        sorted_queries = sorted([(num, i) for i, num in enumerate(queries)])
        seen = [[False] * COLS for _ in range(ROWS)]
        seen[0][0] = True

        points = 0
        ans = [0] * len(queries)
        q = [(grid[0][0], 0, 0)]
        for threshold, i in sorted_queries:
            while q and q[0][0] < threshold:
                _, r, c = heappop(q)
                points += 1

                for dr, dc in ADJ:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and not seen[nr][nc]:
                        seen[nr][nc] = True
                        heappush(q, (grid[nr][nc], nr, nc))

            ans[i] = points

        return ans
