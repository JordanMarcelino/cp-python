### https://neetcode.io/problems/search-2d-matrix

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(array: List[int]) -> int:
            l, r = 0, len(array) - 1
            while l <= r:
                m = r - (r - l) // 2
                if array[m] == target:
                    return m
                if array[m] > target:
                    r = m - 1
                if array[m] < target:
                    l = m + 1
            return -1

        l, r = 0, len(matrix) - 1
        while l <= r:
            m = r - (r - l) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                break

        if not l <= r:
            return False

        return binary_search(matrix[r - (r - l) // 2]) != -1
