### https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1

        ans = 0
        n_inc, n_dec = 1, 1
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                n_inc += 1
                n_dec = 1
            elif nums[i] < nums[i - 1]:
                n_dec += 1
                n_inc = 1
            else:
                n_inc = 1
                n_dec = 1
            ans = max(ans, n_inc, n_dec)

        return ans
