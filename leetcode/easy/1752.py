### https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)

        cnt = 1
        for i in range(1, 2 * N):
            if nums[(i - 1) % N] <= nums[i % N]:
                cnt += 1
            else:
                cnt = 1
            if cnt == N:
                return True

        return N == 1
