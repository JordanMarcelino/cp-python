### https://leetcode.com/problems/count-days-without-meetings/

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        prev_end = 0
        for start, end in meetings:
            start = max(start, prev_end + 1)
            interval = end - start + 1
            days -= max(interval, 0)
            prev_end = max(prev_end, end)

        return days
