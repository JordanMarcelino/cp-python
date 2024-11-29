### https://neetcode.io/problems/two-integer-sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = {}
        for i, num in enumerate(nums):
            if num in sum_hash:
                return [sum_hash[num], i]
            sum_hash[target - num] = i
