### https://adventofcode.com/2024/day/3#part2

import re
import sys
from typing import List


def mul(op: str) -> int:
    x, y = list(map(int, re.findall(r"\d{1,3}", op)))
    return x * y


def sanitize(inp: str) -> List[str]:
    return re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", inp, re.IGNORECASE)


def mul_it_over(inp: str) -> int:
    ops = sanitize(inp)
    res = 0

    enable = True
    for op in ops:
        if op == "do()":
            enable = True
        if op == "don't()":
            enable = False

        if not enable:
            continue
        if enable and op != "do()":
            res += mul(op)

    return res


inp = sys.stdin.read().strip()

print(mul_it_over(inp))
