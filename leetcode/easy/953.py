### https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {c: i for i, c in enumerate(order)}
        new_words = [[dictionary[c] for c in word] for word in words]

        return all(w1 <= w2 for w1, w2 in zip(new_words, new_words[1:]))
