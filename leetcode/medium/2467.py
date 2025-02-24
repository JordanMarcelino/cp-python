### https://leetcode.com/problems/most-profitable-path-in-a-tree/

from collections import defaultdict
from typing import List


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        bob_step = [-1] * len(amount)

        def dfs_bob(node: int, prnt: int, step: int) -> bool:
            if node == 0:
                return True

            for adj in graph[node]:
                if adj == prnt:
                    continue

                if dfs_bob(adj, node, step + 1):
                    bob_step[node] = step
                    return True

            return False

        def dfs_alice(node: int, prnt: int, step: int) -> int:
            ans = 0
            if bob_step[node] == -1 or step < bob_step[node]:
                ans += amount[node]
            elif step == bob_step[node]:
                ans += amount[node] // 2

            max_child_ans = float("-inf")
            for adj in graph[node]:
                if adj == prnt:
                    continue
                child_ans = dfs_alice(adj, node, step + 1)
                max_child_ans = max(max_child_ans, child_ans)

            return ans if max_child_ans == float("-inf") else ans + max_child_ans

        dfs_bob(bob, -1, 0)
        return dfs_alice(0, -1, 0)
