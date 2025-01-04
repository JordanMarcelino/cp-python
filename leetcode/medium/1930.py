### https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans, left = set(), set()
        right = Counter(s)
        for m in s:
            right[m] -= 1
            for c in left:
                if right[c] > 0:
                    ans.add((c, m))
            left.add(m)

        return len(ans)
