### https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        N = len(nums)
        left = bisect_left(nums, 0)
        right = bisect_right(nums, 0)

        return max(left, N - right)
