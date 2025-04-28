### https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0

        start, min_i, max_i = -1, -1, -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                start = i
            if nums[i] == maxK:
                max_i = i
            if nums[i] == minK:
                min_i = i
            ans += max(0, min(min_i, max_i) - start)

        return ans
