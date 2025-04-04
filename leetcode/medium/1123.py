### https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode, d: int) -> Tuple[Optional[TreeNode], int]:
            if not node:
                return (None, d)

            l_node, l_d = dfs(node.left, d + 1)
            r_node, r_d = dfs(node.right, d + 1)
            if l_d > r_d:
                return (l_node, l_d)
            elif r_d > l_d:
                return (r_node, r_d)
            else:
                return (node, l_d)

        node, _ = dfs(root, 0)
        return node
