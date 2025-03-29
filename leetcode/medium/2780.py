### https://leetcode.com/problems/minimum-index-of-a-valid-split/

from collections import Counter, defaultdict
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)

        prefix = defaultdict(int)
        suffix = Counter(nums)
        for i in range(N - 1):
            prefix[nums[i]] += 1
            suffix[nums[i]] -= 1

            if prefix[nums[i]] * 2 > i + 1 and suffix[nums[i]] * 2 > N - 1 - i:
                return i

        return -1
