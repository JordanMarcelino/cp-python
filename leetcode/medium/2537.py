### https://leetcode.com/problems/count-the-number-of-good-subarrays/

from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        l = ans = 0
        for r in range(len(nums)):
            k -= counter[nums[r]]
            counter[nums[r]] += 1

            while k <= 0:
                counter[nums[l]] -= 1
                k += counter[nums[l]]
                l += 1

            ans += l

        return ans
