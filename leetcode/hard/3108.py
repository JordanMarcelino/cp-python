### https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        weight = [(1 << 30) - 1] * n
        group = [-1] * n
        for u, v, w in edges:
            graph[u].append(v)
            graph[v].append(u)
            weight[u] &= w
            weight[v] &= w

        def bfs(src: int) -> None:
            q = deque([src])
            while q:
                u = q.pop()
                weight[src] &= weight[u]

                for v in graph[u]:
                    if group[v] == -1:
                        group[v] = src
                        q.append(v)

        for i in range(n):
            if group[i] == -1:
                group[i] = i
                bfs(i)

        return [
            weight[group[src]] if group[src] == group[dst] else -1 for src, dst in query
        ]
