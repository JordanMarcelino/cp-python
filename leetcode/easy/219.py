### https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}
        for i, num in enumerate(nums):
            if num in memo and abs(memo[num] - i) <= k:
                return True
            memo[num] = i

        return False
