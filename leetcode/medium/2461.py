### https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        begin = 0
        end = 0
        cur_sum = 0
        num_to_idx = {}

        while end < len(nums):
            cur_num = nums[end]
            last_seen = num_to_idx.get(cur_num, -1)

            while begin <= last_seen or end - begin + 1 > k:
                cur_sum -= nums[begin]
                begin += 1

            num_to_idx[cur_num] = end
            cur_sum += cur_num

            if end - begin + 1 == k:
                ans = max(ans, cur_sum)
            end += 1

        return ans
