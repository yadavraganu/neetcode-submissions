class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                stack_ind, stack_val = stack.pop()
                res[stack_ind] = i - stack_ind
            stack.append((i,temp))

        return res

        