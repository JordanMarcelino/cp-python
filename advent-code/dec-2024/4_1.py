### https://adventofcode.com/2024/day/4

import sys
from typing import List


def count_xmas(inp: List[str]) -> int:
    KEYWORD = "XMAS"
    ROWS, COLS = len(inp), len(inp[0])
    DIRECTION = [
        (0, 1),  # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
    ]

    def is_keyword(r: int, c: int, dr: int, dc: int) -> bool:
        for i in range(len(KEYWORD)):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < ROWS and 0 <= nc < COLS) or inp[nr][nc] != KEYWORD[i]:
                return False
        return True

    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in DIRECTION:
                if is_keyword(r, c, dr, dc):
                    count += 1

    return count


inp = sys.stdin.read().strip().split("\r\n")

print(count_xmas(inp))
