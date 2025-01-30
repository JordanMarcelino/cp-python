### https://leetcode.com/problems/is-graph-bipartite/

from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                q = deque([i])

                while q:
                    u = q.popleft()
                    for v in graph[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            q.append(v)
                        elif color[v] == color[u]:
                            return False

        return True
