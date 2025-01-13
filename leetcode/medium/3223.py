### https://leetcode.com/problems/minimum-length-of-string-after-operations/

from collections import Counter
from math import ceil


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum([cnt - (ceil(cnt / 2) - 1) * 2 for cnt in Counter(s).values()])
