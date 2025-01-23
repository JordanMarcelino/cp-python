### https://leetcode.com/problems/count-servers-that-communicate/

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    if row_cnt[r] > 1 or col_cnt[c] > 1:
                        cnt += 1

        return cnt
