class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and stack[-1][1] < curr:
                idx = stack.pop()[0]
                res[idx] = i - idx 
            stack.append((i,curr))
        return res