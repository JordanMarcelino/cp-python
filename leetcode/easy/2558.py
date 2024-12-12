### https://leetcode.com/problems/take-gifts-from-the-richest-pile/

from heapq import heapify, heappop, heappush
from math import floor, sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapify(gifts)

        for _ in range(k):
            gift = -heappop(gifts)
            heappush(gifts, -floor(sqrt(gift)))

        return -sum(gifts)
