### https://leetcode.com/problems/maximum-score-after-splitting-a-string/


class Solution:
    def maxScore(self, s: str) -> int:
        ans = float("-inf")
        left, right = 0, s.count("1")

        for i in range(len(s) - 1):
            left += 1 if s[i] == "0" else 0
            right -= 1 if s[i] == "1" else 0
            ans = max(ans, left + right)

        return ans
