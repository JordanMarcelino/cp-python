### https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        num_to_group = {}
        for num in sorted(nums):
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(num)
            num_to_group[num] = len(groups) - 1

        ans = []
        for num in nums:
            ans.append(groups[num_to_group[num]].popleft())
        return ans
