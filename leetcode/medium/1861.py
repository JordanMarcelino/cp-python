### https://leetcode.com/problems/rotating-the-box/description/

from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])

        for r in reversed(range(m)):
            i = n - 1
            for c in reversed(range(n)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                if box[r][c] == "*":
                    i = c - 1

        rotated_box = []
        for c in range(n):
            new_row = []
            for r in reversed(range(m)):
                new_row.append(box[r][c])
            rotated_box.append(new_row)

        return rotated_box
