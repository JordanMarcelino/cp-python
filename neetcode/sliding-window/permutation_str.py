### https://neetcode.io/problems/permutation-string


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26
        matches = 26

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1

        for i in range(26):
            matches -= 1 if s1_freq[i] != s2_freq[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord("a")
            s2_freq[idx] += 1
            if s1_freq[idx] == s2_freq[idx]:
                matches += 1
            if s1_freq[idx] + 1 == s2_freq[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord("a")
            s2_freq[idx] -= 1
            if s1_freq[idx] == s2_freq[idx]:
                matches += 1
            if s1_freq[idx] - 1 == s2_freq[idx]:
                matches -= 1

            l += 1

        return matches == 26
