### https://leetcode.com/problems/divide-array-into-equal-pairs/

from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for cnt in Counter(nums).values():
            if cnt & 1:
                return False

        return True
