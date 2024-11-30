### https://neetcode.io/problems/generate-parentheses

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(par: str, op: int, cl: int):
            if cl > op:
                return
            if len(par) == 2 * n:
                if cl == op:
                    res.append(par)
                return

            dfs(f"{par}(", op + 1, cl)
            dfs(f"{par})", op, cl + 1)

        dfs("", 0, 0)

        return res
