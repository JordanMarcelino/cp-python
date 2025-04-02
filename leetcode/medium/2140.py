### https://leetcode.com/problems/solving-questions-with-brainpower/

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * (N + 1)

        for i in reversed(range(N)):
            points, brainpower = questions[i]
            next_q = i + brainpower + 1

            dp[i] = max(points + (dp[next_q] if next_q < N else 0), dp[i + 1])

        return dp[0]
