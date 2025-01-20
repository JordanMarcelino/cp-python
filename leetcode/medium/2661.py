### https://leetcode.com/problems/first-completely-painted-row-or-column/

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        positions = {}

        for r in range(ROWS):
            for c in range(COLS):
                positions[mat[r][c]] = (r, c)

        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS
        for i, num in enumerate(arr):
            r, c = positions[num]
            row_cnt[r] += 1
            col_cnt[c] += 1

            if row_cnt[r] == COLS or col_cnt[c] == ROWS:
                return i

        return -1
