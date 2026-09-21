from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        res = [0] * n

        for i in range(n):
            while stack and heights[i] > heights[stack[-1]]:
                popped = stack.pop()
                res[popped] += 1   # popped person sees this taller one
            if stack:
                res[stack[-1]] += 1  # also sees the next taller still in stack
            stack.append(i)

        return res
