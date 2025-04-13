### https://leetcode.com/problems/count-good-numbers/

from math import ceil, floor


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def pow(x: int, y: int) -> int:
            res = 1
            while y:
                if y & 1:
                    res = res * x % MOD
                x = x * x % MOD
                y >>= 1

            return res

        odd_cnt = floor(n / 2)
        even_cnt = ceil(n / 2)

        return pow(5, even_cnt) * pow(4, odd_cnt) % MOD
