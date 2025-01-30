### https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

from collections import defaultdict, deque
from typing import List, Set


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        color = [0] * (n + 1)

        def is_bipartite(i: int) -> bool:
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if color[v] == color[u]:
                        return False
                    if color[v] == 0:
                        color[v] = -color[u]
                        q.append(v)

            return True

        for i in range(1, n + 1):
            if color[i] == 0 and not is_bipartite(i):
                return -1

        def get_connected_components(i: int) -> Set[int]:
            components = {i}
            q = deque([i])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in components:
                        q.append(v)
                        components.add(v)
                        visited[v] = True
            return components

        def get_max_group(i: int) -> int:
            seen = [False] * (n + 1)
            seen[i] = True
            dist = 0
            q = deque([i])
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    for v in graph[u]:
                        if not seen[v]:
                            q.append(v)
                            seen[v] = True
                dist += 1

            return dist

        ans = 0
        visited = [False] * (n + 1)
        for i in range(1, n + 1):
            if visited[i]:
                continue
            visited[i] = True

            max_cnt = 0
            for v in get_connected_components(i):
                max_cnt = max(max_cnt, get_max_group(v))
            ans += max_cnt

        return ans
