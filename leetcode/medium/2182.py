### https://leetcode.com/problems/construct-string-with-repeat-limit/

from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        chars = sorted(list(set(s)))

        res = []
        while chars:
            c = chars.pop()
            if len(chars) == 0 and cnt[c] > repeatLimit:
                res.append(c * repeatLimit)
            elif cnt[c] <= repeatLimit:
                res.append(c * cnt[c])
                cnt[c] = 0
            else:
                cnt[c] -= repeatLimit
                res.append(c * repeatLimit)

                if len(chars) >= 1:
                    n_c = chars.pop()
                    res.append(n_c)

                    cnt[n_c] -= 1
                    if cnt[n_c] > 0:
                        chars.append(n_c)
                if cnt[c] > 0:
                    chars.append(c)

        return "".join(res)
