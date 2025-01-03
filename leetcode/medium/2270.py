### https://leetcode.com/problems/number-of-ways-to-split-array/

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        prefix_sum, ans = 0, 0
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            if prefix_sum >= total_sum - prefix_sum:
                ans += 1

        return ans
