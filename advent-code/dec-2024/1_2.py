### https://adventofcode.com/2024/day/1

import sys
from collections import defaultdict
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


def calculate_similarity_score(left: List[int], right: list[int]) -> int:
    appear = defaultdict(int)

    for num in right:
        appear[num] += 1

    return sum([appear[num] * num for num in left])


inp = sys.stdin.read().strip().split("\n")

left, right = create_pairs(inp)
print(calculate_similarity_score(left, right))
