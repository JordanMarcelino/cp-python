### https://neetcode.io/problems/evaluate-reverse-polish-notation

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        def ops(a: int, b: int, operand: str):
            if operand == "+":
                return a + b
            if operand == "-":
                return b - a
            if operand == "*":
                return a * b
            if operand == "/":
                return int(float(b) / a)

        for token in tokens:
            if token.lstrip("-").isnumeric():
                numbers.append(int(token))
            else:
                a, b = numbers.pop(), numbers.pop()
                numbers.append(ops(a, b, token))

        return numbers[0]
