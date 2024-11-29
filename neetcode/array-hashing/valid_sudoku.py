### https://neetcode.io/problems/valid-sudoku

from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_squares = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                nr = ceil((r + 1) / 3)
                nc = ceil((c + 1) / 3)

                if not board[r][c].isnumeric():
                    continue
                if (
                    board[r][c] in seen_rows[r]
                    or board[r][c] in seen_cols[c]
                    or board[r][c] in seen_squares[(nr, nc)]
                ):
                    return False

                seen_rows[r].add(board[r][c])
                seen_cols[c].add(board[r][c])
                seen_squares[(nr, nc)].add(board[r][c])

        return True
