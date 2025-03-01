### https://leetcode.com/problems/shortest-common-supersequence/


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in reversed(range(N)):
            for j in reversed(range(M)):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        ans = []
        i = j = 0
        while i < N and j < M:
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] > dp[i][j + 1]:
                ans.append(str1[i])
                i += 1
            else:
                ans.append(str2[j])
                j += 1

        while i < N:
            ans.append(str1[i])
            i += 1

        while j < M:
            ans.append(str2[j])
            j += 1

        return "".join(ans)
