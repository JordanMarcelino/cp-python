### https://leetcode.com/problems/find-the-punishment-number-of-an-integer/


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_partition_equal(num: int, target: int) -> bool:
            if num == target:
                return True
            if num == 0:
                return target == 0

            for div in [10, 100, 1000]:
                if is_partition_equal(num // div, target - num % div):
                    return True

        return sum(
            [sqr for i in range(1, n + 1) if is_partition_equal(sqr := i * i, i)]
        )
