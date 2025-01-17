### https://leetcode.com/problems/neighboring-bitwise-xor/

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        flag = 0
        for num in derived:
            if num:
                flag = ~flag

        return not flag
