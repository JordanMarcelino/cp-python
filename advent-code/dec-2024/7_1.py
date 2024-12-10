### https://adventofcode.com/2024/day/7

import sys
from typing import List


def eval_expressions(nums: List[int], ops: List[str]) -> int:
    res = nums[0]

    for i, op in enumerate(ops):
        if op == "+":
            res += nums[i + 1]
        else:
            res *= nums[i + 1]

    return res


def is_total_possible(total: int, nums: List[int]) -> bool:
    operators = ["+", "*"]

    N = len(nums) - 1

    def generate_operator_combinations(
        combinations: List[List[str]], idx: int
    ) -> List[List[str]]:
        if idx == N:
            return [combinations]

        results = []
        for op in operators:
            results.extend(generate_operator_combinations(combinations + [op], idx + 1))
        return results

    combinations = generate_operator_combinations([], 0)

    for ops in combinations:
        if eval_expressions(nums, ops) == total:
            return True

    return False


def sum_possible_result(inp: List[str]) -> int:
    res = 0

    for equ in inp:
        total, nums = equ.replace("\r", "").split(": ")
        if is_total_possible(int(total), list(map(int, nums.split()))):
            res += int(total)

    return res


inp = sys.stdin.read().strip().split("\n")

print(sum_possible_result(inp))
