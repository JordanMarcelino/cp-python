### https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for num in nums:
            if num < k:
                return -1
            seen.add(num)

        return len(seen) if k not in seen else len(seen) - 1
