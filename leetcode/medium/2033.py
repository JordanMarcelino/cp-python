### https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [c for row in grid for c in row]

        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1

        nums.sort()
        median = nums[len(nums) // 2]

        return sum(abs(num - median) // x for num in nums)
