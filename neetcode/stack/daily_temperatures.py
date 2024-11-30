### https://neetcode.io/problems/daily-temperatures

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        arr = []
        for i, t in enumerate(temperatures):
            while arr and t > arr[-1][0]:
                nt, j = arr.pop()
                res[j] = i - j
            arr.append((t, i))

        return res
