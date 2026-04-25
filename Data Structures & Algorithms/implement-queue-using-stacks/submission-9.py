class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []        

    def push(self, x: int) -> None:
        self.s1.append(x)
        if not self.s2:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

    def pop(self) -> int:
        popped = self.s2.pop()
        if not self.s2:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return popped
        
    def peek(self) -> int:
        return self.s2[-1]
        
    def empty(self) -> bool:
        return False if len(self.s1 or self.s2) else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()