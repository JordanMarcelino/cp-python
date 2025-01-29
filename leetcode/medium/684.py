### https://leetcode.com/problems/redundant-connection/

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        prnt = [i for i in range(len(edges) + 1)]

        def find(n: int) -> int:
            if n != prnt[n]:
                prnt[n] = find(prnt[n])
            return prnt[n]

        for n1, n2 in edges:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return [n1, n2]

            prnt[p2] = p1
