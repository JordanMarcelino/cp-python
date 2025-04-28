### https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
from math import ceil
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        for k, cnt in Counter(answers).items():
            ans += ceil(float(cnt) / (k + 1)) * (k + 1)

        return int(ans)
