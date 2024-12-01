### https://leetcode.com/problems/check-if-n-and-its-double-exist/

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        exists = set()

        for num in arr:
            if num * 2 in exists or num / 2 in exists:
                return True
            exists.add(num)

        return False
