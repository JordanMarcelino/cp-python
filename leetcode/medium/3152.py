### https://leetcode.com/problems/special-array-ii/

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1]
            if (
                nums[i] & 1
                and nums[i - 1] & 1
                or not nums[i] & 1
                and not nums[i - 1] & 1
            ):
                prefix[i] += 1

        result = []
        for l, r in queries:
            cnt = prefix[r] - (prefix[l] if l > 0 else 0)
            result.append(cnt == 0)

        return result
