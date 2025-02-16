### https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description/

from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        seen = set()

        def dfs(i: int) -> bool:
            if i == len(ans):
                return True

            for num in reversed(range(1, n + 1)):
                if num in seen:
                    continue
                if num > 1 and (i + num >= len(ans) or ans[i + num]):
                    continue

                seen.add(num)
                ans[i] = num
                if num > 1:
                    ans[i + num] = num

                j = i + 1
                while j < len(ans) and ans[j]:
                    j += 1

                if dfs(j):
                    return True

                seen.remove(num)
                ans[i] = 0
                if num > 1:
                    ans[i + num] = 0

            return False

        dfs(0)
        return ans
