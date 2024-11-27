### https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i

from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        paths = {i: [i - 1] for i in reversed(range(n))}

        results = []
        for src, dst in queries:
            paths[dst].append(src)

            q = deque([(path, 1) for path in paths[n - 1]])
            visit = set()
            while q:
                src, cnt = q.popleft()
                if not src:
                    results.append(cnt)
                    break

                for path in paths[src]:
                    if path not in visit:
                        visit.add(path)
                        q.append((path, cnt + 1))

        return results
