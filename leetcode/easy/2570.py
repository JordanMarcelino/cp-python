### https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        N, M = len(nums1), len(nums2)
        ans = []

        i = j = 0
        while i < N and j < M:
            if nums1[i][0] == nums2[j][0]:
                ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        while i < N:
            ans.append(nums1[i])
            i += 1

        while j < M:
            ans.append(nums2[j])
            j += 1

        return ans
