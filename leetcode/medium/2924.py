### https://leetcode.com/problems/find-champion-ii

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n

        for src, dst in edges:
            in_degree[dst] += 1

        champions = []
        for i, degree in enumerate(in_degree):
            if not degree:
                champions.append(i)

        if len(champions) > 1:
            return -1
        return champions[0]
