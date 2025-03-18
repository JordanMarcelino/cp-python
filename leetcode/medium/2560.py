### https://leetcode.com/problems/house-robber-iv/

from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)

        def can_steal(n: int) -> bool:
            i, cnt = 0, 0
            while i < N:
                if nums[i] <= n:
                    i += 1
                    cnt += 1

                if cnt == k:
                    return True
                i += 1

            return False

        l, r = min(nums), max(nums)
        while l <= r:
            m = l + (r - l) // 2
            if can_steal(m):
                r = m - 1
            else:
                l = m + 1

        return l
