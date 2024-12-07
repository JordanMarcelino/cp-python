### https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/

from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = l + (r - l) // 2

            if sum((num - 1) // m for num in nums) <= maxOperations:
                r = m
            else:
                l = m + 1

        return l
