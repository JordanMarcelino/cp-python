### https://leetcode.com/problems/move-pieces-to-obtain-a-string/


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True

        N = len(start)
        start += "@"
        target += "@"

        l, r = 0, 0
        while l < N or r < N:
            while l < N and start[l] == "_":
                l += 1
            while r < N and target[r] == "_":
                r += 1

            c = start[l]
            if c != target[r]:
                return False
            if c == "L" and l < r:
                return False
            if c == "R" and l > r:
                return False

            l += 1
            r += 1

        return True
