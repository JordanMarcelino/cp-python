### https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([root])
        while q:
            nums = []
            for _ in range(len(q)):
                node = q.popleft()
                nums.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            sorted_nums = sorted(nums)
            num_idx = {num: i for i, num in enumerate(nums)}

            for i in range(len(nums)):
                if nums[i] != sorted_nums[i]:
                    res += 1

                    j = num_idx[sorted_nums[i]]
                    nums[j] = nums[i]
                    num_idx[nums[i]] = j

        return res
