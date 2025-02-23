### https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]

        i, j = 1, 0
        while i < len(preorder):
            node = TreeNode(preorder[i])
            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node

            stack.append(node)
            while stack and j < len(postorder) and stack[-1].val == postorder[j]:
                stack.pop()
                j += 1

            i += 1

        return root
