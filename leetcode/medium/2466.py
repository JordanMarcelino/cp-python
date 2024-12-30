### https://leetcode.com/problems/count-ways-to-build-good-strings/


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = {0: 1}

        for i in range(1, high + 1):
            dp[i] = (dp.get(i - zero, 0) + dp.get(i - one, 0)) % MOD

        return sum([dp[i] for i in range(low, high + 1)]) % MOD
