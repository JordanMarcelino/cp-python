### https://leetcode.com/problems/maximum-average-pass-ratio/

from heapq import heappop, heappush
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def ratio_gain(n_pass: int, total: int) -> float:
            return (n_pass + 1) / (total + 1) - n_pass / total

        heap = []
        for n_pass, total in classes:
            heappush(heap, (-ratio_gain(n_pass, total), n_pass, total))

        for _ in range(extraStudents):
            _, n_pass, total = heappop(heap)
            heappush(heap, (-ratio_gain(n_pass + 1, total + 1), n_pass + 1, total + 1))

        return sum([n_pass / total for _, n_pass, total in heap]) / len(heap)
