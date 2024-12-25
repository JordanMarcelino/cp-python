### https://leetcode.com/problems/unique-paths-iii/

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        OBS, START, END = -1, 1, 2
        ADJ = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        num_obs = 0
        start, end = None, None
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == START:
                    start = (r, c)
                if grid[r][c] == END:
                    end = (r, c)
                if grid[r][c] == OBS:
                    num_obs += 1

        TOTAL_SQUARES = ROWS * COLS - num_obs
        seen = set()

        print(start, end, ROWS, COLS, TOTAL_SQUARES)

        def dfs(pos):
            seen.add(pos)
            r, c = pos

            if grid[r][c] == END and len(seen) == TOTAL_SQUARES:
                seen.remove(pos)
                return 1

            ans = 0
            for dr, dc in ADJ:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] != OBS
                    and (nr, nc) not in seen
                ):
                    ans += dfs((nr, nc))

            seen.remove(pos)
            return ans

        return dfs(start)
