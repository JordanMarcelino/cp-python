### https://leetcode.com/problems/count-the-number-of-ideal-arrays/

import math
from collections import defaultdict


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        sieve = list(range(maxValue + 1))
        for i in range(2, int(maxValue**0.5) + 1):
            if sieve[i] == i:
                for j in range(i * i, maxValue + 1, i):
                    if sieve[j] == j:
                        sieve[j] = i

        def factors(n: int) -> int:
            res = defaultdict(int)
            while n > 1:
                smallest_prime = sieve[n]
                res[smallest_prime] += 1
                n //= smallest_prime
            return res

        res = 0
        for i in range(1, maxValue + 1):
            ways = 1
            for exp in factors(i).values():
                ways = (ways * math.comb(n - 1 + exp, exp)) % MOD
            res += ways % MOD

        return res % MOD
