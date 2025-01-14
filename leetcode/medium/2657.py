### https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n

        pref_a, pref_b = set(), set()
        for i in range(n):
            pref_a.add(A[i])
            pref_b.add(B[i])
            C[i] = len(pref_a.intersection(pref_b))

        return C
