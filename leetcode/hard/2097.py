### https://leetcode.com/problems/valid-arrangement-of-pairs/

from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)

        for src, dst in pairs:
            graph[src].append(dst)
            degree[src] += 1
            degree[dst] -= 1

        src = pairs[0][0]
        for node, deg in degree.items():
            if deg == 1:
                src = node
                break

        res = []

        def dfs(src: int) -> None:
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)
                res.append((src, dst))

        dfs(src)
        return res[::-1]
