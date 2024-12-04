### https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l, r = 0, len(str2)
        for c in str1:
            if l < r and (ord(str2[l]) - ord(c)) % 26 < 2:
                l += 1

        return l == r
