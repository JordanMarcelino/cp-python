### https://leetcode.com/problems/tuple-with-same-product/

from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N = len(nums)
        product_map = defaultdict(int)
        for i in range(N):
            for j in range(i + 1, N):
                product_map[nums[i] * nums[j]] += 1

        ans = 0
        for count in product_map.values():
            if count >= 2:
                ans += (count * (count - 1) // 2) * 8

        return ans
