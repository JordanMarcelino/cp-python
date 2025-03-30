### https://leetcode.com/problems/apply-operations-to-maximize-score/

from heapq import heapify, heappop
from math import sqrt
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        N = len(nums)

        def prime_score(n: int) -> int:
            count = 0
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    count += 1
                    while n % i == 0:
                        n //= i
            if n > 1:
                count += 1
            return count

        prime_factors = [prime_score(num) for num in nums]

        left_bound = [-1] * N
        right_bound = [N] * N
        stack = []

        for i, score in enumerate(prime_factors):
            while stack and prime_factors[stack[-1]] < score:
                right_bound[stack.pop()] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)

        max_heap = [(-nums[i], i) for i in range(N)]
        heapify(max_heap)
        score = 1

        while max_heap and k > 0:
            num, i = heappop(max_heap)
            num = -num

            count = min((i - left_bound[i]) * (right_bound[i] - i), k)

            score = (score * pow(num, count, MOD)) % MOD
            k -= count

        return score
