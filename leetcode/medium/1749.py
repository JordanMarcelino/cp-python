### https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_end = max_sum = float("-inf")
        min_end = min_sum = float("inf")
        for num in nums:
            max_end = max(max_end + num, num)
            min_end = min(min_end + num, num)

            max_sum = max(max_sum, max_end)
            min_sum = min(min_sum, min_end)

        return max(abs(max_sum), abs(min_sum))
