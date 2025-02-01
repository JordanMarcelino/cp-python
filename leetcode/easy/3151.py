### https://leetcode.com/problems/special-array-i/

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return not any(
            [
                (a & 1 and b & 1) or (not a & 1 and not b & 1)
                for a, b in zip(nums, nums[1:])
            ]
        )
