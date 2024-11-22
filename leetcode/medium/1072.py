### https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hash = defaultdict(int)

        for row in matrix:
            row_key = tuple(row)

            if row[0]:
                row_key = tuple([1 - x for x in row])

            hash[row_key] += 1

        return max(hash.values())
