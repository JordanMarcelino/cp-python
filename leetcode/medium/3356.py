### https://leetcode.com/problems/zero-array-transformation-ii/

from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)

        def can_make_zero_array(k: int) -> bool:
            diff = [0] * (N + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r + 1] -= val

            curr_sum = 0
            for i in range(N):
                curr_sum += diff[i]
                if curr_sum < nums[i]:
                    return False

            return True

        l, r = 0, len(queries)
        if not can_make_zero_array(r):
            return -1

        while l < r:
            m = l + (r - l) // 2

            if can_make_zero_array(m):
                r = m
            else:
                l = m + 1

        return l
