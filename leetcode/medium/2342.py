### https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(num: int) -> int:
            ans = 0
            while num > 0:
                ans += num % 10
                num //= 10
            return ans

        digit_map = defaultdict(list)
        for num in nums:
            heappush(digit_map[sum_digits(num)], -num)

        pairs = list(filter(lambda x: len(x) > 1, digit_map.values()))
        if len(pairs) == 0:
            return -1

        ans = float("-inf")
        for pair in pairs:
            a, b = heappop(pair), heappop(pair)
            ans = max(ans, abs(a + b))

        return ans
