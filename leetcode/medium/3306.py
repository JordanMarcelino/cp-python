### https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)

        def atleast_k(k: int) -> int:
            vowels = defaultdict(int)
            non_vowels = 0
            ans = 0

            l = 0
            for r in range(N):
                if word[r] in "aiueo":
                    vowels[word[r]] += 1
                else:
                    non_vowels += 1

                while len(vowels) == 5 and non_vowels >= k:
                    ans += N - r
                    if word[l] in "aiueo":
                        vowels[word[l]] -= 1
                    else:
                        non_vowels -= 1

                    if vowels[word[l]] == 0:
                        del vowels[word[l]]
                    l += 1

            return ans

        return atleast_k(k) - atleast_k(k + 1)
