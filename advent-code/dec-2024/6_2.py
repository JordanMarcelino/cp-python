### https://adventofcode.com/2024/day/6#part2

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


def simulate_guard(
    graph: List[List[str]], pos: tuple[int, int]
) -> set[tuple[int, int]]:
    ROWS, COLS = len(graph), len(graph[0])
    direction = 0
    states = set()

    while True:
        r, c = pos
        dr, dc = get_movement(direction)
        nr, nc = r + dr, c + dc

        current_state = (pos, direction)
        if current_state in states:
            return True
        states.add(current_state)

        if not (0 <= nr < ROWS and 0 <= nc < COLS):
            return False
        if graph[nr][nc] == "#":
            direction = (direction + 1) & 3
            continue

        pos = (nr, nc)


def count_loop_positions(inp: List[str]) -> int:
    graph, pos = build_graph(inp)
    ROWS, COLS = len(graph), len(graph[0])
    num_loop = 0

    for r in range(ROWS):
        for c in range(COLS):
            if graph[r][c] != "." or (r, c) == pos:
                continue

            graph[r][c] = "#"

            if simulate_guard(graph, pos):
                num_loop += 1

            graph[r][c] = "."

    return num_loop


inp = sys.stdin.read().strip().split("\n")
print(count_loop_positions(inp))
