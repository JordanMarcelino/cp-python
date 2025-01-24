### https://leetcode.com/problems/find-eventual-safe-states/

from collections import defaultdict
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for src, dst in enumerate(graph):
            edges[src].extend(dst)

        dp = {}
        seen = set()

        def dfs(node: int):
            if len(edges[node]) == 0:
                return True
            if node in seen:
                return False
            if node in dp:
                return dp[node]

            seen.add(node)

            safe = True
            for adj in edges[node]:
                safe = safe and dfs(adj)

            seen.remove(node)
            dp[node] = safe

            return safe

        results = []
        for i in range(len(graph)):
            if dfs(i):
                results.append(i)

        return results
