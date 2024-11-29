### https://neetcode.io/problems/string-encode-and-decode


from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            i = j + 1
            j = i + size
            res.append(s[i:j])
            i = j

        return res
