### https://leetcode.com/problems/string-matching-in-an-array/

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and len(words[i]) < len(words[j]) and words[i] in words[j]:
                    ans.add(words[i])

        return list(ans)
