### https://leetcode.com/problems/count-vowel-strings-in-ranges/

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWEL = {c for c in "aiueo"}

        prefix_cnt, cnt = [], 0
        for word in words:
            cnt += 1 if word[0] in VOWEL and word[-1] in VOWEL else 0
            prefix_cnt.append(cnt)

        ans = [0] * len(queries)
        for i, [start, end] in enumerate(queries):
            ans[i] = prefix_cnt[end] - (prefix_cnt[start - 1] if start != 0 else 0)

        return ans
