### https://leetcode.com/problems/find-the-town-judge/

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num_trust, seen = [0] * n, set()
        for a, b in trust:
            num_trust[b - 1] += 1
            seen.add(a)

        for i, num in enumerate(num_trust):
            if i + 1 not in seen and num == n - 1:
                return i + 1

        return -1
