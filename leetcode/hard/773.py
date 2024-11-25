### https://leetcode.com/problems/sliding-puzzle/

from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        b = "".join([str(c) for r in board for c in r])
        q = deque([(b.index("0"), b, 0)])
        visit = set([b])

        while q:
            i, b, n = q.popleft()
            if b == "123450":
                return n

            b_arr = list(b)
            for j in adj[i]:
                new_b_arr = b_arr.copy()
                new_b_arr[i], new_b_arr[j] = new_b_arr[j], new_b_arr[i]
                new_b = "".join(new_b_arr)

                if new_b not in visit:
                    q.append((j, new_b, n + 1))
                    visit.add(new_b)

        return -1
