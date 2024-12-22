### https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description/

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        ans = [-1] * len(queries)

        groups = defaultdict(list)
        for i, [a, b] in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[b] > heights[a]:
                ans[i] = b
            else:
                h = max(heights[a], heights[b])
                groups[b].append((h, i))

        heap = []
        for i, h in enumerate(heights):
            for group in groups[i]:
                heappush(heap, group)

            while heap and h > heap[0][0]:
                _, q_i = heappop(heap)
                ans[q_i] = i

        return ans
