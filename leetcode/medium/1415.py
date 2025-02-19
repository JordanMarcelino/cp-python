### https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def dfs(i: int, txt: str) -> bool:
            if i == n:
                ans.append(txt)
                return True

            for c in "abc":
                if i and txt[-1] == c:
                    continue

                new_txt = f"{txt}{c}"
                dfs(i + 1, new_txt)

            return False

        dfs(0, "")
        return ans[k - 1] if k <= len(ans) else ""
