class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        stack = []
        res = list(range(len(heights)))
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                idx = stack.pop()
                res[idx] = -1
            stack.append(i)
        return [i for i in res if i != -1]
        