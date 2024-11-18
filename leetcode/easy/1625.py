### https://leetcode.com/problems/defuse-the-bomb/

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        if k < 0:
            result = []
            for i in range(len(code)):
                count = 0
                for j in range(1, (-k) + 1):
                    count += code[i - j]
                result.append(count)
            return result

        result = []

        for i in range(abs(k)):
            code.append(code[i])

        for i in range(len(code) - abs(k)):
            result.append(sum(code[i + 1 : i + 1 + k]))

        return result
