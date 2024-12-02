### https://neetcode.io/problems/find-target-in-rotated-sorted-array

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        pivot = l
        l, r = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
