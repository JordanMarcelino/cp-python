### https://leetcode.com/problems/count-of-interesting-subarrays/

from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prev = defaultdict(int)
        prev[0] += 1
        cnt = 0
        result = 0

        for num in nums:
            if num % modulo == k:
                cnt = (cnt + 1) % modulo

            result += prev[(cnt - k) % modulo]
            prev[cnt] += 1

        return result
