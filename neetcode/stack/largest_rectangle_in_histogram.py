### https://neetcode.io/problems/largest-rectangle-in-histogram

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        arr = []

        for i, h in enumerate(heights):
            ni = i
            while arr and arr[-1][1] > h:
                l, mh = arr.pop()
                max_area = max(max_area, mh * (i - l))
                ni = l
            arr.append((ni, h))

        for i, h in arr:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
