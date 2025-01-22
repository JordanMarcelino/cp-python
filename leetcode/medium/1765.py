### https://leetcode.com/problems/map-of-highest-peak/

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        ADJ = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    q.append((r, c))

        seen = set(list(q))
        while q:
            r, c = q.popleft()

            for dr, dc in ADJ:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc))

                    if isWater[r][c] and not isWater[nr][nc]:
                        grid[nr][nc] = 1
                    else:
                        grid[nr][nc] = grid[r][c] + 1

        return grid
