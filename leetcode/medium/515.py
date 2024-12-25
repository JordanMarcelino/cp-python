### https://leetcode.com/problems/find-largest-value-in-each-tree-row/

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []

        q = deque([root])
        while q:
            max_val = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max_val)

        return ans
