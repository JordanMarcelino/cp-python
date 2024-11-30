### https://neetcode.io/problems/validate-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        arr = []
        for c in s:
            if c in pairs:
                arr.append(c)
            else:
                if not arr:
                    return False
                if pairs[arr.pop()] != c:
                    return False

        return len(arr) == 0
