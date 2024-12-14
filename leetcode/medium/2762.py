### https://leetcode.com/problems/continuous-subarrays/

from collections import deque
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, res = 0, 0

        min_h, max_h = deque(), deque()
        for r in range(len(nums)):
            while min_h and nums[r] < nums[min_h[-1]]:
                min_h.pop()
            while max_h and nums[r] > nums[max_h[-1]]:
                max_h.pop()
            min_h.append(r)
            max_h.append(r)

            while nums[max_h[0]] - nums[min_h[0]] > 2:
                l += 1
                if min_h[0] < l:
                    min_h.popleft()
                if max_h[0] < l:
                    max_h.popleft()

            res += r - l + 1

        return res
