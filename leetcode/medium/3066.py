### https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)

        ans = 0
        while True:
            if len(nums) <= 1:
                break

            x, y = heappop(nums), heappop(nums)
            if x >= k and y >= k:
                break

            heappush(nums, min(x, y) * 2 + max(x, y))
            ans += 1

        return ans
