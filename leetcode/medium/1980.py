### https://leetcode.com/problems/find-unique-binary-string/

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set()
        for num in nums:
            seen.add(int(num, 2))

        n = len(nums)
        for num in range(n + 1):
            if num in seen:
                continue

            binary = bin(num)[2:]
            return f"{(n - len(binary)) * '0'}{binary}"

        return ""
