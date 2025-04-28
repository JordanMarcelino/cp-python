### https://leetcode.com/problems/count-the-hidden-sequences/

from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_value = 0
        max_value = 0
        current = 0

        for diff in differences:
            current += diff
            if current < min_value:
                min_value = current
            if current > max_value:
                max_value = current

        return max(0, upper - lower - (max_value - min_value) + 1)
