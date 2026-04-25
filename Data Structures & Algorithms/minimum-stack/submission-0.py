class MinStack:

    def __init__(self):
        self.s = []
    def push(self, val: int) -> None:
        if not self.s:
            self.s.append((val,val))
        else:
            _ , min_val = self.s[-1]
            self.s.append((val,min(val,min_val)))

    def pop(self) -> None:
        return self.s.pop()[0]
        
    def top(self) -> int:
        return self.s[-1][0]
        
    def getMin(self) -> int:
        return self.s[-1][1]
        
