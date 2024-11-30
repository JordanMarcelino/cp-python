### https://neetcode.io/problems/max-water-container

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        res = 0
        while l < r:
            res = max(res, (r - l) * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
