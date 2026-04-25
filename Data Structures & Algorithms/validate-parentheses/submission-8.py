class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        br_map = {')':'(','}':'{',']':'['}
        for i in s:
            if stack and i in br_map and br_map[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
