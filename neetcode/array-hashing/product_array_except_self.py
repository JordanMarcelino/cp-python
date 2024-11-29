### https://neetcode.io/problems/products-of-array-discluding-self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            l, r = i - 1, i + 1

            prod = 1
            while l >= 0:
                prod *= nums[l]
                l -= 1
            while r < len(nums):
                prod *= nums[r]
                r += 1
            res.append(prod)

        return res
