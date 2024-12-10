### https://adventofcode.com/2024/day/5

import sys
from collections import defaultdict, deque
from typing import List


def get_rules_and_pages(
    inp: List[str],
) -> tuple[List[tuple[int, int]], List[List[int]]]:
    rules = []
    pages = []

    l = 0
    for i in range(len(inp)):
        try:
            src, dst = inp[i].split("|")
            rules.append((src, dst))
        except Exception:
            l = i + 1
            break

    for i in range(l, len(inp)):
        pages.append(list(map(int, inp[i].split(","))))

    return rules, pages


def build_graph(
    rules: List[tuple[int, int]],
) -> dict[int, List[int]]:
    graph = defaultdict(list)

    for src, dst in rules:
        graph[int(src)].append(int(dst))

    return graph


def topological_sort(graph: dict[int, List[int]], page: List[int]) -> List[int]:
    filtered_graph = defaultdict(list)
    in_degree = {node: 0 for node in page}

    for node in page:
        for neighbor in graph[node]:
            if neighbor in in_degree:
                filtered_graph[node].append(neighbor)
                in_degree[neighbor] += 1

    queue = deque([node for node in page if in_degree[node] == 0])
    ordered_pages = []

    while queue:
        current = queue.popleft()
        ordered_pages.append(current)
        for neighbor in filtered_graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_pages


def correct_pages(rules: List[tuple[int, int]], pages: List[List[int]]):
    graph = build_graph(rules)
    middle_pages = []

    for page in pages:
        sorted_page = topological_sort(graph, page)
        if sorted_page != page:
            middle_pages.append(sorted_page[len(sorted_page) // 2])

    return middle_pages


def count_and_sum_middle_page(
    rules: List[tuple[int, int]], pages: List[List[int]]
) -> int:
    return sum(correct_pages(rules, pages))


inp = sys.stdin.read().strip().split("\n")

rules, pages = get_rules_and_pages(inp)
print(count_and_sum_middle_page(rules, pages))
