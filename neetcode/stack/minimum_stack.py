### https://neetcode.io/problems/minimum-stack


class MinStack:
    def __init__(self):
        self.arr = []
        self.min_val = []

    def push(self, val: int) -> None:
        if not self.min_val:
            self.min_val.append(val)
        else:
            self.min_val.append(min(self.min_val[-1], val))
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
