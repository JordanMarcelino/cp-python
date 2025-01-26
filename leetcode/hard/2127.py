### https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_deg = [0] * n
        chain_len = [0] * n
        visit = [False] * n

        for v in favorite:
            in_deg[v] += 1

        q = deque()
        for i in range(n):
            if in_deg[i] == 0:
                q.append(i)

        while q:
            v = q.popleft()
            visit[v] = True
            n_v = favorite[v]
            chain_len[n_v] = max(chain_len[n_v], chain_len[v] + 1)

            in_deg[n_v] -= 1
            if in_deg[n_v] == 0:
                q.append(n_v)

        max_cycle, pair_chains = 0, 0
        for i in range(n):
            if visit[i]:
                continue

            cycle_len = 0
            cur = i
            while not visit[cur]:
                visit[cur] = True
                cur = favorite[cur]
                cycle_len += 1

            if cycle_len == 2:
                pair_chains += 2 + chain_len[i] + chain_len[favorite[i]]
            else:
                max_cycle = max(max_cycle, cycle_len)

        return max(max_cycle, pair_chains)
