### https://leetcode.com/problems/closest-prime-numbers-in-range/

from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False

        prime = [i for i in range(left, right + 1) if sieve[i]]

        if len(prime) < 2:
            return [-1, -1]

        min_dist = float("inf")
        pair = [-1, -1]
        for i in range(1, len(prime)):
            dist = prime[i] - prime[i - 1]
            if dist < min_dist:
                min_dist = dist
                pair = [prime[i - 1], prime[i]]

        return pair
