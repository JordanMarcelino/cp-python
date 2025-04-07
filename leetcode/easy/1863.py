### https://leetcode.com/problems/sum-of-all-subset-xor-totals/

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)

        def backtrack(i: int, total: int) -> int:
            if i == N:
                return total

            skip = backtrack(i + 1, total)
            take = backtrack(i + 1, total ^ nums[i])
            return skip + take

        return backtrack(0, 0)
