### https://leetcode.com/problems/count-number-of-bad-pairs/

from collections import Counter
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        counter = Counter([num - i for i, num in enumerate(nums)])

        total_pairs = N * (N - 1) // 2
        good_pairs = sum(cnt * (cnt - 1) // 2 for cnt in counter.values())

        return total_pairs - good_pairs
