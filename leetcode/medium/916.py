### https://leetcode.com/problems/word-subsets/

from collections import defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        src = defaultdict(int)
        for word in words2:
            cur = defaultdict(int)
            for c in word:
                cur[c] += 1

            for c in cur:
                src[c] = max(src[c], cur[c])

        def is_universal(word: dict[str, int]) -> bool:
            for c, cnt in src.items():
                if word[c] < cnt:
                    return False
            return True

        ans = []
        for word in words1:
            cur = defaultdict(int)
            for c in word:
                cur[c] += 1

            if is_universal(cur):
                ans.append(word)

        return ans
