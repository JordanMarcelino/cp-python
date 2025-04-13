### https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for cur in range(target, num - 1, -1):
                dp[cur] |= dp[cur - num]

            if dp[target]:
                return dp[target]

        return dp[target]
