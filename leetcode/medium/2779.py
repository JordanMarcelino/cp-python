### https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        cnt = float("-inf")
        l = 0
        for r in range(len(nums)):
            while not nums[r] - nums[l] <= 2 * k:
                l += 1

            cnt = max(cnt, r - l + 1)

        return cnt
