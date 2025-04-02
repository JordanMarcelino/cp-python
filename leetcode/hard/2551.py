### https://leetcode.com/problems/put-marbles-in-bags/

from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        pair_costs = [weights[i] + weights[i + 1] for i in range(N - 1)]
        pair_costs.sort()

        return sum(pair_costs[-(k - 1) :]) - sum(pair_costs[: k - 1])
