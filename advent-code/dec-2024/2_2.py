### https://adventofcode.com/2024/day/2#part2

import sys
from typing import List


def create_reports(inp: List[str]) -> List[List[int]]:
    reports = []
    for s in inp:
        reports.append(list(map(int, s.split())))
    return reports


def is_report_safe(report: List[int]) -> bool:
    def _is_report_safe(report: List[int]) -> bool:
        increasing = all(
            1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)
        )
        decreasing = all(
            1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1)
        )
        return increasing or decreasing

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if _is_report_safe(modified_report):
            return True
    return False


def count_safe_reports(reports: List[List[int]]) -> int:
    safe = 0

    for report in reports:
        if is_report_safe(report):
            safe += 1
    return safe


inp = sys.stdin.read().strip().split("\n")

reports = create_reports(inp)
print(count_safe_reports(reports))
