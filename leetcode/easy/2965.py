### https://leetcode.com/problems/find-missing-and-repeated-values/

from collections import defaultdict
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        counter = defaultdict(int)
        for r in grid:
            for c in r:
                counter[c] += 1

        ans = [0] * 2
        for val in range(1, N**2 + 1):
            if counter[val] > 1:
                ans[0] = val
            if counter[val] == 0:
                ans[1] = val

        return ans
