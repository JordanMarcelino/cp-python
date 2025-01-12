### https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:
            return False

        open_idx, change_idx = [], []
        for i, c in enumerate(s):
            if locked[i] == "0":
                change_idx.append(i)
            elif c == "(":
                open_idx.append(i)
            elif c == ")":
                if open_idx:
                    open_idx.pop()
                elif change_idx:
                    change_idx.pop()
                else:
                    return False

        while open_idx and change_idx and open_idx[-1] < change_idx[-1]:
            open_idx.pop()
            change_idx.pop()

        return not open_idx
