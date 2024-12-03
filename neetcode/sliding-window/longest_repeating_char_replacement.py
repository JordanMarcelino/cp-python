### https://neetcode.io/problems/longest-repeating-substring-with-replacement

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        l, f, res = 0, 0, 0

        for r in range(len(s)):
            freq[s[r]] += 1
            f = max(f, freq[s[r]])

            while (r - l + 1) - f > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
