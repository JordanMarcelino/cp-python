### https://leetcode.com/problems/max-chunks-to-make-sorted/

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cur_max, res = float("-inf"), 0
        for i, num in enumerate(arr):
            cur_max = max(cur_max, num)
            if cur_max == i:
                res += 1

        return res
