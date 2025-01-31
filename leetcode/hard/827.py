### https://leetcode.com/problems/making-a-large-island/

from typing import List, Tuple


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ADJ = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        prnt = {}

        def find(pos: Tuple[int, int]) -> Tuple[int, int]:
            if prnt.get(pos, pos) != pos:
                prnt[pos] = find(prnt.get(pos, pos))
            return prnt.get(pos, pos)

        dp = {}
        seen = set()

        def dfs(r: int, c: int) -> int:
            if (r, c) in dp:
                return dp[(r, c)]
            seen.add((r, c))

            area = 1
            for dr, dc in ADJ:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < N
                    and 0 <= nc < N
                    and (nr, nc) not in seen
                    and grid[nr][nc] == 1
                ):
                    prnt[(nr, nc)] = find((r, c))
                    area += dfs(nr, nc)

            dp[(r, c)] = area
            return area

        ans = float("-inf")
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    root = set()
                    for dr, dc in ADJ:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                            root.add(find((nr, nc)))

                    new_island = 0
                    for pos in root:
                        new_island += dp[pos]
                    ans = max(ans, new_island + 1)

        return ans
