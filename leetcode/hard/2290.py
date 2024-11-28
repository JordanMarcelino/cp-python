### https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner

from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r_adj, c_adj = {}, {}

        for i in range(m):
            if i % m == 0 and m > 1:
                r_adj[i] = [i + 1]
            elif i % m == m - 1:
                r_adj[i] = [i - 1]
            else:
                r_adj[i] = [i - 1, i + 1]

        for i in range(n):
            if i % n == 0 and n > 1:
                c_adj[i] = [i + 1]
            elif i % n == n - 1:
                c_adj[i] = [i - 1]
            else:
                c_adj[i] = [i - 1, i + 1]

        dist = [[float("inf") for _ in range(n)] for _ in range(m)]
        dist[0][0] = 0

        q = deque()
        q.append((0, 0))
        while q:
            r, c = q.popleft()

            for i in range(len(r_adj[r])):
                if dist[r_adj[r][i]][c] > dist[r][c] + grid[r_adj[r][i]][c]:
                    dist[r_adj[r][i]][c] = dist[r][c] + grid[r_adj[r][i]][c]

                    if grid[r_adj[r][i]][c]:
                        q.append((r_adj[r][i], c))
                    else:
                        q.appendleft((r_adj[r][i], c))

            for i in range(len(c_adj[c])):
                if dist[r][c_adj[c][i]] > dist[r][c] + grid[r][c_adj[c][i]]:
                    dist[r][c_adj[c][i]] = dist[r][c] + grid[r][c_adj[c][i]]

                    if grid[r][c_adj[c][i]]:
                        q.append((r, c_adj[c][i]))
                    else:
                        q.appendleft((r, c_adj[c][i]))

        return dist[-1][-1]
