### https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        diff = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        return (
            not diff
            or len(diff) == 2
            and s1[diff[0]] == s2[diff[1]]
            and s1[diff[1]] == s2[diff[0]]
        )
