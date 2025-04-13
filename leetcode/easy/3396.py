### https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)):
            return 0

        ans = 0
        while True:
            ans += 1
            nums = nums[3:]
            if len(nums) == len(set(nums)):
                break
        return ans
