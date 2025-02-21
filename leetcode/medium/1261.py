### https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.val = set()
        self.dfs(root, 0)

    def dfs(self, node: TreeNode, val: int) -> None:
        if not node:
            return

        self.val.add(val)
        self.dfs(node.left, 2 * val + 1)
        self.dfs(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.val


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
