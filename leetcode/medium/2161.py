### https://leetcode.com/problems/partition-array-according-to-given-pivot/

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = [num for num in nums if num < pivot]
        middle = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]

        return left + middle + right
