### https://leetcode.com/problems/find-the-count-of-good-integers/


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        ans = [0]
        seen = set()

        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] *= i * factorial[i - 1]

        def dfs(l: int, r: int, num: list[int]) -> None:
            if l > r:
                num = int("".join(map(str, num)))
                if num % k == 0:
                    ans[0] += count_permutation(str(num))

                return

            for d in range(10):
                if l != 0 or d != 0:
                    num[l] = num[r] = d
                    dfs(l + 1, r - 1, num)

        def count_permutation(num: str) -> int:
            counter = [0] * 10
            for d in num:
                counter[int(d)] += 1

            key = "".join(map(str, counter))
            if key in seen:
                return 0

            seen.add(key)
            res = factorial[n]
            for cnt in counter:
                res //= factorial[cnt]

            if not counter[0]:
                return res

            counter[0] -= 1
            zero_res = factorial[n - 1]
            for cnt in counter:
                zero_res //= factorial[cnt]

            return res - zero_res

        dfs(0, n - 1, [0] * n)
        return ans[0]
