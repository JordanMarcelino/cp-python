### https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        adj = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        q = [(0, 0, 0)]
        visit = set()

        while q:
            t, r, c = heappop(q)
            if (r, c) == (m - 1, n - 1):
                return t

            for dr, dc in adj:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visit:
                    x = 1
                    if (grid[nr][nc] - t) & 1:
                        x = 0

                    heappush(q, (max(t + 1, grid[nr][nc] + x), nr, nc))
                    visit.add((nr, nc))
