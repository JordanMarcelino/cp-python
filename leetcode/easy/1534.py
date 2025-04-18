### https://leetcode.com/problems/count-good-triplets/

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)

        def is_good_triplet(i: int, j: int, k: int) -> bool:
            return (
                abs(arr[i] - arr[j]) <= a
                and abs(arr[j] - arr[k]) <= b
                and abs(arr[i] - arr[k]) <= c
            )

        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    ans += is_good_triplet(i, j, k)

        return ans
