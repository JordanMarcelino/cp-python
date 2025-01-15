### https://leetcode.com/problems/minimize-xor/


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt1, cnt2 = bin(num1).count("1"), bin(num2).count("1")
        ans = num1
        i = 0
        while cnt1 != cnt2:
            if cnt1 > cnt2 and (1 << i) & num1 > 0:
                ans ^= 1 << i
                cnt1 -= 1
            if cnt1 < cnt2 and (1 << i) & num1 == 0:
                ans ^= 1 << i
                cnt1 += 1
            i += 1

        return ans
