### https://leetcode.com/problems/design-a-number-container-system/

from collections import defaultdict
from heapq import heappop, heappush


class NumberContainers:

    def __init__(self):
        self.idx_num = {}
        self.num_idx = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idx_num[index] = number
        heappush(self.num_idx[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_idx:
            return -1

        while self.num_idx[number]:
            if self.idx_num[self.num_idx[number][0]] == number:
                return self.num_idx[number][0]
            heappop(self.num_idx[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
