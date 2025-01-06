### https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        pos = defaultdict(list)
        boxes = [int(c) for c in boxes]

        for i, c in enumerate(boxes):
            pos[c].append(i)

        for i in range(n):
            ans[i] = sum([abs(i - j) for j in pos[1]])

        return ans
