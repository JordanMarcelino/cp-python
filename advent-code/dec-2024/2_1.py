### https://adventofcode.com/2024/day/2

import sys
from typing import List


def create_reports(inp: List[str]) -> List[List[int]]:
    reports = []
    for s in inp:
        reports.append(list(map(int, s.split())))
    return reports


def is_report_safe(report: List[int]) -> bool:
    increasing = report[0] <= report[-1]
    for i in range(1, len(report)):
        if increasing and report[i] < report[i - 1]:
            return False
        if not increasing and report[i] > report[i - 1]:
            return False

    for i in range(1, len(report)):
        if 1 <= abs(report[i] - report[i - 1]) <= 3:
            continue
        return False
    return True


def count_safe_reports(reports: List[List[int]]) -> int:
    safe = 0

    for report in reports:
        if is_report_safe(report):
            safe += 1
    return safe


inp = sys.stdin.read().strip().split("\n")

reports = create_reports(inp)
print(count_safe_reports(reports))
