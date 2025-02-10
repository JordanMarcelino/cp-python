### https://leetcode.com/problems/clear-digits/


class Solution:
    def clearDigits(self, s: str) -> str:
        N = len(s)

        ans = []
        for i in range(N):
            if s[i].isdigit():
                ans.pop()
            else:
                ans.append(s[i])

        return "".join(ans)
