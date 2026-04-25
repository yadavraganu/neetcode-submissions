class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(asteroids)):
            ins_flag = True
            while stack and (stack[-1] > 0 and asteroids[i] < 0) and ins_flag:
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    ins_flag = False
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                else:
                    ins_flag = False
            if ins_flag:
                stack.append(asteroids[i])
        return stack