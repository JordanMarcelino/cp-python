### https://leetcode.com/problems/largest-divisible-subset/

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()

        dp = {}

        def dfs(i: int, prev: int) -> int:
            if i == N:
                return []
            if (i, prev) in dp:
                return dp[(i, prev)]

            ans = dfs(i + 1, prev)
            if nums[i] % prev == 0:
                take = [nums[i]] + dfs(i + 1, nums[i])
                ans = take if len(take) > len(ans) else ans

            dp[(i, prev)] = ans
            return ans

        return dfs(0, 1)
