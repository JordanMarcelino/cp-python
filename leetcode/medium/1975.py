### https://leetcode.com/problems/maximum-matrix-sum/

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        max_sum = 0
        min_val = float("inf")
        neg_len = 0

        for row in matrix:
            for col in row:
                max_sum += abs(col)
                min_val = min(min_val, abs(col))

                if col < 0:
                    neg_len += 1

        if neg_len % 2 == 1:
            return max_sum - (min_val * 2)

        return max_sum
