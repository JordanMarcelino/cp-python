### https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:
        dp = [""] * (n + 1)
        dp[1] = "1"
        for i in range(2, n + 1):
            prev = dp[i - 1]
            prev_len = len(prev)

            cnt = 1
            for j in range(prev_len):
                if j < prev_len - 1 and prev[j] == prev[j + 1]:
                    cnt += 1
                else:
                    dp[i] += f"{cnt}{prev[j]}"
                    cnt = 1

        return dp[n]
