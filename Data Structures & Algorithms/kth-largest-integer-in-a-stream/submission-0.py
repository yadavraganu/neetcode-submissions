import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.storage = []
        self.length = k
        for num in nums:
            heapq.heappush(self.storage,num)
    def add(self, val: int) -> int:
        heapq.heappush(self.storage,val)
        l = self.length
        while len(self.storage) > l:
            heapq.heappop(self.storage)
        res = self.storage[0]
        return res

        
