### https://leetcode.com/problems/count-symmetric-integers/


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(n: int) -> bool:
            n_str = str(n)
            n_len = len(n_str)
            if n_len & 1:
                return False

            l_sum, r_sum = 0, 0
            for i in range(n_len // 2):
                l_sum += int(n_str[i])
                r_sum += int(n_str[n_len - i - 1])

            return l_sum == r_sum

        return sum([is_symmetric(i) for i in range(low, high + 1)])
