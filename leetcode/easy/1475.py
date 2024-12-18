### https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for l in range(n):
            r = l + 1
            while r < n and prices[r] > prices[l]:
                r += 1
            if r < n and prices[r] <= prices[l]:
                prices[l] -= prices[r]

        return prices
