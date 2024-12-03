### https://leetcode.com/problems/adding-spaces-to-a-string/

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = []
        for i, s in enumerate(s):
            if spaces and spaces[0] == i:
                new_str.append(" ")
                spaces.pop(0)
            new_str.append(s)

        return "".join(new_str)
