### https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N - 2):
            if not nums[i]:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1

        return -1 if not nums[-1] or not nums[-2] else ans
