### https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def is_valid_cuts(coordinates: List[List[int]]) -> bool:
            coordinates.sort()

            max_c = coordinates[0][1]
            section = 0
            for c1, c2 in coordinates:
                if max_c <= c1:
                    section += 1
                if section >= 2:
                    return True
                max_c = max(max_c, c2)

            return False

        x = [[x1, x2] for [x1, _, x2, _] in rectangles]
        y = [[y1, y2] for [_, y1, _, y2] in rectangles]

        return is_valid_cuts(x) or is_valid_cuts(y)
