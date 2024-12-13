### https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

from heapq import heapify, heappop
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0

        n = len(nums)
        q = [(num, i) for i, num in enumerate(nums)]
        mark = set()

        heapify(q)
        while q:
            num, i = heappop(q)
            if i in mark:
                continue

            mark.add(max(0, i - 1))
            mark.add(min(i + 1, n))
            score += num

        return score
