### https://leetcode.com/problems/count-largest-group/description/


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(num: int) -> int:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res

        freq = [0] * 37
        for i in range(1, n + 1):
            freq[sum_digits(i)] += 1

        largest = max(freq)
        return sum([cnt == largest for cnt in freq])
