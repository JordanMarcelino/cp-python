### https://adventofcode.com/2024/day/6

import sys
from typing import List


def get_movement(direction: int) -> tuple[int, int]:
    direction_map = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
    }

    return direction_map[direction]


def build_graph(
    inp: List[str],
) -> tuple[List[List[str]], tuple[int, int]]:
    graph = [[""] * (len(inp[0]) - 1) for _ in range(len(inp))]
    start = None

    for i, row in enumerate(inp):
        row = row.replace("\r", "")
        for j, col in enumerate(row):
            if col == "^":
                start = (i, j)
            graph[i][j] = col

    return graph, start


def count_distinct_positions(inp: List[str]) -> int:
    graph, pos = build_graph(inp)
    distinct_positions = set([pos])
    direction = 0

    ROWS, COLS = len(graph), len(graph[0])
    while True:
        r, c = pos
        dr, dc = get_movement(direction)
        nr, nc = r + dr, c + dc

        if nr >= ROWS or nc >= COLS:
            break
        if graph[nr][nc] == "#":
            direction = (direction + 1) & 3
            continue

        pos = (nr, nc)
        distinct_positions.add((nr, nc))

    return len(distinct_positions)


inp = sys.stdin.read().strip().split("\n")
print(count_distinct_positions(inp))
