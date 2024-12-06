### https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        blacklist = set(banned)

        max_num, cur_sum = 0, 0
        l = 1
        while l <= n:
            while l <= n and cur_sum + l <= maxSum and l not in blacklist:
                cur_sum += l
                max_num += 1
                l += 1
            l += 1

        return max_num
