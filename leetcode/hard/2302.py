### https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, ans, cur_sum = 0, 0, 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum * (r - l + 1) >= k:
                cur_sum -= nums[l]
                l += 1

            ans += r - l + 1

        return ans
