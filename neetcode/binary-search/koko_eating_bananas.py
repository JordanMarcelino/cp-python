### https://neetcode.io/problems/eating-bananas

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        l, r = 1, max(piles)

        while l <= r:
            m = r - (r - l) // 2
            nh = sum([ceil(pile / m) for pile in piles])

            if nh > h:
                l = m + 1
            else:
                r = m - 1

        return r - (r - l) // 2
