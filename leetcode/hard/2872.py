### https://leetcode.com/problems/maximum-number-of-k-divisible-components/

from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        res = 0

        def dfs(node: int, parent: int) -> int:
            val = values[node]

            for adj in graph[node]:
                if adj != parent:
                    val += dfs(adj, node)

            if val % k == 0:
                nonlocal res
                res += 1

            return val

        dfs(0, -1)
        return res
