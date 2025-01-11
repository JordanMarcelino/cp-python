### https://leetcode.com/problems/construct-k-palindrome-strings/

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        s_cnt = Counter(s)
        odd_cnt, even_cnt = 0, 0
        for cnt in s_cnt.values():
            if cnt & 1:
                odd_cnt += 1
            else:
                even_cnt += 1

        if odd_cnt > k:
            return False
        return True
