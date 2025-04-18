### https://leetcode.com/problems/count-good-triplets-in-an-array

from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        pos2 = {val: i for i, val in enumerate(nums2)}
        mapped = [pos2[val] for val in nums1]

        def update(tree: List[int], i: int, val: int) -> None:
            i += 1
            while i < len(tree):
                tree[i] += val
                i += i & -i

        def query(tree: List[int], i: int) -> int:
            res = 0
            i += 1
            while i > 0:
                res += tree[i]
                i -= i & -i

            return res

        tree = [0] * (N + 2)
        left_cnt = [0] * N
        for i in range(N):
            left_cnt[i] = query(tree, mapped[i])
            update(tree, mapped[i], 1)

        tree = [0] * (N + 2)
        right_cnt = [0] * N
        for i in reversed(range(N)):
            right_cnt[i] = query(tree, N) - query(tree, mapped[i])
            update(tree, mapped[i], 1)

        return sum([left_cnt[i] * right_cnt[i] for i in range(N)])
