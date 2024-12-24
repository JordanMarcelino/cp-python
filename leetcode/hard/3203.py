### https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

from heapq import defaultdict, heappop, heappush
from math import ceil
from typing import List


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        def build_graph(edges):
            graph = defaultdict(list)
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            return graph

        graph1 = build_graph(edges1)
        graph2 = build_graph(edges2)

        def get_diameter(node, parent, graph):
            max_d = 0
            max_child_d = [0, 0]

            for adj in graph[node]:
                if adj != parent:
                    adj_d, adj_max_leaf_d = get_diameter(adj, node, graph)
                    max_d = max(max_d, adj_d)

                    heappush(max_child_d, adj_max_leaf_d)
                    heappop(max_child_d)

            max_d = max(max_d, sum(max_child_d))
            return [max_d, 1 + max(max_child_d)]

        d1, _ = get_diameter(0, -1, graph1)
        d2, _ = get_diameter(0, -1, graph2)

        return max(d1, d2, 1 + ceil(d1 / 2) + ceil(d2 / 2))
