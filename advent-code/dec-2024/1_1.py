### https://adventofcode.com/2024/day/1

import sys
from typing import List


def create_pairs(inp: List[str]) -> tuple[List[int]]:
    left, right = [], []
    for loc in inp:
        i, j = loc.split()
        left.append(int(i))
        right.append(int(j))

    return left, right


def calculate_total_distance(left: List[int], right: List[int]) -> int:
    left.sort()
    right.sort()
    return sum([abs(i - j) for i, j in zip(left, right)])


inp = sys.stdin.read().strip().split("\n")

left, right = create_pairs(inp)
print(calculate_total_distance(left, right))
