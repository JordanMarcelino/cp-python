### https://leetcode.com/problems/trapping-rain-water-ii/

from heapq import heappop, heappush
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])
        ADJ = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        min_heap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        ans = 0
        max_h = -1
        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            ans += max_h - h

            for dr, dc in ADJ:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and heightMap[nr][nc] != -1:
                    heappush(min_heap, (heightMap[nr][nc], nr, nc))
                    heightMap[nr][nc] = -1

        return ans
