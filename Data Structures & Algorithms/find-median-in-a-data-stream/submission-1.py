import heapq
class MedianFinder:

    def __init__(self):
        self.smaller_max_heap = []
        self.larger_min_heap = []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.smaller_max_heap,num * -1)

        if len(self.smaller_max_heap) >= len(self.larger_min_heap) + 1:
            val = heapq.heappop(self.smaller_max_heap)
            heapq.heappush(self.larger_min_heap,val * -1)
        
        if len(self.smaller_max_heap) + 1 <= len(self.larger_min_heap):
            val = heapq.heappop(self.larger_min_heap)
            heapq.heappush(self.smaller_max_heap,val * -1)
        
        if self.smaller_max_heap and self.larger_min_heap and self.smaller_max_heap[0]*-1 > self.larger_min_heap[0]:
            val = heapq.heappop(self.smaller_max_heap)
            heapq.heappush(self.larger_min_heap,val * -1)

    def findMedian(self) -> float:

        if len(self.smaller_max_heap) > len(self.larger_min_heap):
            return self.smaller_max_heap[0]*-1
        elif len(self.larger_min_heap) > len(self.smaller_max_heap):
            return self.larger_min_heap[0]
        else:
            return (self.larger_min_heap[0] + (self.smaller_max_heap[0]*-1))/2
        
        