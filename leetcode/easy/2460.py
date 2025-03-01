### https://leetcode.com/problems/apply-operations-to-an-array/

from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        i = 0
        for j in range(N):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums
