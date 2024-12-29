### https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])

        chars = [[0] * 26 for _ in range(n)]
        for word in words:
            for j, c in enumerate(word):
                chars[j][ord(c) - ord("a")] += 1

        dp = [[-1] * len(target) for _ in range(n)]

        def dfs(i: int, j: int) -> int:
            if j == len(target):
                return 1
            if i == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            cnt = dfs(i + 1, j) % MOD
            cnt += (chars[i][ord(target[j]) - ord("a")] * dfs(i + 1, j + 1)) % MOD
            dp[i][j] = cnt % MOD

            return dp[i][j]

        return dfs(0, 0)
