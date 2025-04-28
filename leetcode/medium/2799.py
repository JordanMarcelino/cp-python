### https://leetcode.com/problems/count-complete-subarrays-in-an-array/

from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        n_unique = len(set(nums))

        counter = defaultdict(int)
        l, ans = 0, 0
        for r in range(N):
            counter[nums[r]] += 1
            while len(counter) == n_unique:
                counter[nums[l]] -= 1
                if not counter[nums[l]]:
                    del counter[nums[l]]

                l += 1
                ans += N - r

        return ans
