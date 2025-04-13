### https://leetcode.com/problems/count-the-number-of-powerful-integers/


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def sanitize(x: int) -> int:
            ans = 0
            less = False
            for c in map(int, str(x)):
                if less:
                    ans = ans * 10 + limit
                elif c > limit:
                    less = True
                    ans = ans * 10 + limit
                else:
                    ans = ans * 10 + c

            return ans

        def count(x: int) -> int:
            ans = 0
            base = limit + 1
            prefix = str(x)[: -len(s)]
            for c in map(int, prefix):
                ans = ans * base + c
            if int(prefix + s) <= x:
                ans += 1

            return ans

        return count(sanitize(finish)) - count(sanitize(start - 1))
