### https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}

        res = []
        for x, y in queries:
            if x in balls:
                if colors[balls[x]] == 1:
                    del colors[balls[x]]
                else:
                    colors[balls[x]] -= 1

            balls[x] = y
            colors[y] = colors.get(y, 0) + 1
            res.append(len(colors))

        return res
