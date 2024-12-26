### https://leetcode.com/problems/target-sum/

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == len(nums):
                return total == target

            memo[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return memo[(i, total)]

        return dfs(0, 0)
