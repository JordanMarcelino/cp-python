### https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

from collections import defaultdict, deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(root, 0)])
        left, right = defaultdict(list), defaultdict(list)

        while q:
            node, lvl = q.popleft()

            if node.left and node.right:
                q.append((node.left, lvl + 1))
                q.append((node.right, lvl + 1))
            if (lvl + 1) & 1 and node.left and node.right:
                left[lvl].append(node.left)
                right[lvl].append(node.right)

        for lvl in left:
            n = len(left[lvl])
            for i in range(n):
                left[lvl][i].val, right[lvl][n - i - 1].val = (
                    right[lvl][n - i - 1].val,
                    left[lvl][i].val,
                )

        return root
