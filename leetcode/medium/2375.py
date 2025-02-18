### https://leetcode.com/problems/construct-smallest-number-from-di-string/


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = [0] * (len(pattern) + 1)
        seen = set()

        def dfs(i: int) -> bool:
            if i == len(ans):
                return True

            for num in range(1, 10):
                if num in seen:
                    continue
                if i and (
                    pattern[i - 1] == "I"
                    and num < ans[i - 1]
                    or pattern[i - 1] == "D"
                    and num > ans[i - 1]
                ):
                    continue

                seen.add(num)
                ans[i] = num

                if dfs(i + 1):
                    return True

                seen.remove(num)

            return False

        dfs(0)
        return "".join([str(c) for c in ans])
