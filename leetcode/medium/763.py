### https://leetcode.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}

        size = end = 0
        ans = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, last[c])

            if i == end:
                ans.append(size)
                size = 0

        return ans
