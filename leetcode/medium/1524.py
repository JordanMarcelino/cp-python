### https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7

        ans = odd = total = 0
        even = 1
        for num in arr:
            total += num
            if total & 1:
                ans = (ans + even) % MOD
                odd += 1
            else:
                ans = (ans + odd) % MOD
                even += 1

        return int(ans)
