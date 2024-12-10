### https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        special = defaultdict(int)

        sub = s[0]
        special[sub] += 1

        for i in range(1, len(s)):
            if sub[-1] == s[i]:
                sub += s[i]
                tmp = ""
                for c in sub:
                    tmp += c
                    special[tmp] += 1
            else:
                special[s[i]] += 1
                sub = s[i]

        thrice = [len(c[0]) for c in list(filter(lambda c: c[1] >= 3, special.items()))]
        if not thrice:
            return -1

        return max(thrice)
