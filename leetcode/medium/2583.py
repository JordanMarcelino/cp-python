### https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

from collections import deque
from heapq import heappop, heappush
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []

        q = deque([root])
        while q:
            level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            heappush(level_sums, -level_sum)

        if len(level_sums) < k:
            return -1

        ans = 0
        for _ in range(k):
            ans = heappop(level_sums)

        return -ans
