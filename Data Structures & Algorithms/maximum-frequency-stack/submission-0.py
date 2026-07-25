from collections import defaultdict
import heapq
class FreqStack:

    def __init__(self):
        self.heap = []
        self.count_map = defaultdict(int)
        self.index = 0
    
    def push(self, val: int) -> None:

        self.count_map[val] = self.count_map.get(val,0) + 1
        heapq.heappush(self.heap,(-1*self.count_map[val], -1*self.index, val))
        self.index += 1
 
    def pop(self) -> int:

        _ , _ , val = heapq.heappop(self.heap)
        self.count_map[val] = self.count_map.get(val,0) - 1

        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()