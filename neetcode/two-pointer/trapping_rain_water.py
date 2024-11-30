### https://neetcode.io/problems/trapping-rain-water

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res
