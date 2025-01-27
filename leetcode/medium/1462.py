### https://leetcode.com/problems/course-schedule-iv/

from collections import defaultdict, deque
from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        graph = defaultdict(list)
        in_deg = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            in_deg[b] += 1

        q = deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)

        course_prereq = defaultdict(set)
        while q:
            i = q.popleft()

            for j in graph[i]:
                course_prereq[j].add(i)
                for k in course_prereq[i]:
                    course_prereq[j].add(k)

                in_deg[j] -= 1
                if in_deg[j] == 0:
                    q.append(j)

        result = []
        for i, j in queries:
            result.append(i in course_prereq[j])
        return result
