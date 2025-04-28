### https://leetcode.com/problems/count-the-number-of-fair-pairs/

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        ans = 0
        for i in range(len(nums)):
            left = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1)

            ans += right - left

        return ans
