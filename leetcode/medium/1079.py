### https://leetcode.com/problems/letter-tile-possibilities/

from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)

        def dfs() -> int:
            ans = 0
            for c in cnt:
                if cnt[c]:
                    cnt[c] -= 1
                    ans += 1 + dfs()
                    cnt[c] += 1

            return ans

        return dfs()
