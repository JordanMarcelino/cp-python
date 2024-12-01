### https://neetcode.io/problems/car-fleet

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for pos, sp in sorted(
            [(pos, sp) for pos, sp in zip(position, speed)], reverse=True
        ):
            time = (target - pos) / sp
            if arr and time <= arr[-1]:
                continue
            arr.append(time)

        return len(arr)
