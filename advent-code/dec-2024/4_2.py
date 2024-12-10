### https://adventofcode.com/2024/day/4#part2

import sys
from typing import List


def count_xmas(inp: List[str]) -> int:
    ROWS, COLS = len(inp), len(inp[0])

    def is_keyword(r: int, c: int) -> bool:
        top_left = (
            inp[r - 1][c - 1] == "M" and inp[r][c] == "A" and inp[r + 1][c + 1] == "S"
        )
        bottom_right = (
            inp[r - 1][c - 1] == "S" and inp[r][c] == "A" and inp[r + 1][c + 1] == "M"
        )
        top_right = (
            inp[r - 1][c + 1] == "M" and inp[r][c] == "A" and inp[r + 1][c - 1] == "S"
        )
        bottom_left = (
            inp[r - 1][c + 1] == "S" and inp[r][c] == "A" and inp[r + 1][c - 1] == "M"
        )

        return (top_left or bottom_right) and (top_right or bottom_left)

    count = 0
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if is_keyword(r, c):
                count += 1

    return count


inp = sys.stdin.read().strip().split("\r\n")

print(count_xmas(inp))
