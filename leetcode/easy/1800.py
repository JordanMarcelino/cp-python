### https://leetcode.com/problems/maximum-ascending-subarray-sum/

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum, max_sum = nums[0], nums[0]
        for a, b in zip(nums, nums[1:]):
            if b > a:
                cur_sum += b
            else:
                cur_sum = b
            max_sum = max(max_sum, cur_sum)

        return max_sum
