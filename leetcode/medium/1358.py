### https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)

        cnt = defaultdict(int)
        l, ans = 0, 0
        for r in range(N):
            cnt[s[r]] += 1

            while len(cnt) == 3:
                ans += N - r
                cnt[s[l]] -= 1

                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1

        return ans
