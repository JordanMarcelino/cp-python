### https://leetcode.com/problems/shifting-letters-ii/

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = [ord(c) - ord("a") for c in s]

        query = [0] * (len(s) + 1)
        for [start, end, dr] in shifts:
            query[start] += -1 if dr else 1
            query[end + 1] += 1 if dr else -1

        shift = 0
        for i in reversed(range(len(query))):
            shift += query[i]
            s[i - 1] = (shift + s[i - 1]) % 26

        return "".join([chr(ord("a") + c) for c in s])
