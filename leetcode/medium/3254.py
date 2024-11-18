### https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results = []
        for i in range(len(nums) - k + 1):
            power = True
            start = nums[i]

            for num in nums[i + 1 : i + k]:
                if num != start + 1:
                    results.append(-1)
                    power = False
                    break
                else:
                    start = num

            if power:
                results.append(nums[i + k - 1])

        return results
