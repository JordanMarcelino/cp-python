### https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet = max_diff = max_val = 0
        for num in nums:
            max_triplet = max(max_triplet, max_diff * num)
            max_diff = max(max_diff, max_val - num)
            max_val = max(max_val, num)

        return max_triplet
