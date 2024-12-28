### https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        k_sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] - nums[i - k] + nums[i])

        memo = {}

        def get_max_sum(i, cnt):
            if cnt == 3 or i > len(nums) - k:
                return 0
            if (i, cnt) in memo:
                return memo[(i, cnt)]

            inc = k_sums[i] + get_max_sum(i + k, cnt + 1)
            skip = get_max_sum(i + 1, cnt)

            memo[(i, cnt)] = max(inc, skip)
            return memo[(i, cnt)]

        i = 0
        ans = []
        while i <= len(nums) - k and len(ans) < 3:
            inc = k_sums[i] + get_max_sum(i + k, len(ans) + 1)
            skip = get_max_sum(i + 1, len(ans))

            if inc >= skip:
                ans.append(i)
                i += k
            else:
                i += 1

        return ans
