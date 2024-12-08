### https://leetcode.com/problems/two-best-non-overlapping-events/description/

from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()

        max_suffix = [0] * n
        max_suffix[n - 1] = events[n - 1][2]

        for i in range(n - 2, -1, -1):
            max_suffix[i] = max(events[i][2], max_suffix[i + 1])

        max_sum = 0
        for i in range(n):
            l, r = i + 1, n - 1
            next_event = -1

            while l <= r:
                m = l + (r - l) // 2
                if events[m][0] > events[i][1]:
                    next_event = m
                    r = m - 1
                else:
                    l = m + 1

            if next_event != -1:
                max_sum = max(max_sum, events[i][2] + max_suffix[next_event])
            max_sum = max(max_sum, events[i][2])

        return max_sum
