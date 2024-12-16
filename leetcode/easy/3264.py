### https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            num, i = heappop(heap)
            new_num = num * multiplier
            nums[i] = new_num
            heappush(heap, (new_num, i))

        return nums
