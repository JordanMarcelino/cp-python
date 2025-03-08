### https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)

        ans = cnt = blocks[:k].count("W")
        for i in range(N - k):
            cnt += (blocks[i + k] == "W") - (blocks[i] == "W")
            ans = min(ans, cnt)
        return ans
