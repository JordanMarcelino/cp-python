### https://neetcode.io/problems/median-of-two-sorted-arrays

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(nums2) < len(nums1):
            A, B = B, A

        total = len(A) + len(B)
        half = len(A) + (len(B) - len(A)) // 2

        l, r = 0, len(A) - 1
        while True:
            lm = l + (r - l) // 2
            rm = half - lm - 2

            a_l = A[lm] if lm >= 0 else float("-inf")
            a_r = A[lm + 1] if (lm + 1) < len(A) else float("inf")
            b_l = B[rm] if rm >= 0 else float("-inf")
            b_r = B[rm + 1] if (rm + 1) < len(B) else float("inf")

            if a_l <= b_r and b_l <= a_r:
                if total & 1:
                    return min(a_r, b_r)
                return (max(a_l, b_l) + min(a_r, b_r)) / 2
            elif a_l > b_r:
                r = lm - 1
            else:
                l = lm + 1
