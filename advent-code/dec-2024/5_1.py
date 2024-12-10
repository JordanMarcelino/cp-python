### https://adventofcode.com/2024/day/5

import sys
from collections import defaultdict
from typing import List


def get_rules_and_pages(inp: List[str]) -> tuple[dict[int, List[int]], List[List[int]]]:
    rules = defaultdict(list)
    pages = []

    l = 0
    for i in range(len(inp)):
        try:
            src, dst = inp[i].split("|")
            rules[int(dst)].append(int(src))
        except Exception:
            l = i + 1
            break

    for i in range(l, len(inp)):
        pages.append(list(map(int, inp[i].split(","))))

    return rules, pages


def count_and_sum_middle_page(
    rules: dict[int, List[int]], pages: List[List[int]]
) -> int:
    res = 0

    for page in pages:
        banned = set()
        skip = False

        for num in page:
            if num in banned:
                skip = True
                break

            for ban in rules[num]:
                banned.add(ban)

        if not skip:
            m = len(page) // 2
            res += page[m]

    return res


inp = sys.stdin.read().strip().split("\n")

rules, pages = get_rules_and_pages(inp)
print(count_and_sum_middle_page(rules, pages))
