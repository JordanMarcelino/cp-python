### https://neetcode.io/problems/longest-substring-without-duplicates


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0

        seen = set()
        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            res = max(res, i - l + 1)

        return res
