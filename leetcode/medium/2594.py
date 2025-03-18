### https://leetcode.com/problems/minimum-time-to-repair-cars/

from math import sqrt
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair(time: int) -> bool:
            cnt = 0
            for rank in ranks:
                cnt += int(sqrt(time / rank))
                if cnt >= cars:
                    return True

            return False

        l, r = 1, max(ranks) * cars**2
        while l <= r:
            m = l + (r - l) // 2
            if can_repair(m):
                r = m - 1
            else:
                l = m + 1

        return l
