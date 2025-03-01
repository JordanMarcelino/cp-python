### https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        ans = 0
        for i in range(2, n):
            prev = 0
            nxt = i - 1

            while prev < nxt:
                target = arr[prev] + arr[nxt]

                if arr[i] > target:
                    prev += 1
                elif arr[i] < target:
                    nxt -= 1
                else:
                    dp[nxt][i] = dp[prev][nxt] + 1
                    ans = max(ans, dp[nxt][i])
                    prev += 1
                    nxt -= 1

        return ans + 2 if ans else 0
