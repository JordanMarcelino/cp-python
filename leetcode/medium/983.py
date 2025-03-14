### https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {len(days): 0}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]

            dp[i] = float("inf")
            j = i
            for cost, dur in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + dur:
                    j += 1
                dp[i] = min(dp[i], cost + dfs(j))

            return dp[i]

        return dfs(0)
