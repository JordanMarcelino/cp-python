### https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_divide(n: int) -> bool:
            return sum([c // n for c in candies]) >= k

        l, r = 1, max(candies)
        if can_divide(r):
            return r

        while l < r:
            m = l + (r - l) // 2
            if can_divide(m):
                l = m + 1
            else:
                r = m

        return l - 1
