### https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        N = len(nums)

        ans = 0
        for i in range(N - 2):
            if 2 * (nums[i] + nums[i + 2]) == nums[i + 1]:
                ans += 1

        return ans
