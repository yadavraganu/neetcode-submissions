from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:      
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popped
        
    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return False if len(self.q1) or len(self.q2) else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()