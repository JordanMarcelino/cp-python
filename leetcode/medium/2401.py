### https://leetcode.com/problems/longest-nice-subarray/

from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, bitmask, ans = 0, 0, 0
        for r in range(len(nums)):
            while bitmask & nums[r]:
                bitmask ^= nums[l]
                l += 1

            bitmask |= nums[r]
            ans = max(ans, r - l + 1)

        return ans
