### https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i, d = 0, 0
        while i < len(traversal):
            if not traversal[i].isdigit():
                d += 1
                i += 1
            else:
                j = i
                while j < len(traversal) and traversal[j].isdigit():
                    j += 1

                node = TreeNode(int(traversal[i:j]))
                while len(stack) > d:
                    stack.pop()

                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack and not stack[-1].right:
                    stack[-1].right = node

                stack.append(node)
                d = 0
                i = j

        return stack[0]
